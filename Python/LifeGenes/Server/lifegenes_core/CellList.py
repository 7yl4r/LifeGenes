# lifeGenes cell list object
import pickle
import logging

from LifeGenes.Server.lifegenes_core import Cell

# a generalized list of cells
# FIELDS:
# cells - a list of cell objects
# PUBLIC METHODS:
# findCell - locate a cell by x,y coords
# killCellAt - remove a cell by x,y coords
# save - save cellList to file
# load - load cellList from file
#	set - make this list into a copy of given list
class CellList:
	def __init__(self, pattern):
		self.cells = list()
		# add cell object to list for each pair in pattern
		for cellIndex in range(len(pattern) / 2):
			self.cells.append(Cell.Cell(pattern[cellIndex * 2], pattern[cellIndex * 2 + 1]))
			cellIndex += 1

	def setCell(self, x, y, dna=None, cell=None):
		if cell is not None:
			self.killCellAt(x, y)  # remove old cell if exists
			self.cells.append(cell)  # add new cell
		elif dna is not None:
			self.KillCellAt(x, y)
			self.cells.append(cell(x, y, dna))
		else:
			raise ValueError("setCell requires dna or cell object be specified")

	def getCells(self):
		return CellList

	def findCell(self, x, y):
		# retuns cell object with given coords
		for c in self.cells:
			if c.x is x and c.y is y:
				return c
		#implied else
		return None

	def killCellAt(self, x, y):
		# deletes cell at given loc. Returns True for sucessful deletion, False for cell not found.
		for c in self.cells:
			if c.x == x and c.y == y:
				self.cells.remove(c)
				return True
		else:
			return False

	def save(self, fname):
		# saves the cell list to the given file name
		with open(fname, 'wb') as f:
			pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

	def load(self, fname):
		# loads the cell list from the given file name
		with open(fname, 'rb') as f:
			newList = pickle.load(f)
		try:
			newList.cells[0]
		except AttributeError:
			logging.error('loaded list seems to have no cells!')
			raise
		#implied else
		self.set(newList)
		logging.info(str(len(self.cells)) + ' cells loaded from file')

	#except: logging.error('cellList load appears to have failed. dir(cellList)='+str(dir(self)))

	def set(self, cList):
		# makes the cell list a copy of the given cellList
		self.cells = cList.cells
