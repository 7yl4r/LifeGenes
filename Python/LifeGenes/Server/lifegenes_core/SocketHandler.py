from __future__ import print_function

from Action import Action, ChangeCellColor, Message, MoveCell, RemoveCell, NewCell
from Cell import Cell

# this handler will be run for each incoming connection in a dedicated greenlet
class Handler():
	def __init__(self, socket, address):
		self.socket = socket
		self.address = address

		print('New connection from %s:%s' % address)
		socket.sendto(self.parseOutbound('Connected to LifeGenes server\r\n'), address)

		self.main()

	def main(self):
		# using a makefile because we want to use readline()
		fileobj = self.socket.makefile()
		while True:
			self.socket.wait_read(fileobj, timeout=5)
			line = fileobj.readline()
			iter = 0
			while line is not '':
				self.parseInbound(line)
				iter += 1

			if iter is 0:
				print("client %s disconnected" % self.address)

			fileobj.flush()

	def parseInbound(self, line, delim='~'):
		"""
		Parse socket information
		:param line: readline coming from socket stream
		:param delim: delimiter to separate values in the string
		"""
		payload = line.strip().split(delim)

		newCell = None
		msg = None
		rmCellID = None
		cellID = None
		x = None
		y = None
		color = None

		ID = payload[0]
		if ID is Message.getID():
			msg = payload[1]
		elif ID is NewCell.getID():
			newCell = Cell.decompress(payload[1])
		elif ID is RemoveCell.getID():
			rmCellID = payload[1]
		elif ID is MoveCell.getID():
			cellID = payload[1]
			x = payload[2]
			x = payload[3]
		elif ID is ChangeCellColor.getID():
			cellID = payload[1]
			color = payload[2]

		# TODO: Do something with this information
		return

	def parseOutbound(self, action=Action(), delim='~', data=None):
		"""

		:param delim: delimiter to separate values in the string
		:param action: possible actions: ChangeCellColor, Message, MoveCell, RemoveCell, NewCell
		:param data: extra data as a dict, if any
		:return: payload as a string
		"""
		# Parse actions
		payload = ''
		if isinstance(action, Action):
			ID = action.getID()
			payload += str(ID)

		if isinstance(action, Message):
			payload = payload + delim + action.getMsg()
		elif isinstance(action, NewCell):
			payload = payload + delim + action.getCell().compress()
		elif isinstance(action, RemoveCell):
			payload = payload + delim + action.getCellID()
		elif isinstance(action, MoveCell):
			payload = payload + delim + action.getCellID() + delim + action.getX() + delim + action.getY()
		elif isinstance(action, ChangeCellColor):
			payload = payload + delim + action.getCellID() + delim + action.getColor()

		return payload