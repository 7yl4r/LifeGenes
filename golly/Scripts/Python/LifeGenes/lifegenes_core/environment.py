try: import golly
except: 
	print 'could not load golly, using folly instead'
	from tests.folly import folly as golly
import logging

from LifeGenes.lifegenes_core.cellList import cellList	#import LifeGenes cell definition
from LifeGenes.lifegenes_core.cell     import cell as LGcell

from LifeGenes.lifegenes_core.__util.appdirs import user_data_dir
from os.path import join
from os import makedirs


class environment:
	# prepares the needed data structures
	def __init__(self, g=golly):
		saveDir = user_data_dir('LifeGenes','7yl4r-ware')
		try:
			makedirs(saveDir)
		except OSError:
			pass # probably the dir already exists... 
		self.CELL_LIST_FILENAME = join(saveDir,'lifeGenes_cellList.pk')

		self.originL = g.getlayer() #starting layer
		if g.empty(): g.exit("The pattern is empty.")
		# check for existing geneticColor layer
		currindex = 0
		self.colorIndex = -1
		while currindex < g.numlayers():
			if g.getname(currindex) == 'geneticColor':
				# continue from where we left off
				self.colorIndex = currindex
				g.show('geneticColor layer already exists!')
				 # read cell genes from a file and make self.cellList
				self.cellList = cellList([0,0])
				self.cellList.load(self.CELL_LIST_FILENAME)
				break
			else: currindex+=1
		if self.colorIndex == -1:	#if we didn't find existing colorLayer
			#set up new colorLayer
			startpatt = g.getcells(g.getrect()) # get starting pattern array [x1,y1,x2,y2,...]

			self.cellList = cellList(startpatt)

			logging.info(str(len(startpatt)/2)+' cells found, '+str(len(self.cellList.cells))+' trait objects created.')


			# add color layer
			if g.numlayers() + 1 > g.maxlayers():
				g.exit("You need to delete a layer.")

			self.colorIndex = g.addlayer()     # create layer for colors
			g.setname('geneticColor')
			g.setrule('constant')	#use custom constant rule
			g.setcolors([0,255,0, 0,0,255]) #live states vary from green to blue
		g.setlayer(self.originL) # set layer back to original layer
		
	# close down the environment
	def teardown(self,g=golly):
		g.setlayer(self.originL)	#ensure we are on the right layer
		self.update(g)		#ensure there are no half-built arrays
		self.drawColor(g)	#one last draw
		g.update()			#one last display update
		self.cellList.save(self.CELL_LIST_FILENAME)

	# cellMotions allows cells to move around in their environment while no evolution takes place
	#     motion is based on values calculated from the cell's neural network
	#     layer must be on the original layer, NOT the color layer.
	def cellMotions(self, g=golly):
		for cell in self.cellList.cells:
			cell.move(g.setcell,g.getcell)
			
	# update the environment to match the changes in the given cell environment g
	def update(self, g=golly):
		newPattern = g.getcells(g.getrect())
		# generate DNA for new cells
		newList = list() #save this & add at end to not muck up the list
		for newCellIndex in range(len(newPattern)/2): #for all cells in newCellIndex
			#add the cell if it does not already exist
			xi = newPattern[newCellIndex*2] #newCell location
			yi = newPattern[newCellIndex*2+1]
			existingCell = self.cellList.findCell(xi,yi)
			if existingCell==None:
				parents = list()
				newCell = LGcell(xi,yi)
				neighbors = [[newCell.x-1,newCell.y+1],\
						 [newCell.x  ,newCell.y+1],\
						 [newCell.x+1,newCell.y+1],\
						 [newCell.x+1,newCell.y  ],\
						 [newCell.x+1,newCell.y-1],\
						 [newCell.x  ,newCell.y-1],\
						 [newCell.x-1,newCell.y-1],\
						 [newCell.x-1,newCell.y  ]]
				for n in neighbors:
					if self.cellList.findCell(n[0],n[1])!=None: #add neighbor as parent if exists
						parents.append(self.cellList.findCell(n[0],n[1]))
					#if len(parents)==3: #this *might* improve efficiency, but only a little
					#	break
				#g.note(str(newCell.x)+','+str(newCell.y)+' parents are: '+str(parents))
				newCell.inheritDNA(parents)
				newList.append(newCell)
			else: #keep old cell info;
				newList.append(existingCell)
		self.cellList.cells = newList
			
	#uses g.update() and fixes self.cellList to match
	# depreciated version kept around (temporarily) for testing
	def update_depreciated(self, g=golly):
		#g.autoupdate(True)#while debugging
		newPattern = g.getcells(g.getrect())
		# generate DNA for new cells
		cellsToAppend = list() #save this & add at end to not muck up the list
		for newCellIndex in range(len(newPattern)/2): #for all cells in newCellIndex
			#add the cell if it does not already exist
			xi = newPattern[newCellIndex*2] #newCell location
			yi = newPattern[newCellIndex*2+1]
			if self.cellList.findCell(xi,yi)==None:
				parents = list()
				newCell = LGcell(xi,yi)
				neighbors = [[newCell.x-1,newCell.y+1],\
						 [newCell.x  ,newCell.y+1],\
						 [newCell.x+1,newCell.y+1],\
						 [newCell.x+1,newCell.y  ],\
						 [newCell.x+1,newCell.y-1],\
						 [newCell.x  ,newCell.y-1],\
						 [newCell.x-1,newCell.y-1],\
						 [newCell.x-1,newCell.y  ]]
				for n in neighbors:
					if self.cellList.findCell(n[0],n[1])!=None: #add neighbor as parent if exists
						parents.append(self.cellList.findCell(n[0],n[1]))
					#if len(parents)==3: #this *might* improve efficiency, but only a little
					#	break
				#g.note(str(newCell.x)+','+str(newCell.y)+' parents are: '+str(parents))
				newCell.inheritDNA(parents)
				cellsToAppend.append(newCell)
			#else: keep old cell info; do nothing
		for c in cellsToAppend:
			self.cellList.cells.append(c)

		# remove dead cells
		self.removeDeadCells()

	#draws colors onto custom color layer
	def drawColor(self, g=golly):
		originL = g.getlayer() #starting layer
		g.setlayer(self.colorIndex)

		# clear the layer
		try:
			g.select(g.getrect())
			g.clear(0)  
		except: 		
			logging.warn('cannot clear empty layer')
		g.select([])

		# show the colors of each cell
		for c in self.cellList.cells:
			g.setcell(c.x,c.y,c.getColor())
		g.setlayer(originL) # set layer back to original layer

# ========================== PRIVATE METHODS =======================================

	#NOTE: this method is depreciated and no longer used
	#removes genetic material from cell no longer in environment layer
	def removeDeadCells(self, g=golly):
		originL = g.getlayer() #starting layer
		newPattern = g.getcells(g.getrect())
		#g.note('newPattern='+str(newPattern))
		g.setlayer(self.colorIndex) #switch to color layer
		cellsToKill=list() #must keep this list to do at end or loops get fudged
		for oldCell in self.cellList.cells:
			for newCellIndex in range(len(newPattern)/2):
				xi = newPattern[newCellIndex*2] #newCell location
				yi = newPattern[newCellIndex*2+1]
				if oldCell.x==xi and oldCell.y==yi:
					#g.note('cell at '+str(xi)+','+str(yi)+' found.')
					break #cell found in new pattern; move on
			else: #if cell not found in new pattern; cell has died.
				#g.note('cell at '+str(oldCell.x)+','+str(oldCell.y)+' not found.')
				g.setcell(oldCell.x,oldCell.y,0)
				cellsToKill.append([oldCell.x,oldCell.y])
		for c in cellsToKill:
			self.cellList.killCellAt(c[0],c[1])
		g.setlayer(originL)

