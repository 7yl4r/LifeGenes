ACTION_IDS = {'NewCell': 0, 'RemoveCell': 1, 'MoveCell': 2, 'ChangeCellColor': 3, 'Message': 10}


def getClientAction(ID):
    print "Action Received: %s" % str(ID)
    for action, actionID in ACTION_IDS.iteritems():
        if (ID == actionID):
            print "ID is %s" % str(actionID)
            if action is 'NewCell':
                print "newCell"
                return NewCell()
            elif action is 'RemoveCell':
                print "remCell"
                return RemoveCell()
            elif action is 'moveCell':
                print "moveCell"
                return MoveCell()
            elif action is 'ChangeCellColor':
                print "colorCell"
                return ChangeCellColor()
            elif action is 'Message':
                print "message"
                return Message()
            else:
                print "ClientAction received has an unknown ID somehow"
    print "done finding actions."
    return None

class ClientAction(object):
    _ID = None
    _userID = None  # TODO: Implement a player ID so we know where the actions come from

    def getID(self):
        if self._ID is None:
            raise Exception
        else:
            return self._ID

    def getUserID(self):
        if self._userID is None:
            self._userID = 0  # Local test user
        else:
            return self._ID


class CellAction(ClientAction):
    _cellID = None

    def getCellID(self):
        if self._cellID is None:
            raise Exception
        else:
            return self._cellID


class NewCell(ClientAction):
    def __init__(self):
        super(NewCell, self).__init__()

    def __call__(self, cell):
        self._ID = ACTION_IDS.get('NewCell')
        self._cell = cell

    def getCell(self):
        return self._cell


class RemoveCell(CellAction):
    def __init__(self):
        super(RemoveCell, self).__init__()

    def __call__(self, cellID):
        self._ID = ACTION_IDS.get('RemoveCell')
        self._cellID = cellID


class MoveCell(CellAction):
    def __init__(self):
        super(MoveCell, self).__init__()

    def __call__(self, x, y, cellID):
        self._ID = ACTION_IDS.get('MoveCell')
        self._x = x
        self._y = y
        self._cellID = cellID

    def getX(self):
        return self._x

    def getY(self):
        return self._y


class ChangeCellColor(CellAction):
    def __init__(self):
        super(ChangeCellColor, self).__init__()

    def __call__(self, color, cellID):
        self._ID = ACTION_IDS.get('ChangeCellColor')
        self._cellID = cellID
        self._color = color

    def getColor(self):
        return self._color


class Message(ClientAction):
    def __init__(self):
        super(Message, self).__init__()

    def __call__(self, msg):
        self._ID = ACTION_IDS.get('Message')
        self._msg = msg

    def getMsg(self):
        return self._msg