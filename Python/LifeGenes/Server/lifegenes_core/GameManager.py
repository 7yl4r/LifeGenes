from threading import Timer

from gevent.server import StreamServer
from gevent.pool import Pool

from SocketHandler import Handler, parseInbound
from environment import environment as env
import ActionHandler

DELTA_T = 0.1  # seconds between updates


class GameManager(object):
    def __init__(self, follyInstance=None, userNum=256, ipAddress=('127.0.0.1', 7070)):
        """
        Creates a new game manager
        :param userNum: Max number of users allowed to connect at any time
        :param ipAddress: (ipAddressString, portAsInt)
        """

        self.universe = follyInstance
        self.update_handle = Timer(DELTA_T, self.update)
        self.update_handle.start()
        self.pauseTime = 0  # amount of time to stay paused
        self.socketHandler = Handler()
        pool = Pool(userNum)  # Create a pool of greenlets
        self.server = StreamServer(ipAddress, handle=self.socketHandler, spawn=pool)
        self.server.serve_forever()

    def update(self):
        # get actions requested from connected sockets
        actions = self.readSockets()
        # commit actions to the universe
        ActionHandler.handleActions(self.universe, actions)

        self.universe.update(self)
        env.drawColor(self.universe)
        env.cellMotions(self.universe)  # Position to place this in update not sure

        # TODO: Send clients the changes
        for client in self.socketHandler.clients:
            data = None  # TODO: data = changes to client gamestate as a dict parsed as a string
            client[0].send(data)

        self.update_handle = Timer(DELTA_T + self.pauseTime, self.update)
        self.pauseTime = 0
        self.update_handle.start()

    # TODO: This needs fixing.. pull connected sockets from SocketHandler and read
    def readSockets(self):
        fileobj = self.server.socket.makefile()
        self.server.socket.wait_read(fileobj, timeout=5)
        line = fileobj.readline()
        iter = 0
        actions = []
        while line is not '':
            actions.append(parseInbound(line))
            iter += 1

        if iter is 0:
            print("all clients disconnected")
            fileobj.flush()
            return None

        fileobj.flush()

        return actions

    def getServer(self):
        return self.server

    def getUniverse(self):
        return self.universe