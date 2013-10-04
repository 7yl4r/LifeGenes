# lifeGenes cell list object

from .cell import cell
import pickle

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
			self = pickle.load(f)