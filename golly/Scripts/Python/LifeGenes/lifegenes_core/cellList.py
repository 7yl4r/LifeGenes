# lifeGenes cell list object

from .cell import cell
import pickle
import logging

# a generalized list of cells
# FIELDS:
#	cells - a list of cell objects
# PUBLIC METHODS:
#	findCell - locate a cell by x,y coords
#	killCellAt - remove a cell by x,y coords
#	save - save cellList to file
#	load - load cellList from file
#	set - make this list into a copy of given list
class cellList:
	def __init__(self,pattern):
		self.cells = list()
		# add cell object to list for each pair in pattern
		for cellIndex in range(len(pattern)/2):
			self.cells.append(cell(pattern[cellIndex*2],pattern[cellIndex*2+1]))
			cellIndex+=1

	# retuns cell object with given coords
	def findCell(self,x,y):
		for c in self.cells:
			if c.x==x and c.y==y:
				return c
		#implied else
		return None

	# deletes cell at given loc
	def killCellAt(self,x,y):
		for c in self.cells:
			if c.x==x and c.y==y:
				self.cells.remove(c)
				
	# saves the cell list to the given file name
	def save(self,fname):
		with open(fname,'wb') as f:
			pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

	# loads the cell list from the given file name
	def load(self,fname):
		with open(fname,'rb') as f:
			newList = pickle.load(f)
		try:
			check = newList.cells[0]
		except AttributeError:
			logging.error('loaded list seems to have no cells!')
			raise 
		#implied else
		self.set(newList)
		logging.info(str(len(self.cells))+' cells loaded from file')
		#except: logging.error('cellList load appears to have failed. dir(cellList)='+str(dir(self)))
			
	# makes the cell list a copy of the given cellList
	def set(self,cList):
		self.cells = cList.cells