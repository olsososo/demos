from twisted.internet.defer import Deferred

def out(s):
	print s

d = Deferred()
d.addCallbacks(out,out)

d.callback('first result')
d.callback('second result')

print 'Finished'
