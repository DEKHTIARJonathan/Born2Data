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
