from twisted.internet.defer import Deferred

def got_poem(res):
	print 'your poem is served:'
	print res

def poem_failed(err):
	print err.__class__
	print err
	print 'no poetry for you'


d = Deferred()

d.addCallbacks(got_poem,poem_failed)

d.errback(Exception('I have failed.'))
