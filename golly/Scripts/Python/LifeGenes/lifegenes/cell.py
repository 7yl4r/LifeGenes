# LifeGenes cell genome definition 

from random import randrange

BASES = ['A','B','C','D']	#DNA Base Pairs (BP)
DNA_MINLEN = 10			#min base pairs in a genome 
DNA_MAXLEN = 100		#max base pairs in a genome

class cell:
	def __init__(self,X,Y):	#TODO: add DNA= at end
		self.randomizeDNA()
		self.x = X
		self.y = Y

	# return color value 1-255 generated from first 10 BP of DNA
	def getColor(self):	
		color = 128	#starting color in middle of range
		maxColor = 200
		minColor = 1
		dc    = 15 	#delta color; amount of change when codon is detected
		lightCodon = 'AB' #string which decreases color value
		darkCodon  = 'BD' #string which increases color value
		for i in range(len(self.DNA)-1):
			if (str(self.DNA[i])+str(self.DNA[i+1])) == darkCodon:
				color+=dc
			if (str(self.DNA[i])+str(self.DNA[i+1])) == lightCodon:
				color-=dc
		if color > maxColor : color = maxColor
		if color < minColor : color = minColor
		return color

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


