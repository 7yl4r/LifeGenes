# Starting point for the application

from LifeGenes.Server.lifegenes_core.Folly import FollyInstance
from LifeGenes.Server.lifegenes_core.GameManager import GameManager

connection_info = ('127.0.0.1', 7070)
number_of_users = 256
close = False

try:
	instance = FollyInstance()
	gm = GameManager(follyInstance=instance, ipAddress=connection_info, userNum=number_of_users)
	while close is False:
		gm.update()

	# TODO: Implement a user-initiated close-down of the server
finally:
	print "Game server is shutting down"
	# Implement safe-closing code
	gm.getServer().kill()