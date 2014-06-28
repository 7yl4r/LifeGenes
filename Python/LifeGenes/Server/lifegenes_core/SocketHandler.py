from __future__ import print_function

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

	def parseInbound(self, line):
		"""
		Parse socket information
		:param line: readline coming from socket
		"""
		# TODO: Create better communication methods (the one in GameManager looks great)
		strs = line.strip().split(sep=':')
		key = strs[0]
		value = strs[1]
		if key is 'quit':
			print("client quit")
		elif key is 'msg':
			print(value)

	def parseOutbound(self, data):
		"""
		Parse socket information
		:param data:
		:return: string full of params
		"""
		# TODO: Create better communication methods (the one in GameManager looks great)
		if isinstance(data, dict):
			return data
		elif isinstance(data, basestring):
			package = 'msg:'+data
		return package