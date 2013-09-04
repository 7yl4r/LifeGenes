# this script creates a cell genome for each cell in the current layer, 
# and then displays the genetic 'color' of each cell by creating another 
# layer using the custom rule 'constant.table' which allows for 255 
# unchanging states (and thus a nice range of colors).
# Please see the [LifeGenes project for genetic cellular automaton](https://github.com/7yl4r/LifeGenes) for more info.

from LifeGenes.lifegenes_core.environment import environment as lifegenes_environment

import golly as g

import logging
setupLog('drawColors.log')

lg_envmt = lifegenes_environment()
lg_envmt.drawColor()

