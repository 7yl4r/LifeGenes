# this script allows for testing of lifegenes functionality from the python command line rather than the golly environment. Currently this is accomplished by using a mock-golly module called folly (short for fake-golly). The folly module does not actually perform all functions as golly would, it just looks like it for testing.

try:	# print a nice message if someone tries to open this script from w/in golly
	import golly as g
	g.exit('this script is for dev test only and cannot be run from within golly, check out the scripts in the "LifeGenes" folder instead')
except:
	from LifeGenes.lifegenes_core.tests.folly import folly as g
	
from LifeGenes.lifegenes_core.setupLog import setupLog
from LifeGenes.lifegenes_core.tests.optimization_tools import timedRuns
from os import system
	
import logging
setupLog('__test_LifeGenes.log')

def wait():
	try:
		system('pause')  #windows, doesn't require enter
	except:
		system('read -p "Press any key to continue"') #linux

		
# MAIN
logging.info('script started')
nruns = 10

print 'testing environment...'
from LifeGenes.lifegenes_core.environment import environment as lifegenes_environment
lg_envmt = lifegenes_environment()
testNames = list()
testTimes = list()

g.getcellsconfig = 'const growing'
g.generation = 0
print 'testing drawColor for constantly growing cell list'
testNames.append('drawColor')
testTimes.append( timedRuns(lg_envmt.drawColor,nruns,lambda:[g.step(),lg_envmt.update()]) )
#wait()

g.getcellsconfig = 'const growing'
g.generation = 0 
print 'testing update() for constantly growing cell list'
testNames.append('update()')
testTimes.append( timedRuns(lg_envmt.update,nruns,g.step) )
#wait()

g.getcellsconfig = 'const growing'
g.generation = 0 
print 'testing cellMotions() for constantly growing cell list'
testNames.append('cellMotions()')
testTimes.append( timedRuns(lg_envmt.cellMotions,nruns,lambda:[g.step(),lg_envmt.update()]) )
#wait()

slowest = max(testTimes)
print '\n'+testNames[testTimes.index(slowest)]+' had worst performance of '+str(slowest)+'s'
