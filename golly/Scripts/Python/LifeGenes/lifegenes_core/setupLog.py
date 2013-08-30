#BEGIN setup log file for this script:
import golly as g
from os.path import expanduser
from os import mkdir
import logging

def setupLog(logName='LifeGenesLog.txt'):
	# assume that you want your logs in LifeGenes source which is in your home directory
	# (this works best on my linux machine)
#	home = expanduser("~")
#	logDir = home+'\LifeGenes\__logs'
#	try:
#		mkdir(logDir)
#	except OSError:
#		pass # probably the dir already exists...
		
#	try:
#		logPath = logDir+'\\'+logName
#		print str(logging.getLogger())
#		logging.basicConfig(filename=logPath,\
#							level=logging.DEBUG,\
#							format='%(asctime)s %(levelname)s:%(message)s',\
#						   filemode='w')
#	except IOError: # couldn't open file
	# try putting logs in golly directory instead
	# ( this works best on windows...)
	logPath = logName
	logging.basicConfig(filename=logPath,\
					level=logging.DEBUG,\
					format='%(asctime)s %(levelname)s:%(message)s',\
					   filemode='w')
						   
	#NOTE: this file only resets when golly is restarted, 
	#      otherwise the log object is retained and reused, 
	#      appending to the file as the script is run multiple times
	g.show('created .log at '+str(logPath))
	#END log file setup