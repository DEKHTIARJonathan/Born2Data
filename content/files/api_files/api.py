################################# Import Libraries ################################
import os.path
from bottle import route, run, response, static_file, request, error, Bottle, template
from json import dumps, loads, load

#################################### WebService Route / #####################################
class API:
	def __init__(self, port, local):
		self._app = Bottle()
		self._route()

		self._local = local
		self._port = port

		if local:
			self._host = '127.0.0.1'
		else:
			self._host = '0.0.0.0'

	def start(self):
		self._app.run(server='paste', host=self._host, port=self._port)

	def _route(self):
		self._app.hook('before_request')(self._strip_path)
		self._app.route('/static/<filename:path>', callback=self._getStaticFile)
		self._app.route('/', callback=self._homepage)

		self._app.route('/action', method="POST", callback=self._doAction)
		self._app.route('/action', method="GET", callback=self._doAction)

	def _strip_path(self):
		request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')

	def _getStaticFile(self, filename):
		extension = str.lower(os.path.splitext(filename)[1][1:])
		if  extension == 'jpeg'or extension == 'jpg':
			return static_file(filename, root=os.getcwd()+'\\static', mimetype='image/jpg')
		elif extension == 'png':
			return static_file(filename, root=os.getcwd()+'\\static', mimetype='image/png')
		elif extension == 'css':
			return static_file(filename, root=os.getcwd()+'\\static', mimetype='text/css')
		elif extension == 'js':
			return static_file(filename, root=os.getcwd()+'\\static', mimetype='text/javascript')

	def _homepage(self):
		return static_file("index.html", root=os.getcwd()+'\\html')

	def _doAction(self):
		rv = {"status": "Success"}
		response.content_type = 'application/json'

		return dumps(rv)
