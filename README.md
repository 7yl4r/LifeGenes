![LifeGenes inherited coloration](http://i.imgur.com/Kx7DHmP.png)
==================================================================

The LifeGenes project for genetic cellular automaton adds genetic inheritance and various traits to the cells in [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life). This is accomplished through [golly](http://golly.sourceforge.net/)'s python scripting interface. 

This is a highly collaborative project in progress ogiginating from [/r/collaboratecode](http://www.reddit.com/r/CollaborateCode/); please don't hesitate to contact us or to join in the fun! More information can be found in the tentative [project outline](https://docs.google.com/document/d/1J2VmziJeNyKQskGeW49x_LJf8Pt3dW5QQK-ghKpZ8bw/edit?usp=sharing).

### Current Cell Traits ###
* color - color is expressed using a 255 state layer using custom golly rule in 'constant.table'

### Planned Cell Traits ###
* Neural-network based AI
* mass/speed movement rules

## Getting Started ##
1. *install golly* - These scripts must be run from within golly. Start out by installing and playing around with that a bit.
2. *place scripts and rules where golly can find them* - find golly's install directory and then place the 'LifeGenesGolly' folder into /golly/scripts/python/. To use the cell color display, you must also place 'constant.table' into golly/rules/
3. *Load the scripts in golly using the gui*
4. *modify scripts* - [here](http://golly.sourceforge.net/Help/python.html) you can find golly's python scripting documentation. Also note that golly can get confused after experiencing a python bug and persistant errors while debugging can sometimes be fixed by restarting golly. Similarly, imported files will not get re-imported when re-running a script unless golly restarts.
