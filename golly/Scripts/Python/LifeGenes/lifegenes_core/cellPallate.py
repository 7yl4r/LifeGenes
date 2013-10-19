import pickle
import logging

from LifeGenes.lifegenes_core.__util.appdirs import user_data_dir
import errno
from os.path import join
from os import getcwd, chdir, makedirs
from glob import glob
import Tkinter as tk
try:
	from PIL import Image, ImageTk
except ImportError:
	raise ImportError("this function requires the Python Imaging Library (PIL). "
		+"See http://www.pythonware.com/products/pil/ "
		+"or https://github.com/python-imaging/Pillow for more.")

saveDir = user_data_dir('LifeGenes','7yl4r-ware')
DNA_COLLECTION_FILE= join(saveDir,'dna_collection.pk')
CELL_COLLECTION_DIR= join(saveDir,'cellCollection')

class cellPallate:
# defines a pallate of saved DNA sequences
# ATTRIBUTES:
#	pallate = list of cell objects in the pallate
#	pallateImages = a list of image files for each cell in pallate
#	cellNames = a list of cell object names
#	selected= number representing currently selected dna sequence in pallate
# PUBLIC METHODS:
#	load = loads dna strings from file into pallate
#	save = saves dna pallate to file
#	display = 
	def __init__(self):
		self.pallate = list()
		self.pallateImages = list()
		self.cellNames = list()
		self.selected= None
		
	def __del__(self):
		pass #self.save()
		
	def load(self):
	# loads all dna from file and puts it in the pallate
		startingDir = getcwd()
		chdir(CELL_COLLECTION_DIR)
		for file_ in glob("*"):
			with open(join(CELL_COLLECTION_DIR,file_,'cell.pk'),'rb') as f:
						self.pallate.append(pickle.load(f))
			self.pallateImages.append(join(CELL_COLLECTION_DIR,file_,'cell.png'))
			self.cellNames.append(file_)
		logging.info(str(len(self.pallate)) + ' DNA strings loaded into pallate')
		chdir(startingDir)

	def __saveCellObj(self,cellObj,saveFile):
	# saves given cell object to given file
		with open(saveFile,'wb') as f:
			pickle.dump(cellObj, f, pickle.HIGHEST_PROTOCOL)
		logging.info('cell object saved to collection')

	def __saveCellImage(self,cellObj,saveFile):
	# creates and saves given cell genome image to given file
		import Image, ImageDraw
		#TODO: generate something nice looking here
		im = Image.new("RGB", (50,50), "black")
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

		cellNames
	def getUserChoice(self):
	# creates a tkinter display which shows the pallate and allows for selection
		root = tk.Tk()
		class selectorDisplay:
			def __init__(self, master, cellPallate):
				self.cellPallate = cellPallate
				self.selected = None
				self.frame = tk.Frame(master)
				self.frame.pack()

				self.imageButtons = list()

				for img in self.cellPallate.pallateImages:
					self.insertButton(img,str(img))

				select_butt = tk.Button(self.frame, text="Clone this cell.", command=self.submit)
				select_butt.pack()

			def insertButton(self,img,text):
			# insert cell button
				image = Image.open(img)
				cellImage = ImageTk.PhotoImage(image)

				i = len(self.imageButtons) # i = index of new button
				self.imageButtons.append(tk.Button(self.frame, 
					text=str(text), 
					image=cellImage, 
					command=(lambda i=i:(self.raiseButtons(),
						self.imageButtons[i].config(relief=tk.SUNKEN),
						self.setSelection(i),
						tk.Label(self.frame, text='cell strain "'+self.cellPallate.cellNames[i]+'" selected').pack(),
						#self.frame.mainloop()
					))
				))
				self.imageButtons[i].image = cellImage # keep a reference
				self.imageButtons[i].pack(side=tk.LEFT)

			def raiseButtons(self):
			# raise all buttons
				for but in self.imageButtons: 
					but.config(relief=tk.RAISED)

			def setSelection(self,choice):
			# sets the pallate selection
				self.selected = choice

			def submit(self):
				self.frame.quit() # close dialog
				self.cellPallate.select(self.selected)		

		app = selectorDisplay(root,self)
		root.mainloop()

		import _tkinter
		try:
			root.destroy() # optional...ish
		except _tkinter.TclError:
			pass # ignore failed destroy due to already being destroyed.

		return self.getSelectedCellObj()

	def getSelectedCellObj(self):
	# returns cell object currently selected
		return self.pallate[self.selected]
		
	def getSelectedCellName(self):
	# returns name of currently selected cell
		return self.cellNames[self.selected]

	def getSelectedCellImg(self):
	# returns image of currently selected cell
		return self.pallateImages[self.selected]
	
	def select(self,selection):
	# moves selection
		self.selected = selection
		logging.info(self.cellNames[self.selected]+' selected')
