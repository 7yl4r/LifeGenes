import pickle
import logging

from LifeGenes.lifegenes_core.__util.appdirs import user_data_dir
import errno
from os.path import join
from os import getcwd, chdir, makedirs
from glob import glob
saveDir = user_data_dir('LifeGenes','7yl4r-ware')
DNA_COLLECTION_FILE= join(saveDir,'dna_collection.pk')
CELL_COLLECTION_DIR= join(saveDir,'cellCollection')

class cellPallate:
# defines a pallate of saved DNA sequences
# ATTRIBUTES:
#	pallate = list of dna strings in the pallate
#	selected= number representing currently selected dna sequence in pallate
# PUBLIC METHODS:
#	load = loads dna strings from file into pallate
#	save = saves dna pallate to file
#	display = 
	def __init__(self):
		self.pallate = list()
		self.selected= None
		
	def __del__(self):
		pass #self.save()
		
	def load(self):
	# loads all dna from file and puts it in the pallate
		startingDir = getcwd()
		chdir(CELL_COLLECTION_DIR)
		for file_ in glob("*.pk"):
			with open(file_,'rb') as f:
				while True:
					try:
						self.pallate.append(pickle.load(f))
					except EOFError:
						logging.info(str(len(self.pallate)) + ' DNA strings loaded into pallate')
						return

	def __saveCellObj(self,cellObj,saveFile):
	# saves given cell object to given file
		with open(saveFile,'wb') as f:
			pickle.dump(cellObj, f, pickle.HIGHEST_PROTOCOL)
		logging.info('cell object saved to collection')

	def __saveCellImage(self,cellObj,saveFile):
	# creates and saves given cell genome image to given file
		import Image, ImageDraw
		#TODO: generate something nice looking here
		im = Image.new("RGB", (512,512), "black")
		draw = ImageDraw.Draw(im)
		draw.line((0, 0) + im.size, fill=128)
		draw.line((0, im.size[1], im.size[0], 0), fill=128)
		del draw 

		# write to stdout
		im.save(saveFile, "PNG")

		logging.info('cell image generated')
	
	def saveCell(self,cellObj,name):
	# public interface for saving given cell with given name.
	# saves the cell object and generates needed genome image.
		cellDir = join(CELL_COLLECTION_DIR,name)
		try:
			makedirs(cellDir)
		except: #cell already exists
			raise IOError('cell with name "'+name+'" already exists')

		objectFile = join(cellDir,'cell.pk')
		self.__saveCellObj(cellObj,objectFile)

		imageFile = join(cellDir,'cell.png')
		self.__saveCellImage(cellObj,imageFile)


		

		
	def display(self):
	# creates a tkinter display which shows the pallate and allows for selection
		import Tkinter as tk
		root = tk.Tk()
		class selectorDisplay:
			def __init__(self, master):
				frame = tk.Frame(master)
				frame.pack()
				
				try:
					from PIL import Image, ImageTk
				except ImportError:
					raise ImportError("this function requires the Python Imaging Library (PIL). See http://www.pythonware.com/products/pil/ or https://github.com/python-imaging/Pillow for more.")
				imageFile = join(saveDir,'images','test_image.png')
				image = Image.open(imageFile)
				cellImage = ImageTk.PhotoImage(image)
				
				def select1():
					print "button 1 selected"
					self.button1.config(relief=SUNKEN)
				
				self.button1 = tk.Button(frame, text=imageFile, image=cellImage, command=select1)
				self.button1.image = cellImage # keep a reference
				self.button1.pack()

				hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
				hi_there.pack()

			def say_hi(self):
				print "hi there, everyone!"
				w = tk.Label(root, text="Hello, world!")
				w.pack()
				root.mainloop()
		app = selectorDisplay(root)
		root.mainloop()
		import _tkinter
		try:
			root.destroy() # optional...ish
		except _tkinter.TclError:
			pass # ignore failed destroy due to already being destroyed.
		
	def getSelectedCell(self):
	# returns cell object currently selected
		return self.selected
	
	def select(self,selection):
	# moves selection and updates display
		self.selected = selection
