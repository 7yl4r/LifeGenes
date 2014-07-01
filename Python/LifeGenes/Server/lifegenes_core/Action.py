import abc


class Action(object):
	_ID = None

	def getID(self):
		if self._ID is None:
			raise Exception
		else:
			return self._ID


class CellAction(Action):
	_cellID = None

	def getCellID(self):
		if self._cellID is None:
			raise Exception
		else:
			return self._cellID


class NewCell(Action):
	def __init__(self, cell):
		super(NewCell, self).__init__()
		self._ID = 0
		self._cell = cell

	def getCell(self):
		return self._cell


class RemoveCell(CellAction):
	def __init__(self, cellID):
		super(RemoveCell, self).__init__()
		self._ID = 1
		self._cellID = cellID


class MoveCell(CellAction):
	def __init__(self, x, y, cellID):
		super(MoveCell, self).__init__()
		self._ID = 2
		self._x = x
		self._y = y
		self._cellID = cellID

	def getX(self):
		return self._x

	def getY(self):
		return self._y


class ChangeCellColor(CellAction):
	def __init__(self, color, cellID):
		super(ChangeCellColor, self).__init__()
		self._ID = 3
		self._cellID = cellID
		self._color = color

	def getColor(self):
		return self._color


class Message(Action):
	def __init__(self, msg):
		super(Message, self).__init__()
		self._ID = 10
		self._msg = msg

	def getMsg(self):
		return self._msg