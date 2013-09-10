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
	pass


def poetry_main():
	addresses = parse_args()
	print addresses

if __name__ == '__main__':
	poetry_main()
