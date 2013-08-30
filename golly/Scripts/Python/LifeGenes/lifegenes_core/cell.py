# LifeGenes cell genome definition 

from random import randrange

import logging

BASES = ['A','B','C','D']	#DNA Base Pairs (BP)
DNA_MINLEN = 10		#min base pairs in a genome 
DNA_MAXLEN = 1000		#max base pairs in a genome

#strings which decrease value in neural network connection
ANN_DN_CODONS = [['ABDD', 'CAAB', 'ABAD', 'CBBC'],\
['DDDA', 'DBAB', 'AADD', 'ABAB'],\
['CDDC', 'DCDD', 'ACBD', 'BADC'],\
['CBBB', 'BBDA', 'AACD', 'DDCA'],\
['ADDA', 'CBDD', 'DBAA', 'DBAC'],\
['CBAB', 'ACAD', 'ABCD', 'CBCB'],\
['BBAC', 'DCCD', 'BCAB', 'BACC'],\
['DDCC', 'BDCC', 'DADA', 'BADA'],\
['DDDD', 'BBAB', 'BDDA', 'CDAD'],\
['DDBD', 'BDBA', 'DCDA', 'BBAA'],\
['BDAA', 'DBBC', 'BADD', 'BBDD'],\
['ABAA', 'DDBC', 'ADBB', 'CCDA'],\
['BCDC', 'CACA', 'CAAC', 'CBAD'],\
['ADDC', 'DBDB', 'CCAA', 'CCBD'],\
['BACD', 'AABC', 'DACD', 'BCBB'],\
['ABDA', 'ACCC', 'BBDB', 'DDCD'],\
['ADBD', 'CDDB', 'DDBA', 'DCBB'],\
['CABC', 'CCDD', 'ACCD', 'ACBC'],\
['CCCB', 'CACB', 'ACCA', 'DDCB']]

#strings which increase value in neural network connection
ANN_UP_CODONS = [['CDCB', 'BABB', 'ACAC', 'ABCB'],\
['CCDB', 'CDAB', 'DDDB', 'DACC'],\
['BBCC', 'ACDB', 'CADB', 'BDCB'],\
['DBBA', 'CBAA', 'AACC', 'BCBA'],\
['ACDA', 'BAAB', 'DADD', 'DDAD'],\
['BDCD', 'AACA', 'AAAC', 'BBCB'],\
['CAAA', 'DBDD', 'BCAC', 'AAAB'],\
['DCDC', 'BCCD', 'DACA', 'BDBD'],\
['CCBA', 'ADBC', 'BBCA', 'CBCC'],\
['BCDD', 'BACB', 'DAAC', 'DCBA'],\
['CCDC', 'DADB', 'CACC', 'BDDB'],\
['BDCA', 'ADAB', 'BDAB', 'BBBB'],\
['DCDB', 'DACB', 'ADCA', 'AABB'],\
['DCAC', 'ABAC', 'ABBC', 'BDAC'],\
['DABA', 'ACBA', 'BCCA', 'CBCD'],\
['CCAD', 'CABB', 'DDAA', 'ABBB'],\
['CBDB', 'BABC', 'BCCB', 'ADDB'],\
['ADAC', 'BBBD', 'DBBD', 'DDAB'],\
['DAAB', 'ADBA', 'AAAD', 'CBBA']]

DARK_CODON  = 'A'
LIGHT_CODON = 'B'

# TODO: genetically calculated values need only be calculated once and then stored for future reference. This will greatly improve efficiency.

