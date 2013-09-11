import datetime,errno,optparse,socket
from twisted.internet import main


def parse_args():
	parser = optparse.OptionParser()
	_,addresses = parser.parse_args()
	
	if not addresses:
		parser.exit()
	
	def parse_address(addr):
		if ':' not in addr:
			host = '127.0.0.1'
			port = addr
		else:
			host,port = addr.split(':',1)

		if not port.isdigit():
			parser.error('ports must be integers.')
	
		return host,int(port)
	
	return map(parse_address,addresses)


class PoetrySocket(object):
	
	poem =''

	def __init__(self,task_num,address):
		self.task_num = task_num
		self.address = address
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socket.connect(address)
		self.sock.setblocking(0)

		from twisted.internet import reactor
		reactor.addReader(self)
	
	def fileno(self):
		try:
			return self.socket.fileno()
		except socket.error:
			return -1
	
	def connectionLost(self,reason):
		self.sock.close()
		
		from twisted.internet import reactor
		reactor.removeReader(self)

		for reader in reactor.getReaders():
			if isinstance(reader,PoetrySocket):
				return

		reactor.stop()		

	def doRead(self):
		bytes = ''

		while True:
			try:
				bytesread = self.sock.recv(1024)
				if not bytesread:
					break
				else:
					bytes += bytesread
			except socket.error,e:
				if a.args[0] == errno.EWOULDBLOCK:
					break
				return main.CONNECTION_LOST
			
			if not bytes:
				print "Task %d finished " %self.task_num
				return main.CONNECTION_DONE
			else:
				msg = "Task %d:got %d bytes of poetry from %s"
				print msg %(self.task_num,len(bytes),self.format_addr)
		
			self.poem += bytes
	
	def logPrefix(self):
		return 'Poetry'		

	def format_addr(self):
		host,port = self.address
		return "%s:%s" %(host or '127.0.0.1',port)



def poetry_main():
	addresses = parse_args()
	start = datetime.datetime.now()

	sockets = [PoetrySocket(i+1,addr) for i,addr in enumerate(addresses)]	
	
	from twisted.internet import reactor
	reactor.run()
	
	elapsed = datetime.datetime.now() - start 
	
	for i,sock in enumerate(sockets):
		print 'task %d bytes of poetry' %(i+1,len(sock.poem))
	
	print "Got %d poem in %s " %(len(addresses),elapsed)	


if __name__ == '__main__':
	poetry_main()
