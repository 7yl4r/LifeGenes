from threading import Timer

from gevent.server import StreamServer

from SocketHandler import Handler

from environment import environment as env

DELTA_T = 0.1  # seconds between updates


class GameManager(object):
	def __init__(self, follyInstance=None, userNum=256, ipAddress=('127.0.0.1', 7070)):
		"""
		Creates a new game manager
		:param userNum: Max number of users allowed to connect at any time
		:param ipAddress: (ipAddressString, portAsInt)
		"""

		self.sockets = list()  # list of all websocket connections open
		self.universe = follyInstance
		self.update_handle = Timer(DELTA_T, self.update)
		self.update_handle.start()
		self.pauseTime = 0  # amount of time to stay paused
		self.server = StreamServer(listener=ipAddress, handle=Handler, backlog=userNum)
		self.server.serve_forever()

	def update(self):
		# updates the universe
		self.universe.update(self)
		env.drawColor(self.universe)
		env.cellMotions(self.universe)  # Position in update not sure
		# TODO: Send clients the changes
		self.update_handle = Timer(DELTA_T + self.pauseTime, self.update)
		self.pauseTime = 0
		self.update_handle.start()

	def getServer(self):
		return self.server