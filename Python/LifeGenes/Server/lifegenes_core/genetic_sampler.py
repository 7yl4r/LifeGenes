# this script prompts the user to take a genetic sample from the displayed cells and then saves it for later examination or use.

import logging

from Folly import FollyInstance
from LifeGenes.Server.lifegenes_core.environment import environment
from LifeGenes.Server.lifegenes_core.cellPallate import CELL_COLLECTION_DIR, cellPallate


# noinspection PyCallByClass
def collect_dna():
	# prepare environment
	g = FollyInstance()
	cellList = g.getCells()
	env = environment()

	# ask user to select cell of interest
	g.setcursor("Pick")
	g.show('select cell to sample')
	event = g.getevent(True)  # turn on golly event script access
	while not event.startswith("click"):
		event = g.getevent()  # return event handling to golly
	# event is a string like "click 10 20 left none"
	g.getevent(False)  # return event handling to golly
	evt, xstr, ystr, butt, mods = event.split()
	x = int(xstr)
	y = int(ystr)
	logging.info('cell (' + xstr + ',' + ystr + ') selected')
	try:
		# retrieve selected cell
		selectedCell = env.cellList.findCell(x, y)
	except AttributeError:
		g.show('cannot find cell!')
		logging.error('cell not found. len(cellList)=' + str(len(cellList.cells)))
		env.teardown()
		return

	# prompt user for name 
	import Tkinter as tk

	root = tk.Tk()

	class selectorDisplay:
		def __init__(self, master, selectedCell):
			self.pallate = cellPallate()  # cell pallate instance for saving cell info

			self.frame = tk.Frame(master)
			self.frame.pack()
			self.cell = selectedCell

			instructions = tk.Label(root, text='Please enter a name for this cell.\n\
			                        NOTE: names should only consist of letters, numbers, "_", and "-"')
			instructions.pack()

			self.entry = tk.Entry(master)
			self.entry.pack()
			self.entry.focus_set()

			button_save = tk.Button(master, text="save", width=10,
			                        command=self.submitEntry)
			button_save.pack()

			button_cancel = tk.Button(master, text="cancel", width=10,
			                          command=self.frame.quit)
			button_cancel.pack()

		def submitEntry(self):
			# save the cell
			name = self.entry.get()

			g.show('saving ' + name + ' to ' + CELL_COLLECTION_DIR)

			saved = self.pallate.saveCell(self.cell, name)

			if saved:
				self.frame.quit()  # close dialog
				g.show('DNA sample saved to collection')

	selectorDisplay(root, selectedCell)
	root.mainloop()
	import _tkinter

	try:
		root.destroy()  # optional...ish
	except _tkinter.TclError:
		pass  # ignore failed destroy due to already being destroyed.

	env.teardown()
	return

# make DNA display?
# from Tkinter import *

# root = Tk()

# w = Label(root, text="Hello, world!")
# w.pack()

# root.mainloop()
