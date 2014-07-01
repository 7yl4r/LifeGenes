import logging
from os.path import join
from os import makedirs
from multiprocessing import Pool, cpu_count

from LifeGenes.Server.lifegenes_core import CellList
from LifeGenes.Server.lifegenes_core.Cell import Cell
from LifeGenes.Server.lifegenes_core.__util.appdirs import user_data_dir


pool = Pool(processes=cpu_count())


class environment:
	# prepares the needed data structures
	# parameters:
	# g        : GoL-like environment api handle
	def __init__(self, follyInstance):
		self.g = follyInstance
		saveDir = user_data_dir('LifeGenes', '7yl4r-ware')
		try:
			makedirs(saveDir)
		except OSError:
			pass  # probably the dir already exists...
		self.CELL_LIST_FILENAME = join(saveDir, 'lifeGenes_cellList.pk')

		self.originL = self.g.getlayer()  # starting layer

		# check for existing geneticColor layer
		currindex = 0
		self.colorIndex = None
		while currindex < self.g.numlayers():
			if self.g.getname(currindex) == 'geneticColor':
				# continue from where we left off
				self.colorIndex = currindex
				logging.info('geneticColor layer already exists, loading from file ' + self.CELL_LIST_FILENAME)
				# read cell genes from a file and make self.cellList
				self.cellList = CellList.CellList([0, 0])
				self.cellList.load(self.CELL_LIST_FILENAME)
				break
			else:
				currindex += 1
		if self.colorIndex is None:  # if we didn't find existing colorLayer
			logging.info('color layer not found. creating new environment')
			if self.g.empty():
				self.cellList = CellList.CellList([])
			else:
				# detect existing cells
				startpatt = self.g.getcells(self.g.getrect())  # get starting pattern array [x1,y1,x2,y2,...]
				self.cellList = CellList.CellList(startpatt)
				logging.info(str(len(startpatt) / 2) + ' cells found, ' + str(
					len(self.cellList.cells)) + ' trait objects created.')

			# add color layer
			if self.g.numlayers() + 1 > self.g.maxlayers():
				self.g.exit("You need to delete a layer.")

			# create layer for colors
			self.colorIndex = self.g.addlayer()
			self.g.setname('geneticColor')
			self.g.setrule('constant')  # use custom constant rule
			self.g.setcolors([0, 255, 0, 0, 0, 255])  # live states vary from green to blue
		self.g.setlayer(self.originL)  # set layer back to original layer
		assert (self.cellList is not None)


	def __del__(self):
		self.teardown()

	# close down the environment
	def teardown(self):
		self.g.setlayer(self.originL)  # ensure we are on the right layer
		self.update()  # ensure there are no half-built arrays
		self.drawColor()  # one last draw
		self.g.update()  # one last display update
		self.cellList.save(self.CELL_LIST_FILENAME)

	# cellMotions allows cells to move around in their environment while no evolution takes place
	# motion is based on values calculated from the cell's neural network
	# layer must be on the original layer, NOT the color layer.
	def cellMotions(self):
		for cell in self.cellList.cells:
			cell.move(self.g.setcell, self.g.getcell)

	# update the environment to match the changes in the given cell environment g
	def update(self):
		newPattern = self.g.getcells(self.g.getrect())
		# generate DNA for new cells
		newList = list()  # save this & add at end to not muck up the list
		newCells = list()
		jobs = list()
		for newCellIndex in range(len(newPattern) / 2):  # for all cells in newCellIndex
			# add the cell if it does not already exist
			xi = newPattern[newCellIndex * 2]  # newCell location
			yi = newPattern[newCellIndex * 2 + 1]
			existingCell = self.cellList.findCell(xi, yi)
			if existingCell is None:
				parents = list()
				newCell = Cell(xi, yi)
				neighbors = [[newCell.x - 1, newCell.y + 1],
				             [newCell.x, newCell.y + 1],
				             [newCell.x + 1, newCell.y + 1],
				             [newCell.x + 1, newCell.y],
				             [newCell.x + 1, newCell.y - 1],
				             [newCell.x, newCell.y - 1],
				             [newCell.x - 1, newCell.y - 1],
				             [newCell.x - 1, newCell.y]]
				for n in neighbors:
					cell = self.cellList.findCell(n[0], n[1])
					if cell is not None:  # add neighbor as parent if exists
						parents.append(cell)
					# if len(parents)==3: #this *might* improve efficiency, but only a little
					# break
				# self.g.note(str(newCell.x)+','+str(newCell.y)+' parents are: '+str(parents))

				# add inheritDNA job to the worker pool
				jobs.append(pool.apply_async(newCell.inheritDNA, (parents, newCell.getBases(),
				                                                  newCell.getMutationRisk(), newCell.getID())))
				newCells.append(newCell)

			else:  # keep old cell info;
				newList.append(existingCell)

		pool.join()  # allow all processes to finish before unblocking
		for job in jobs:
			dic = job()
			for cell in newCells:
				if cell.getID() is dic['ID']:
					cell.DNA = dic['DNA']

		newList.extend(newCells)
		self.cellList.cells = newList

	# uses self.g.update() and fixes self.cellList to match
	# depreciated version kept around (temporarily) for testing
	def update_depreciated(self):
		# self.g.autoupdate(True)#while debugging
		newPattern = self.g.getcells(self.g.getrect())
		# generate DNA for new cells
		cellsToAppend = list()  # save this & add at end to not muck up the list
		for newCellIndex in range(len(newPattern) / 2):  # for all cells in newCellIndex
			# add the cell if it does not already exist
			xi = newPattern[newCellIndex * 2]  # newCell location
			yi = newPattern[newCellIndex * 2 + 1]
			if self.cellList.findCell(xi, yi) is None:
				parents = list()
				newCell = Cell(xi, yi)
				neighbors = [[newCell.x - 1, newCell.y + 1],
				             [newCell.x, newCell.y + 1],
				             [newCell.x + 1, newCell.y + 1],
				             [newCell.x + 1, newCell.y],
				             [newCell.x + 1, newCell.y - 1],
				             [newCell.x, newCell.y - 1],
				             [newCell.x - 1, newCell.y - 1],
				             [newCell.x - 1, newCell.y]]
				for n in neighbors:
					if self.cellList.findCell(n[0], n[1]) is not None:  # add neighbor as parent if exists
						parents.append(self.cellList.findCell(n[0], n[1]))
					# if len(parents)==3: #this *might* improve efficiency, but only a little
					# break
				# self.g.note(str(newCell.x)+','+str(newCell.y)+' parents are: '+str(parents))
				newCell.inheritDNA(parents)
				cellsToAppend.append(newCell)
			# else: keep old cell info; do nothing
		for c in cellsToAppend:
			self.cellList.cells.append(c)

		# remove dead cells
		self.removeDeadCells()

	# draws colors onto custom color layer
	def drawColor(self):
		originL = self.g.getlayer()  # starting layer
		self.g.setlayer(self.colorIndex)

		# clear the layer
		indexCheck = None
		try:
			indexCheck = self.g.getrect()[0]
		except Exception:  # catch IndexError getting swallowed
			logging.debug('skipping attempt to clear empty layer')

		if indexCheck is not None:
			logging.debug(join(map(str, self.g.getrect())))
			self.g.select(self.g.getrect())
			self.g.clear(0)
			self.g.select([])

		# show the colors of each cell
		for c in self.cellList.cells:
			self.g.setcell(c.x, c.y, c.getColor())
		self.g.setlayer(originL)  # set layer back to original layer

	# ========================== PRIVATE METHODS =======================================

	# NOTE: this method is depreciated and no longer used
	# removes genetic material from cell no longer in environment layer
	def removeDeadCells(self):
		originL = self.g.getlayer()  # starting layer
		newPattern = self.g.getcells(self.g.getrect())
		# self.g.note('newPattern='+str(newPattern))
		self.g.setlayer(self.colorIndex)  # switch to color layer
		cellsToKill = list()  # must keep this list to do at end or loops get fudged
		for oldCell in self.cellList.cells:
			for newCellIndex in range(len(newPattern) / 2):
				xi = newPattern[newCellIndex * 2]  # newCell location
				yi = newPattern[newCellIndex * 2 + 1]
				if oldCell.x == xi and oldCell.y == yi:
					# self.g.note('cell at '+str(xi)+','+str(yi)+' found.')
					break  # cell found in new pattern; move on
			else:  # if cell not found in new pattern; cell has died.
				# self.g.note('cell at '+str(oldCell.x)+','+str(oldCell.y)+' not found.')
				self.g.setcell(oldCell.x, oldCell.y, 0)
				cellsToKill.append([oldCell.x, oldCell.y])
		for c in cellsToKill:
			self.cellList.killCellAt(c[0], c[1])
		self.g.setlayer(originL)

