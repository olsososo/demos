from twisted.web import http


def renderHomePage(request):
	colors ='red','blue','green'
	flavors = 'vanilla','chocolate','strawberry','coffes'
	
	request.write("""
<html>
<head>
	<title>Form Test</title>
</head>
<body>		
	<form action = "posthandler" method = "post">
		your name:
		<p>
			<input type ="text" name = "name">
		</p>
		what is your favourite color?
		<p>
""")
	for color in colors:
		request.write(
		"<input typr='radio' name='color' value='%s'>%s<br/>"%(color,color.capitalize()))
	
	request.write("""
		</p>
		what kinds of ice cream do you like?
		<p>
""")

	for flavor in flavors:
		request.write(
		"<input type = 'checkbox' name ='flavor' value ='%s'>%s<br/>" %(
		flavor,flavor.capitalize()))

	request.write("""
		</p>
		<input type = 'submit' />
	</form>
</body>
</html>
""")


def handlePost(request):
	request.write("""
<html>
<head>
	<title>Posted Form Data</title>
</head>
<body>
	<h1>Form Data</h1>
""")	
	for key,values in request.args.items():
		request.write("<h2>%s</h2>" %key)
		request.write("<ul>")
		
		for value in values:
			request.write("<li>%s</li>" %value)
	
		request.write("</ul>")
	
	request.write("""
</body>
</html>
""")	
	request.finish()
 
class FunctionHandleRequest(http.Request):
	pageHandlers = {
		'/':renderHomePage,
		'/posthandler':handlePost,
	}
	
	def process(self):
		self.setHeader("Content-Type","text/html")
		if self.pageHandlers.has_key(self.path):
			handler = self.pageHandlers[self.path]
			handler(self)
		else:
			self.setResponseCode(http.NOT_FOUND)
			self.write("<h1>Not Found</h1>Sorry,no such page.")
			self.finish()


class MyHttp(http.HTTPChannel):
	requestFactory = FunctionHandleRequest	


class MyHttpFactory(http.HTTPFactory):
	protocol = MyHttp
	

if __name__ == "__main__":
	from twisted.internet import reactor
	reactor.listenTCP(8000,MyHttpFactory())
	reactor.run()
