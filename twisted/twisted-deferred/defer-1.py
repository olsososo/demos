from twisted.internet.defer import Deferred


def got_poem(res):
	print 'your poem is served'
	print res

def poem_failed(err):
	print 'No poetry for you'	

d = Deferred()

d.addCallbacks(got_poem,poem_failed)

d.callback('This poem is short')


print 'finished'
