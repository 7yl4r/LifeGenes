# Starting point for the application

from LifeGenes.Server.lifegenes_core.Folly import FollyInstance
from LifeGenes.Server.lifegenes_core.GameManager import GameManager

connection_info = ('127.0.0.1', 7070)
number_of_users = 256


try:
	instance = FollyInstance()
	gm = GameManager(follyInstance=instance, ipAddress=connection_info, userNum=number_of_users)
	while True:
		gm.update()
finally:
	print "Game server is shutting down"