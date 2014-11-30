#this script allows the user to select a genetic sample saved pallate and draw cells.

import golly as g
from LifeGenes.lifegenes_core.cellList import cellList
from LifeGenes.lifegenes_core.environment import environment 
from LifeGenes.lifegenes_core.cell import cell

import logging
from LifeGenes.lifegenes_core.setupLog import setupLog
setupLog('genetic_filler.log')

from LifeGenes.lifegenes_core.cellPallate import cellPallate

def draw_dna():
    logging.debug('loading cell pallate')
    pallate = cellPallate()
    pallate.load()

    logging.debug('getting default pallate selection')
    chosenCell = pallate.getUserChoice()
    chosenName = pallate.getSelectedCellName()
    g.show('now drawing with DNA from '+chosenName)
    logging.debug('now drawing with DNA from '+chosenName+'='+str(chosenCell))

    # prepare environment
    env = environment()
    logging.debug('turning on golly even script access')
    event = g.getevent(True)  # turn on golly event script access
    # === let user draw
    g.setcursor("Draw")
    try:    #this try statement is just to ensure the 'finally' block is run
        while True:    # loop until stop button is pressed
            event = g.getevent() # event is a string like "click 10 20 left none"
            if len(event) < 1: # do not try to split empty string
                continue
            else:
                logging.debug('event recieved: "'+event+'"')
                evt, xstr, ystr, butt, mods = event.split()
                if evt=="click" and butt=="left" and mods=="none": # left click
#                    logging.debug('left click detected at '+xstr+','+ystr)
                    x = int(xstr)
                    y = int(ystr)
                    env.cellList.setCell(x,y,cell=cell(x,y,chosenCell.DNA))    #add cell to list
                    g.setcell(x,y,1)    #fill in functional cell
                    env.drawColor()    #update color layer to match
                    g.update()        #update golly display
                    logging.info('cell ('+xstr+','+ystr+') painted with "'+chosenName+'"')
                    g.show('cell painted. press "Esc" to stop drawing')
                else:
                    logging.info('event "'+event+'" not recognized')
    except:    # re-raise any errors encountered
        logging.error('unexpected error: '+sys.exc_info()[0])
        raise
    finally:
        g.getevent(False) # return event handling to golly
        g.show('done drawing '+chosenName+' cells.')
        logging.debug('done drawing '+chosenName+' cells.')
        # === teardown
        env.teardown()
        return

# === MAIN ===
draw_dna()