class cell:
	def __init__(self,X,Y):	#TODO: add DNA= at end
		self.randomizeDNA()
		self.x = X
		self.y = Y

	# return color value 1-255 generated from first 10 BP of DNA
	def getColor(self):	
		color = 110	#starting color in middle of range
		maxColor = 220
		minColor = 1
		dc    = 1 	#delta color; amount of change when codon is detected
		return self.getGeneticValue(color,maxColor,minColor,dc,DARK_CODON,LIGHT_CODON)

	# generates a random DNA string using bases defined in BASES
	def randomizeDNA(self):
		global BASES
		DNAlen = randrange(DNA_MINLEN,DNA_MAXLEN)
		self.DNA = list()
		for i in range(DNAlen):
			self.DNA.append(BASES[randrange(0,len(BASES)-1)])

	# generates DNA string from given parent cells
	def inheritDNA(self,parents):
		if len(parents) != 3:
			print 'ERR: cell needs 3 parents!'
			self.DNA = [[BASES[0]*BASES[1]]*DNA_MINLEN]
			return
		genes = [parents[0].DNA,parents[1].DNA,parents[2].DNA] #total genetic material to choose from
		#implied else
		DNAlen = int((len(genes[0])+len(genes[1])+len(genes[2]))/3)
		for i in range(DNAlen): #add random DNA if one parent's genome is too short
			for p in range(0,2):
				if i > len(genes[p])-1:
					genes[p].append(BASES[randrange(0,len(BASES)-1)])
		cellDNA = list()
		for i in range(DNAlen): #figure out child cell's DNA
			inheritFrom = randrange(0,2)
			cellDNA.append(genes[inheritFrom][i])
		self.DNA = cellDNA

	# get visual information about the cells nearby
	def getVisualInput(self,stateGetter):
		#setup visual input 
		return [stateGetter(self.x-1,self.y-2),\
		        stateGetter(self.x  ,self.y-2),\
		        stateGetter(self.x+1,self.y-2),\
		        stateGetter(self.x-2,self.y-1),\
		        stateGetter(self.x-1,self.y-1),\
		        stateGetter(self.x  ,self.y-1),\
		        stateGetter(self.x+1,self.y-1),\
		        stateGetter(self.x+2,self.y-1),\
		        stateGetter(self.x-2,self.y  ),\
		        stateGetter(self.x-1,self.y  ),\
		        stateGetter(self.x+1,self.y  ),\
		        stateGetter(self.x+2,self.y  ),\
		        stateGetter(self.x-2,self.y+1),\
		        stateGetter(self.x-1,self.y+1),\
		        stateGetter(self.x  ,self.y+1),\
		        stateGetter(self.x+1,self.y+1),\
		        stateGetter(self.x+2,self.y+1),\
		        stateGetter(self.x-1,self.y+2),\
		        stateGetter(self.x  ,self.y+2),\
		        stateGetter(self.x+1,self.y+2)]

	# returns a numeric value determined from DNA; codons MUST be same length TODO: fix this
	def getGeneticValue(self,startVal,maxVal,minVal,delta,upCodon,downCodon):
		genes = ''.join(self.DNA)	#convert from DNA char array to string (to use slicing)
		v = startVal
		pass # logging.debug('looking for strings '+str(downCodon)+' and '+str(upCodon))
		L = len(downCodon) # == len(upCodon)
		for i in range( len(self.DNA)-L ):
			s_dn = genes[i:(i+len(downCodon))]
			s_up = genes[i:(i+len(upCodon))]
			pass # logging.debug('checking strings '+str(s_dn)+' and '+str(s_up))
			if s_dn == downCodon:
				v-=delta
			if s_up == upCodon:
				v+=delta
		if v > maxVal : v = maxVal
		if v < minVal : v = minVal
		return v

	# gets the weights for ANN connections (see wiki for more info)
	def getNNweights(self):
		startV = 0	#starting color in middle of range
		maxV = 1000
		minV = -1000
		delt = 1 	# amount of change when codon is detected
		num_outs = 4
		num_ins  = len(ANN_UP_CODONS)
		pass #logging.debug('weights should be '+str(num_ins)+'x'+str(num_outs))
		weights = [ [startV]*num_outs ]*num_ins	# inputs x outputs list
		pass # logging.debug('weights is '+str(len(weights))+' items in total')
		pass # logging.debug(str(num_ins)+'x'+str(num_outs)+' weights list created:\n'+str(weights))
		for i in range(num_ins):
			for o in range(num_outs):
				pass # logging.debug('looking for codon['+str(i)+']['+str(o)+']')
				weights[i][o] = self.getGeneticValue(startV,maxV,minV,delt,ANN_UP_CODONS[i][o],ANN_DN_CODONS[i][o])
		return weights

	# moves the cell as determined by DNA-encoded neural network (see wiki for more info)
	def move(self,stateSetter,stateGetter):
		num_ins  = len(ANN_UP_CODONS)
		v = self.getVisualInput(stateGetter)
		w = self.getNNweights()
		output = [0]*4
		for o in range(4):
			for i in range(num_ins):
				output[o] = v[i]*w[i][o]
		dirVal = max(output) #cell moves in direction of greatest output
		if dirVal < 1: #simple threshold
			return
		else:
			direction = output.index(dirVal)
			if direction == 0:
				d = 'up'
			elif direction ==1:
				d = 'right'
			elif direction == 2:
				d = 'down'
			elif direction == 3:
				d = 'left'
			else: 
				logging.error('direction number "'+str(direction)+'" not recognized')
				return
			self.moveOne(d,stateSetter,stateGetter)
		
	# allows the cell to move one space in given direction
	def moveOne(self,direction,stateSetter,stateGetter):
		# find new cell object attributes
		if direction == 'up':
			newX = self.x
			newY = self.y - 1
		elif direction == 'down':
			newX = self.x
			newY = self.y + 1
		elif direction == 'left':
			newX = self.x - 1
			newY = self.y
		elif direction == 'right':
			newX = self.x + 1
			newY = self.y
		else:
			logging.warn('direction "'+str(direction)+'" not recognized by cell')
			return
		#check for occupied space
		if stateGetter(newX,newY) == 1:	# another cell is already there	
			pass # TODO: try to push cell?
		else: # space is clear; move into it
			stateSetter(self.x,self.y,0)	# set state=0 of old location in golly
			self.x = newX
			self.y = newY
			stateSetter(self.x,self.y,1)	# set state=1 of new location in golly

	# allows the cell to move in directions up,right,down,left a given distance
	def moveNum(self,direction,distance,stateSetter,stateGetter):
		if distance == 0:
			logging.warn('cell movement distance == 0')
			return
		for x in range(distance):
			self.moveOne(direction,stateSetter,stateGetter)




