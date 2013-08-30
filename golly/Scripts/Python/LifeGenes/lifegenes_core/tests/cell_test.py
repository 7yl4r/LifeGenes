# this set of unit tests is meant to be run from a command line to test aspects of the LifeGenes outside of golly.

from ..cell import cell, DNA_MINLEN, DNA_MAXLEN
from random import randrange
from time import time

# test the cell class
def simpleCellTest():
	x = randrange(10000)
	y = randrange(10000)
	print '=== cell('+str(x)+','+str(y)+') result ==='
	c = cell(x,y)
	
	assert cell.X == x, 'cell x location incorrect'
	assert cell.Y == y, 'cell y location incorrect'
	
	assert len(cell.DNA) >= DNA_MINLEN, 'cell DNA too small'
	assert len(cell.DNA) <= DNA_MAXLEN, 'cell DNA too large'
	
	cellDiagnostic(c)
	# TODO: check for any value errors (but I don't see any and that's good enough for me right now)

# prints out simple diagnostic info for cell to show traits
def simpleCellDiagnostic(cell):
	print '    DNA: '+str(cell.DNA)
	print ' DNAlen: '+str(len(cell.DNA))
	print '    loc: ('+str(cell.x)+','+str(cell.y)+')'
	print '  color: '+str(cell.getColor())
	
# generates random cells and outputs histogram data of color values
def cellColorHistogram():
	print [0,0,0,0,0,0]

# runs a given test n times and makes a simple display
def timedRuns(test,n):
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
n = 10	#number of runs
timedRuns(cell(123,345),n)
#endMain

