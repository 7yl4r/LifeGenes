# this module contains functions which are useful for evaluating and optimizing performance of another function.

from time import time

# runs a given test n times and makes a simple display. 'test' can be function or string to be run with eval()
# example: timedRuns('randrange(0,10)',100) will find a random int between 0 and 10 100 times and print out the estimated avg time to complete.
# example2: timedRuns(randRange(0,10),100) does the same thing
def timedRuns(test,n):	#TODO: add args parameter
	if hasattr(test, '__call__'):
		t = list()
		sTime = time()
		for i in range(n):
			startTime = time()
			test()
			endTime = time()
			t.append(endTime-startTime)
		eTime = time()
		scale = 39/max(t)
		for ttt in t:
			print '|'*int(round(ttt*scale)+1)
		print "tests complete.\n\t est avg time to complete:"+str((eTime-sTime)/n)+'s'
		print "slowest: "+str(max(t))+"s, quickest: "+str(min(t))+"s"
	else: #try to eval as string
		t = list()
		sTime = time()
		for i in range(n):
			startTime = time()
			eval(test)
			endTime = time()
			t.append(endTime-startTime)
		eTime = time()
		scale = 38/max(t)
		for ttt in t:
			print '|'*int(round(ttt*scale)+1)
		print "tests complete for '"+test+"'.\n\t est avg time to complete:"+str((eTime-sTime)/n)+'s'
		print "slowest: "+str(max(t))+"s, quickest: "+str(min(t))+"s"
