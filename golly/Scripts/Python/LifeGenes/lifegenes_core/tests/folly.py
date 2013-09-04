# this module defines a fake golly-like environment. This is useful for testing and debugging.
# to use simply put 'from LifeGenes.lifegenes_core.tests.folly import folly as g' in place of 'import golly as g'

class follyInstance:
	def __init__(self):
		# change these values to test different start-cases:
		self.currentLayer = 0
		self.curLayerEmpty= False
		self.layerColors  = [[0,255]]
		self.layerNames   = ['first!']	#i'm not sure what this actually looks like in golly
		self.layerRules   = ['life']
		self.nLayers      = 1
		self.maxLayers    = 10
		
	# golly behavior:
	#Add a new, empty layer immediately after the current layer and return the new layer's index, 
	# an integer from 0 to numlayers() - 1. 
	# The new layer becomes the current layer and inherits most of the previous layer's settings, 
	# including its algorithm, rule, scale, location, cursor mode, etc. 
	# The step exponent is set to 0, there is no selection, no origin offset, and the layer's initial name is "untitled".
	def addlayer(self):
		if self.nLayers+1 >= self.maxLayers:
			print 'ERR: attempt to add layer above maxlayers'
		else:
			self.layerNames.append('untitled')
			self.layerColors.append(self.layerColors[self.getlayer()])
			self.layerRules.append(self.layerRules[self.getlayer()])
			self.currentLayer = self.nLayers
			self.nLayers+=1
			return self.currentLayer
			
	def clear(self):
		return

	# golly behavior:
	# Return True if the universe is empty or False if there is at least one live cell.
	# This is much more efficient than testing getpop() == "0".
	def empty(self):
		return self.curLayerEmpty
		
	def exit(self,msg):
		print 'requested exit via exit() method with message:'
		print msg
		exit()
	
	def getcell(self,x,y):
		return 1
	
	# goly behavior:
	#Return any live cells in the specified rectangle as a cell list. 
	# The given list can be empty (in which case the cell list is empty) 
	# or it must represent a valid rectangle of the form [x,y,width,height].
	def getcells(self,boundingRect):
	#	# return a couple of cells:
	#	return [0  ,1,\
	#	        1  ,1,\
	#			1  ,0,\
	#			100,121]
				
		# return many cells:
		cellList = list()
		for cellN in range(1000):
			cellList.append(cellN)   #x loc
			cellList.append(0)       #y loc
		return cellList
			
			
		
	# matches golly behavior: 
	# Return the index of the current layer, an integer from 0 to numlayers() - 1.
	def getlayer(self):
		return self.currentLayer
		
	def getname(self,index):
		return self.layerNames[index]
	
	#golly behavior:
	# Return the current pattern's bounding box as a list.
	# If there is no pattern then the list is empty ([]), 
	# otherwise the list is of the form [x,y,width,height].
	def getrect(self):
		return [0,0,101,121]
		
	def maxlayers(self):
		return self.maxlayers;
	
	def numlayers(self):
		return self.nLayers
		
	def select(self,list):
		return
		
	def setcell(self,x,y,val):
		#yeah... whatever...
		return
		
	def setcolors(self,colors):
		self.layerColors[self.getlayer()] = colors

	def setlayer(self,layern):
		self.currentlayer = layern
	
	def setname(self,name):
		self.layerNames[self.getlayer()] = name
		
	def setrule(self,rule):
		self.layerRules[self.getlayer()] = rule
	
	def show(self,msg):
		print msg
		return
		
	def step(self):
		return
		
	def update(self):
		return

folly = follyInstance()