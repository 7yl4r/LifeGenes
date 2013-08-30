# this set of unit tests is meant to be run from a command line to test aspects of the LifeGenes outside of golly.

from ..cell import cell, DNA_MINLEN, DNA_MAXLEN, MAX_COLOR, MIN_COLOR
from random import randrange
from time import time
from math import floor

# test the cell class
def simpleCellTest():
	x = randrange(-10000,10000)
	y = randrange(-10000,10000)
	c = cell(x,y)
	
	assert c.x == x, 'cell x location incorrect'
	assert c.y == y, 'cell y location incorrect'
	
	assert len(c.DNA) >= DNA_MINLEN, 'cell DNA too small'
	assert len(c.DNA) <= DNA_MAXLEN, 'cell DNA too large'
	
	# TODO: check for other value errors
	
	return c

# prints out simple diagnostic info for cell to show traits
def simpleCellDiagnostic(cell):
	print ' === cell diagnostic ==='
	print '    DNA: '+str(cell.DNA)
	print ' DNAlen: '+str(len(cell.DNA))
	print '    loc: ('+str(cell.x)+','+str(cell.y)+')'
	print '  color: '+str(cell.getColor())
	print ' ======================='
	
# generates n random cells and checks bell curve of color values histogram
def checkColorHistogram(n):
	print ' === checking color histogram === '
	nBins = 5
	binSize = floor((MAX_COLOR - MIN_COLOR)/nBins)
	histogram = [0]*nBins
	binEdge = [0]*(nBins+1)
	binEdge[0] = MIN_COLOR
	for i in range(1,nBins+1):
		binEdge[i] = binEdge[i-1] + binSize
	binEdge[nBins] = MAX_COLOR
	print 'binEdges='+str(binEdge)
	for i in range(n):
		c = cell(1,1)
		v = c.getColor();
		for i in range(nBins):
			if v <= binEdge[i+1]:
				histogram[i]+=1
				break
		
	print 'colorVal histogram: '+str(histogram)
	for i in range(1,nBins):
		if i < nBins/2.0:
			assert histogram[i]>=histogram[i-1], 'color values biased low'
		elif i > nBins/2.0:
			assert histogram[i]<=histogram[i-1], 'color values biased high'
		else: print str(i)+'=?='+str(nBins/2)
		assert histogram[i] > 0, 'color values not spread well enough'
	print ' ================================ '

	# prints out simple diagnostic info for cell to show traits
def simpleCellDiagnostic(cell):
	print ' === cell diagnostic ==='
	print '    DNA: '+str(cell.DNA)
	print ' DNAlen: '+str(len(cell.DNA))
	print '    loc: ('+str(cell.x)+','+str(cell.y)+')'
	print '  color: '+str(cell.getColor())
	print ' ======================='
	
# generates n random cells, checks for flat direction histogram 
# TODO: also check for bell-curve of magnitudes
def checkMovementHistogram(n):
	print ' === checking direction histogram === '
	#counts for each case:
	up = 0
	down = 0 
	left = 0
	right = 0
	none = 0 
	thresh = n/10 # ~10% variance between values allowed
	def dummyStateGetter(x,y):
		return 1
	for i in range(n):
		c = cell(1,1)
		[v,mag] = c.getMovement(dummyStateGetter);
		if v =='up': up+=1
		elif v=='down': down+=1
		elif v=='left': left+=1
		elif v=='right': right+=1
		elif v==None: none+=1
		else: assert False, 'unknown direction value:'+v
	print 'up\tdown\tleft\tright\tnone'
	print str(up)+'\t'+str(down)+'\t'+str(left)+'\t'+str(right)+'\t'+str(none)
	
	assert up+down+left+right+none == n, 'incorrect count!'
	r = max([up,down,left,right])-min([up,down,left,right])
	assert r<thresh,\
		'direction spread is not equal. bias='+str(r/n)
	#TODO: check for magnitude spread (i.e. the number of 'none's)
	print ' ==================================== '

# runs a given test n times and makes a simple display
def timedRuns(test,n):	#TODO: add args parameter
	t = list()
	sTime = time()
	for i in range(n):
		startTime = time()
		test()
		endTime = time()
		t.append(endTime-startTime)
	eTime = time()
	scale = 40/max(t)
	for ttt in t:
		print '|'*int(round(ttt*scale))
	print "tests complete. est avg time to complete:"+str((eTime-sTime)/n)+'s'

#Main:
n = 100 #number of cells in histogram tests
#timedRuns(cell,[123,345],100)
simpleCellDiagnostic(simpleCellTest())
checkColorHistogram(100)
checkMovementHistogram(100)

#endMain

