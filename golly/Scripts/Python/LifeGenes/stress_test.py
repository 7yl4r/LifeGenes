# this script creates a cell genome for each cell in the current layer, 
# then displays the genetic 'color' of each cell.
# The script then begins cycling between rounds of cell movement and cell evolution.
# Please see the [LifeGenes project for genetic cellular automaton](https://github.com/7yl4r/LifeGenes) for more info.
try:
    import golly as g
except ImportError:
    from LifeGenes.lifegenes_core.tests.folly import folly as g

from LifeGenes.lifegenes_core.environment import environment as lifegenes_environment

from time import time    #for debugging timers

from LifeGenes.lifegenes_core.setupLog import setupLog

import logging
setupLog('stressTest.log')

def makeCheckerBoard(size):
    for x in range(size):
        for y in range(size):
            g.setcell(x,y,(x+y)%2)


class run():
    def __init__(self):
        try:
            g.show('setting up test')


            testSize = 100 #this is the size of one side of the square testing area
            g.select([-testSize/2,-testSize/2,testSize,testSize])
            #clear the canvas
            g.clear(1)
            g.clear(0)
            g.randfill(50)
            g.update()

            g.show('stressTest started')

            startTime = time()
            lg_envmt = lifegenes_environment()
            endTime = time()
            logging.debug('\tsetup t\t=\t\t'+str(endTime-startTime))
            g.update()

            startTime = time()
            lg_envmt.drawColor()
            endTime = time()
            logging.debug('\tcolorDraw t\t=\t' + str( endTime - startTime))
            g.update()
            
            startTime = time()
            lg_envmt.cellMotions()
            endTime = time()
            logging.debug('\tmovement t\t=\t' + str( endTime - startTime))
            g.update()

            startTime = time()
            lg_envmt.drawColor()
            endTime = time()
            logging.debug('\tcolor update t \t= ' + str( endTime - startTime))
            g.update()

            g.step()

            startTime = time()
            lg_envmt.update()
            endTime = time()
            logging.debug('\tevolve update t\t= ' + str( endTime - startTime))

            startTime = time()
            lg_envmt.cellMotions()
            endTime = time()
            logging.debug('\tmovement t\t=\t' + str( endTime - startTime))
            g.update()

            startTime = time()
            lg_envmt.drawColor()
            endTime = time()
            logging.debug('\tcolor update t\t= ' + str( endTime - startTime))
            g.update()



            g.update()
            g.show('test complete')
        finally:
                logging.info('cycling halted from external source (probably golly)')


#MAIN
run() 
