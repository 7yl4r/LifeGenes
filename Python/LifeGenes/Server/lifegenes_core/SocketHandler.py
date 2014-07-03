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