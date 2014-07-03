# The webUI branch is a massive refactoring designed to move away from golly as the primary UI and towards a web-app.#
Things right now are probably broken, outdated, and undocumented. Hang tight while the awesome is brewing.

![LifeGenes inherited coloration](http://i.imgur.com/Kx7DHmP.png)
==================================================================

The LifeGenes project for genetic cellular automaton adds genetic inheritance and various traits to the cells in [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life). This branch is a deviation from the Golly implementation of LifeGenes, and aims to provide a multiplayer experience driven by your browser in HTML5. This is accomplished by a Java/LIBGDX to HTML5 Canvas front-end, with a Python Gevent server for the back-end.

This is a highly collaborative project in progress originating from [/r/collaboratecode](http://www.reddit.com/r/CollaborateCode/); please don't hesitate to fork, send pull requests, report issues, or ask questions! For help and more information check out [the wiki](https://github.com/7yl4r/LifeGenes/wiki), our [google+ community](https://plus.google.com/communities/117413839180254151272), or the tentative [project outline](https://docs.google.com/document/d/1J2VmziJeNyKQskGeW49x_LJf8Pt3dW5QQK-ghKpZ8bw/edit?usp=sharing).

### Current Cell Traits ###
* color - expressed using a 256 state layer using custom golly rule 'constant.table'
* Neural network based AI which determines cell movement

### Planned Cell Traits ###
* mass/speed movement rules
* Neural network based AI which releases/recieves inter-cell communication signals (i.e. chemoreceptors)

## Getting Started ##
TODO

## Want to Contribute? ##
Please do! You may want to check out [my python style explanation](https://gist.github.com/7yl4r/6756413) for details on how/why this project deviates from PEP8.

You can start by knocking out plenty of TODOs in the code itself. There are many holes left when Golly was ripped out of the picture, and they need the TLC they deserve.

Then check our [github issue tracker](https://github.com/7yl4r/LifeGenes/issues?state=open) for bugs or enhancements which need fixing. 

## Acknowledgements & Dependencies##
Gradle builds and compiles our project and pulls in the necessary LIGDX files to get you coding. 
* [Gradle](http://www.gradle.org/) - Gradle combines the power and flexibility of Ant with the dependency management and conventions of Maven into a more effective way to build. Powered by a Groovy DSL and packed with innovation, Gradle provides a declarative way to describe all kinds of builds through sensible defaults. Gradle is quickly becoming the build system of choice for many open source projects, leading edge enterprises and legacy automation challenges.

The following dependencies are packaged into the LifeGenes.lifegenes_core.__util directory and no setup or worry about them is needed, but they help make this work possible and merit mention here:
* [appdirs](https://pypi.python.org/pypi/appdirs/1.2.0) - "A small Python module for determining appropriate platform-specific dirs". Used under permission of the [MIT License](http://opensource.org/licenses/MIT).
