#this script allows the user to select a genetic sample saved pallate and draw cells.

import golly as g
from LifeGenes.lifegenes_core.cellList import cellList
from LifeGenes.lifegenes_core.environment import environment 

import logging
from LifeGenes.lifegenes_core.setupLog import setupLog
setupLog('genetic_filler.log')

from LifeGenes.lifegenes_core.cellPallate import cellPallate

def draw_dna():
	# === load DNA pallate
	pallate = cellPallate()
	pallate.load()
	
	# === let user select DNA 
	pallate.display()
	
	# === let user draw
	g.setcursor("Draw")
	# prepare environment
	env = environment()
	event = g.getevent(True) #turn on golly event script access
	try:
		while True:	# loop until stop button is pressed
			event = g.getevent() # event is a string like "click 10 20 left none"
			evt, xstr, ystr, butt, mods = event.split()
			if evt=="click" and butt=="left" and mods=="none": # left click
				x = int(xstr)
				y = int(ystr)
				env.cellList.setCell(x,y,cell=pallate.getSelectedCell())
				logging.info('cell ('+xstr+','+ystr+') painted with "'+str(pallate.selected)+'"')		
	finally:		
		g.getevent(False) # return event handling to golly
		# === teardown
		env.teardown()
		return

# === MAIN ===
draw_dna()


