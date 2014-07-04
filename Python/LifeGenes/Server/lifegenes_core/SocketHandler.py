from __future__ import print_function

import ClientAction
from Cell import Cell

# this handler will be run for each incoming connection in a dedicated greenlet
class Handler():
    def __init__(self):
        self.clients = []

    def __call__(self, socket, address):
        self.clients.append((socket, address))

        print('New connection from %s' % address)

        # socket.sendto(parseOutbound(Action.Message('Connected to LifeGenes server\r\n')), address)

    # TODO: This needs testing. It *might* work
    def readSockets(self):
        """
        Reads server socket file to see if there's anything to be read.
        If there is something to be read, parse into object and return actions,
        then flush the file.
        :return: Actions, or None if there isn't any
        """

        actions = []
        for socket, address in self.clients:
            fileobj = socket.makefile()
            socket.wait_read(fileobj, timeout=5)
            line = fileobj.readline()
            iter = 0
            while line is not '':
                actions.append(parseInbound(line))
                iter += 1

            if iter is 0:
                print("client %s disconnected" % address)
                fileobj.flush()

            fileobj.flush()

        return actions

def parseInbound(line, delim='~'):
    """
    Parse socket information
    :param line: readline coming from socket stream
    :param delim: delimiter to separate values in the string
    :return Action: returns action full of data for use
    """
    payload = line.strip().split(delim)

    ID = payload[0]
    action = ClientAction.getClientAction(ID)

    # Compile actions
    if isinstance(action, ClientAction.Message):
        action(payload[1])
    elif isinstance(action, ClientAction.NewCell):
        action(Cell.decompress(payload[1]))
    elif isinstance(action, ClientAction.RemoveCell):
        action(payload[1])
    elif isinstance(action, ClientAction.MoveCell):
        action(payload[2], payload[3], payload[1])
    elif isinstance(action, ClientAction.ChangeCellColor):
        action(payload[1], payload[2])
    else:
        raise Exception("Inbound parsing failed: Unknown action acquired")

    return action


# TODO
def parseOutbound(action, delim='~', data=None):
    """

    :param delim: delimiter to separate values in the string
    :param action: possible actions: ChangeCellColor, Message, MoveCell, RemoveCell, NewCell
    :param data: extra data as a dict, if any
    :return: payload as a string
    """
    # Parse actions
    payload = ''

    return payload