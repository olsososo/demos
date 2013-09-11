from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


def got_poem(res):
	print 'Your poem is served'
	print res

def poem_failed(err):
	print 'No poetry for you'	

d = Deferred()

d.addCallbacks(got_poem,poem_failed)

d.errback(Failure(Exception('I have failed.')))

print "Finished"
