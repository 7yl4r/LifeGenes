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
nruns = 100

print 'testing environment...'
from LifeGenes.lifegenes_core.environment import environment as lifegenes_environment
lg_envmt = lifegenes_environment()
print 'testing drawColor'
timedRuns(lg_envmt.drawColor,nruns)
wait()
print 'testing update()'
timedRuns(lg_envmt.update,nruns)
wait()
print 'testing cellMotions()'
timedRuns(lg_envmt.cellMotions,nruns)

wait()


