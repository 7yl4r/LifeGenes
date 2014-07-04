from threading import Timer

from gevent import spawn
from gevent.server import StreamServer
from gevent.pool import Pool

from SocketHandler import Handler, parseInbound
from environment import environment
import ActionHandler

DELTA_T = 0.1  # seconds between updates


class GameManager(object):
    def __init__(self, follyInstance=None, userNum=256, ipAddress=('127.0.0.1', 7070)):
        """
        Creates a new game manager
        :param userNum: Max number of users allowed to connect at any time
        :param ipAddress: (ipAddressString, portAsInt)
        """
        self.env = environment(follyInstance)
        self.universe = follyInstance
        self.update_handle = Timer(DELTA_T, self.update)
        self.update_handle.start()
        self.pauseTime = 0  # amount of time to stay paused
        self.socketHandler = Handler()
        pool = Pool(userNum)  # Create a pool of greenlets
        self.server = StreamServer(ipAddress, handle=self.socketHandler, spawn=pool)
        # TODO: Restructure SocketHandler to not call outside code since the server needs to be in a subprocess
        spawn(self.server.serve_forever())

    def update(self):
        # get actions requested from connected sockets
        # TODO: Moved readSockets to SocketHandler. Need to fix this line below
        #actions = self.readSockets()
        actions = None  # temp until above is fixed
        # commit actions to the universe
        if actions is not None:
            ActionHandler.handleActions(self.universe, actions)

        self.universe.update(self)
        self.env.drawColor()
        self.env.cellMotions()  # Position to place this in update not sure

        # TODO: Send clients the changes
        for client in self.socketHandler.clients:
            data = None  # TODO: data = changes to client as a dict parsed as a string. Possibly using the action format
            client[0].send(data)

        self.update_handle = Timer(DELTA_T + self.pauseTime, self.update)
        self.pauseTime = 0
        self.update_handle.start()

    def getServer(self):
        return self.server

    def getUniverse(self):
        return self.universe