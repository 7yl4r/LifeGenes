# this script creates a cell genome for each cell in the current layer, 
# and then displays the genetic 'color' of each cell by creating another 
# layer using the custom rule 'constant.table' which allows for 255 
# unchanging states (and thus a nice range of colors).
# Please see the [LifeGenes project for genetic cellular automaton](https://github.com/7yl4r/LifeGenes) for more info.


from glife import rect
import golly as g

from LifeGenes.lifegenes_core.cell import cell	#import LifeGenes cell definition

if g.empty(): g.exit("The pattern is empty.")

# check for existing geneticColor layer
currindex = 0
colorIndex = -1
while currindex < g.numlayers():
	if g.getname(currindex) == 'geneticColor':
		# continue from where we left off
		colorIndex = currindex
		g.show('geneticColor layer already exists!')
		break
	else: currindex+=1
if colorIndex == -1:	#if we didn't find existing colorLayer
	#set up new colorLayer
	startpatt = g.getcells(g.getrect()) # get starting pattern array [x1,y1,x2,y2,...]
	cells = list() #create new cell list

	# add cell object to list
	for cellIndex in range(len(startpatt)/2):
		cells.append(cell(startpatt[cellIndex*2],startpatt[cellIndex*2+1]))
		cellIndex+=1

	g.show(str(len(startpatt)/2)+' cells found, '+str(len(cells))+' trait objects created.')


	# add color layer
	if g.numlayers() + 1 > g.maxlayers():
		g.exit("You need to delete a layer.")

	colorLayerIndex = g.addlayer()     # create layer for colors
	g.setname('geneticColor')
	g.setrule('constant')	#use custom constant rule
	g.setcolors([0,255,0, 0,0,255]) #live states vary from green to blue

	for c in cells:
		g.setcell(c.x,c.y,c.getColor())

	#TODO: set layer back to original layer

