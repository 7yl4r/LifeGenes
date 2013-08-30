![LifeGenes inherited coloration](http://i.imgur.com/Kx7DHmP.png)
==================================================================

The LifeGenes project for genetic cellular automaton adds genetic inheritance and various traits to the cells in [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life). This is accomplished primarily through [golly](http://golly.sourceforge.net/)'s python scripting interface. 

This is a highly collaborative project in progress originating from [/r/collaboratecode](http://www.reddit.com/r/CollaborateCode/); please don't hesitate to fork, send pull requests, report issues, or ask questions! For help and more information check out [the wiki](https://github.com/7yl4r/LifeGenes/wiki), our [google+ community](https://plus.google.com/communities/117413839180254151272), or the tentative [project outline](https://docs.google.com/document/d/1J2VmziJeNyKQskGeW49x_LJf8Pt3dW5QQK-ghKpZ8bw/edit?usp=sharing).

### Current Cell Traits ###
* color - expressed using a 256 state layer using custom golly rule 'constant.table'
* Neural network based AI which determines cell movement

### Planned Cell Traits ###
* mass/speed movement rules
* Neural network based AI which releases/recieves inter-cell communication signals (i.e. chemoreceptors)

## Getting Started ##
1. *install golly & Python* - These scripts must be run from within golly (v2.5 tested) and you need python v2.7 (v3.3 has known compatibilty issues with golly) to run them. Start out by installing and playing around with those two a bit if you aren't already familiar.
2. *place scripts and rules where golly can find them* - find golly's install directory and then merge our 'golly' folder with the install directory (called 'golly' by default). HINT: golly's home directory will be something like '/usr/share/golly' for ubuntu or 'C:\Program Files\golly\' for windows. The file structure should be properly set up to make sure all scripts, rules, and patterns end up in their right place.
3. *Load the scripts in golly* - [from golly's python instructions](http://golly.sourceforge.net/Help/python.html): To run one of these scripts, tick the Show Scripts item in the File menu and then simply click on the script's name. You can also select one of the Run items in the File menu.
4. *Observe genetic evolution in action!*

Advanced users may want to *modify scripts* - [golly's python instructions](http://golly.sourceforge.net/Help/python.html) contain golly's python scripting documentation. Note that (on Linux) golly can get confused after experiencing a python bug and persistant errors while debugging can sometimes be fixed by restarting golly. Similarly, imported files will not get re-imported when re-running a script unless golly restarts.
