# this script creates a cell genome for each cell in the current layer, 
# then displays the genetic 'color' of each cell.
# The script then begins cycling between rounds of cell movement and cell evolution.
# Please see the [LifeGenes project for genetic cellular automaton](https://github.com/7yl4r/LifeGenes) for more info.

# import time	#for delays when debugging

import logging
from LifeGenes.Server.lifegenes_core import environment as lifegenes_environment, setupLog

setupLog.setupLog('movingCells.log')


class run():
	def __init__(self, follyInstance):
		g = follyInstance
		logging.info('script started')
		lg_envmt = lifegenes_environment.environment()
		lg_envmt.drawColor()
		logging.info('setup complete; beginning evolution cycles')
		try:
			while True:  # until stopped by golly
				g.show('cells moving')
				for i in range(5):  # rounds of cell movement
					lg_envmt.cellMotions()
					lg_envmt.drawColor()
					g.update()

				g.show('cells evolving')
				# one round of evolution:
				g.step()
				lg_envmt.update()
				lg_envmt.drawColor()
				g.update()
		finally:
			logging.info('cycling halted from external source (probably golly)')
			g.show('closing gracefully, hold on just a sec...')
			lg_envmt.teardown()

# MAIN
run()
