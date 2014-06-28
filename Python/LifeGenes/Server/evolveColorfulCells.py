# this script creates a cell genome for each cell in the current layer, 
# and then displays the genetic 'color' of each cell by creating another 
# layer using the custom rule 'constant.table' which allows for 255 
# unchanging states (and thus a nice range of colors).
# Please see the [LifeGenes project for genetic cellular automaton](https://github.com/7yl4r/LifeGenes) for more info.

import logging

from LifeGenes.Server.lifegenes_core.setupLog import setupLog
from LifeGenes.Server.lifegenes_core.environment import environment as lifegenes_environment

setupLog('evolveCellsWithColor.log')


class run():
	def __init__(self, follyInstance):
		g = follyInstance
		logging.info('script started')
		lg_envmt = lifegenes_environment()
		lg_envmt.drawColor()
		logging.info('setup complete; beginning evolution cycles')
		try:
			while True:  # until stopped by golly
				g.step()
				lg_envmt.update()
				lg_envmt.drawColor()
				g.update()
		finally:
			logging.info('cycling halted from external source')
			g.show('closing gracefully, hold on just a sec...')
			lg_envmt.teardown()

# MAIN
run()
