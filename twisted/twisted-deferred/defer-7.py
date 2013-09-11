import sys

from twisted.internet.defer import Deferred

def got_poem(poem):
	print poem

def poem_failed(err):
    print >>sys.stderr, 'poem download failed'
    print >>sys.stderr, 'I am terribly sorry'
    print >>sys.stderr, 'try again later?'

def poem_done(_):
	from twisted.internet import reactor
	reactor.stop()

def foo(_):
	print "hello world!"
	
d = Deferred()

d.addCallback(got_poem,poem_failed)
d.addBoth(foo)
d.addBoth(poem_done)


from twisted.internet import reactor

reactor.callWhenRunning(d.callback,'Another short poem')

reactor.run()
