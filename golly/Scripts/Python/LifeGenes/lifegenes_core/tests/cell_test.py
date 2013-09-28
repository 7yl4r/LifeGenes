# this set of unit tests is meant to be run from a command line to test aspects of the LifeGenes outside of golly.

from ..cell import cell,DNA_MINLEN,DNA_MAXLEN,MAX_COLOR,MIN_COLOR,NN_MIN,NN_MAX,BASES
from random import randrange
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
	
	for base in BASES:
		try: c.DNA.index(base)
		except: assert False, str(c.DNA)+'\nDNA string does not have each base'+str(BASES)
	
	# TODO: check for other value errors
	
	return c

# prints out simple diagnostic info for cell to show traits
def simpleCellDiagnostic(cell):
	print '\n === === === === cell diagnostic === === === ==='
	print '    DNA: '+str(cell.DNA)
	print ' DNAlen: '+str(len(cell.DNA))
	print '    loc: ('+str(cell.x)+','+str(cell.y)+')'
	print '  color: '+str(cell.getColor())
	print '...does that look about right to you?'
	print ' ================================================='
	
# checks for bell curve of color values in given cell list
def checkColorHistogram(cellList):
	print '\n === checking color histogram === '
	checkValueSpread(cellList,5,MIN_COLOR,MAX_COLOR,'getColor()')
	print ' ================================ '
	
# checks for bell-curve distribution of NN weights in given cell list
def checkNNweights(cellList):
	print '\n === checking NN histogram === '
	checkValueSpread(cellList,5,NN_MIN,NN_MAX,'getNNweights()[0][0]')
	print ' ================================ '
	
def checkValueSpread(cellList,nBins,min,max,cellValueGetterCallString):
	binSize = floor((max - min)/nBins)
	histogram = [0]*nBins
	binEdge = [0]*(nBins+1)
	binEdge[0] = min
	for i in range(1,nBins+1):
		binEdge[i] = binEdge[i-1] + binSize
	binEdge[nBins] = max
	print 'binEdges='+str(binEdge)
	for c in cellList:
		v = eval('c.'+cellValueGetterCallString);
		for i in range(nBins):
			if v <= binEdge[i+1]:
				histogram[i]+=1
				break
	print 'histogram: '+str(histogram)
	for i in range(1,nBins):
		if i < nBins/2.0:
			assert histogram[i]>=histogram[i-1], 'values biased low'
		elif i > nBins/2.0:
			assert histogram[i]<=histogram[i-1], 'values biased high'
		else: print str(i)+'=?='+str(nBins/2)
		assert histogram[i] > 0, 'values not spread well enough'
	print '...these are not the problems you are looking for. move along.'
	
# checks for flat direction histogram  in given cellList
# TODO: also check for bell-curve of magnitudes
def checkMovementHistogram(cellList):
	print '\n === checking direction histogram === '
	#counts for each case:
	up = 0
	down = 0 
	left = 0
	right = 0
	none = 0 
	thresh = n/100*10 # ~10% deviation from balance is allowed
	def dummyStateGetter(x,y):
		return 1
	for c in cellList:
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
		'direction spread is not equal. bias='+str(float(r)/float(n))
	#TODO: check for magnitude spread (i.e. the number of 'none's)
	print "...s'good"
	print ' ==================================== '
	
#Main:
n = 5000 #number of cells in histogram tests
cellList = list()
for i in range(n):
	cellList.append(cell(1,1))
#timedRuns(cell,[123,345],100)
simpleCellDiagnostic(simpleCellTest())
checkColorHistogram(cellList)
checkNNweights(cellList)
checkMovementHistogram(cellList)

#endMain

