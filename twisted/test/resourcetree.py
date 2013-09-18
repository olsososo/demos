from twisted.web import resource,static,server


class ColorRoot(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
		self.requestedColors = []
		


class HomePage(resource.Resource):
	def render(self,request):
		return """
<html>
<head>
	<title>Colors</title>
	<link type = "text/css" href="/styles.css" rel = "Stylesheet" />
</head>
<body>
<h1>Colors Demo</h1>
What's here:
<ul>
	<li><a href="/color">Color Viewr</a></li>
</ul>
</body>
</html>
"""


if __name__ == "__main__":
	from twisted.internet import reactor
	
	root = resource.Resource()
	
	root.putChild('',HomePage())

	root.putChild('color',ColorRoot())

	root.putChild('style.css',static.File('styles.css'))

	site = server.Site(root)
	
	reactor.listenTCP(8000,site)
	
	reactor.run()
