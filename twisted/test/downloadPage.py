from twisted.web import client

import os
import tempfile
import sys


def downloadToTempFile(url):
	tmpfd,tempfilename = tempfile.mkstemp()
	os.close(tmpfd)
	return client.downloadPage(url,tempfilename).addCallback(returnFilename,tempfilename)

def returnFilename(result,filename):
	return filename	


if __name__ == "__main__":
	from twisted.internet import reactor
	
	def printFile(filename):
		for line in file(filename,"r+b"):
			sys.stdout.write(line)
	
		os.unlink(filename)
		reactor.stop()

	def printError(failure):
		print >> sys.stderr,"Error:",failure.getErrorMessage()

	if len(sys.argv) == 2:
		url = sys.argv[1]
		downloadToTempFile(url).addCallback(printFile).addErrback(printError)		
		reactor.run()
	else:
		print "Usage:%s <URL>" %__file__
