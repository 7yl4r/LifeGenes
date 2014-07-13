from __future__ import print_function

import ClientAction
from Cell import Cell, decompress
import GameManager

DELIM = "^&*"

# this handler will be run for each incoming connection in a dedicated greenlet
class Handler():
    def __init__(self, socket, address):
        self.clients = []
        self.clients.append((socket, address))
        self.readSockets()

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
            while True:
                # TODO: fileobj blocks until client disconnects... But messages are getting sent
                line = fileobj.readline()
                if line is not None:
                    # TODO: If line has data this repeats continuously... which should not happen
                    parsedLine = parseInbound(line)
                    # append to actions if valid
                    if parsedLine is not None:
                        actions.append(parsedLine)
                else:
                    print("client %s disconnected" % str(address))
                    break
                fileobj.flush()
                if actions.__len__() > 0:

                    GameManager.QUEUE.put(actions)
                    actions = []


def parseInbound(line):
    """
    Parse socket information
    :param line: readline coming from socket stream
    :param delim: delimiter to separate values in the string
    :return Action: returns action full of data for use
    """
    payload = line.strip().split(DELIM)

    ID = int(payload[0])
    action = ClientAction.getClientAction(ID)

    # Compile actions
    if isinstance(action, ClientAction.Message):
        print("m")
        action(payload[1])
    elif isinstance(action, ClientAction.NewCell):
        print("m")
        action(decompress(payload[1]))
    elif isinstance(action, ClientAction.RemoveCell):
        print("m")
        action(payload[1])
    elif isinstance(action, ClientAction.MoveCell):
        print("m")
        action(payload[2], payload[3], payload[1])
    elif isinstance(action, ClientAction.ChangeCellColor):
        print("m")
        action(payload[1], payload[2])
    else:
        return None

    return action


# TODO
def parseOutbound(action, data=None):
    """

    :param action: possible actions: ChangeCellColor, Message, MoveCell, RemoveCell, NewCell
    :param data: extra data as a dict, if any
    :return: payload as a string
    """
    # Parse actions
    payload = ''

    return payload