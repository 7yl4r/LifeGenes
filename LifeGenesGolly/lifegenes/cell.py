# LifeGenes cell genome definition 

from random import randrange

BASES = ['A','B','C','D']	#DNA Base Pairs (BP)
DNA_MINLEN = 10			#min base pairs in a genome 
DNA_MAXLEN = 100		#max base pairs in a genome

class cell:
	def __init__(self,X,Y):
		self.randomizeDNA()
		self.x = X
		self.y = Y

	# return color value 0-255 generated from first 10 BP of DNA
	def getColor(self):	
		color = 128
		for i in range(len(self.DNA)-1):
			if (str(self.DNA[i])+str(self.DNA[i+1])) == 'AB':
				color+=50
			if (str(self.DNA[i])+str(self.DNA[i+1])) == 'BA':
				color-=50
		if color > 255 : color = 255
		if color < 0   : color = 0
		return color

	# generates a random DNA string using bases defined in BASES
	def randomizeDNA(self):
		global BASES
		DNAlen = randrange(DNA_MINLEN,DNA_MAXLEN)
		self.DNA = list()
		for i in range(DNAlen):
			self.DNA.append(BASES[randrange(0,len(BASES)-1)])

