#this script prompts the user to take a genetic sample from the displayed cells and then saves it for later examination or use.

import pickle
import golly as g
from LifeGenes.lifegenes_core.cellList import cellList
from LifeGenes.lifegenes_core.environment import environment 
from LifeGenes.lifegenes_core.__util.appdirs import user_data_dir
from os.path import join

import logging
from LifeGenes.lifegenes_core.setupLog import setupLog
setupLog('genetic_sampler.log')

saveDir = user_data_dir('LifeGenes','7yl4r-ware')
DNA_COLLECTION_FILE= join(saveDir,'dna_collection.pk')

def collect_dna():
	# prepare environment
	env = environment()

	# ask user to select cell of interest
	g.setcursor("Pick")
	g.show('select cell to sample')
	event = g.getevent(True) #turn on golly event script access
	while not event.startswith("click"):
		event = g.getevent() # return event handling to golly
		# event is a string like "click 10 20 left none"
	g.getevent(False) # return event handling to golly
	evt, xstr, ystr, butt, mods = event.split()
	x = int(xstr)
	y = int(ystr)
	logging.info('cell ('+xstr+','+ystr+') selected')
	try:
		# retrieve selected cell DNA
		dna = env.cellList.findCell(x,y).DNA
	except AttributeError:
		g.show('cannot find cell!')
		logging.error('cell not found. len(cellList)='+str(len(cellList.cells)))
		env.teardown()
		return

	# TODO: prompt user for name 
	
	# save DNA to list of saved 
	with open(DNA_COLLECTION_FILE,'wb') as f:
		pickle.dump(dna, f, pickle.HIGHEST_PROTOCOL)
	g.show('DNA sample saved to collection')
	env.teardown()
	return

# === MAIN ===
collect_dna()


# make DNA display?
#from Tkinter import *

#root = Tk()

#w = Label(root, text="Hello, world!")
#w.pack()

#root.mainloop()