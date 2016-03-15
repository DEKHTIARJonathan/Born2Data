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
