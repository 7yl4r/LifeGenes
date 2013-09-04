# this script allows for testing of lifegenes functionality from the python command line rather than the golly environment. Currently this is accomplished by using a mock-golly module called folly (short for fake-golly). The folly module does not actually perform all functions as golly would, it just looks like it for testing.

from LifeGenes.lifegenes_core.environment import environment as lifegenes_environment
from LifeGenes.lifegenes_core.setupLog import setupLog

try:	# print a nice message if someone tries to open this script from w/in golly
	import golly as g
	g.exit('this script is for dev test only and cannot be run from within golly, check out the scripts in the "LifeGenes" folder instead')
except:
	from LifeGenes.lifegenes_core.tests.folly import folly as g
	
import logging
setupLog('__test_LifeGenes.log')

class run():
	def __init__(self):
		logging.info('script started')
		lg_envmt = lifegenes_environment()
		lg_envmt.drawColor()
		logging.info('setup complete; beginning evolution cycles')
		try:
			while(True):	#until stopped by golly
				g.step()
				#g.update()
				lg_envmt.update()
				lg_envmt.drawColor()
				g.update()
		finally:
				logging.info('cycling halted from external source (probably golly)')
				#TODO: save cell genomes to file

#MAIN
run()
