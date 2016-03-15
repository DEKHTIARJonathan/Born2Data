Rapid API Prototyping with Bottle.py
####################################

:date: 2016-03-14 17:12
:tags: Python, API, REST, Bottle.py
:category: Python
:slug: fast-API-with-Bottle
:author: Jonathan DEKHTIAR
:headline: Python Tutorial: How to launch rapidly a REST API with Bottle.py

Rapid API Prototyping with Bottle.py
====================================

Python Tutorial: How to launch rapidly a REST API with Bottle.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Source File

Download all sources: `API_files.zip <{API_files.zip}../../../files/api_files/api_files.zip>`_

File: *server.py*

.. code-block:: python

   ################################# Import Libraries ################################
   import os.path
   import sys

   from loadConf import loadAPIConf

   import api

   #######################################################################################
   #######################################################################################
   #######################################################################################

   configAPI = loadAPIConf()

   serverAPI = {'port':configAPI['serverAPI']['port'], 'local':configAPI['serverAPI']['local']}

   api = api.API(serverAPI['port'], serverAPI['local'])
   api.start()

File: *loadConf.py*

.. code-block:: python

  ################################# Import Libraries ################################
  import os.path
  import xml.etree.ElementTree as XML

  def loadAPIConf(confPath = 'conf.xml'):
    configurations = XML.parse(confPath).getroot()

    servers = dict()

    for serv in configurations.iter('APIserver'):

      serverName = serv.attrib['serverName']
      serverPort = serv.attrib['port']
      serverIP = serv.attrib['ip']
      serverLocal = serv.attrib['local']

      servers[serverName] = {'ip':serverIP, 'port':serverPort, 'local':str2bool(serverLocal)}

    return servers

  def str2bool(v):
    return v.lower() == "true"

File: *api.py*

.. code-block:: python

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

File: *conf.xml*

.. code-block:: xml

  <!-- ################################# Config File ################################ -->

  <config>

      <APIserver serverName="serverAPI" local="false"  ip="127.0.0.1" port="8080"/>

  </config>


A transition should not begin or end a
section or document, nor should two
transitions be immediately adjacent.
