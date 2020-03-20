# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:08:57 2019

@author: tiago.santos
"""
import csv
from CallAPIRest import CallAPIRest
import json
import normalize

apiPath = '/api/atlas/v2'
hostname=''
port=''
username=''
password=''
glossaryName=''
shortDescription=''
headers = {'content-type': 'application/json;charset=utf8'}

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

resultRequest = apiRest.createGlossary(glossaryName, shortDescription)

print(apiRest.getStatusCode())

print (resultRequest)
