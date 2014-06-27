__author__ = 'brianerikson'

# clean workspace to run the simulation again

try: import golly as g
except ImportError:
	print 'could not load golly, using folly instead'
	from LifeGenes.lifegenes_core.tests.folly import folly as g

def reset():

	g.setlayer(g.numlayers() - 1)

	while g.getlayer() > 0:
		g.dellayer()
		g.setlayer(g.numlayers() - 1)

	g.reset()