# this script creates a cell genome for each cell in the current layer, 
# then displays the genetic 'color' of each cell.
# The script then begins cycling between rounds of cell movement and cell evolution.
# Please see the [LifeGenes project for genetic cellular automaton](https://github.com/7yl4r/LifeGenes) for more info.

import golly as g

from LifeGenes.lifegenes_core.environment import environment as lifegenes_environment

# import time	#for delays when debugging

from LifeGenes.lifegenes_core.setupLog import setupLog

import logging
setupLog('movingCells.log')


class run():
	def __init__(self):
		logging.info('script started')
		lg_envmt = lifegenes_environment()
		lg_envmt.drawColor()
		logging.info('setup complete; beginning evolution cycles')
		try:
			while(True):	#until stopped by golly
				g.show('cells moving')
				for i in range(5): # rounds of cell movement
					#logging.debug('movement round '+str(i))
					lg_envmt.cellMotions()
					#logging.debug('cells moved')
					lg_envmt.drawColor()
					#logging.debug('cells recolored')
					g.update()
					#logging.debug('golly updated')
					#time.sleep(1)

				g.show('cells evolving')
				# one round of evolution:
				#logging.debug('evolution round started')
				g.step()
				#g.update()
				#logging.debug('golly evolution complete')
				lg_envmt.update()
				#logging.debug('cellList updated')
				lg_envmt.drawColor()
				#logging.debug('cells recolored')
				g.update()
				#logging.debug('golly updated')
				#time.sleep(1)
		finally:
				logging.info('cycling halted from external source (probably golly)')
				g.show('closing gracefully, hold on just a sec...')
				lg_envmt.teardown()
				#TODO: save cell genomes to file


#MAIN
run()
