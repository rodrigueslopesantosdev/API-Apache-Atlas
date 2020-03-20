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
hostname='srvpednd01.axxiom1.local'
port='21000'
username='admin'
password='Axxiom@2019'
glossaryName='Glossario D580 Teste'
shortDescription='Glossario de termos de negãcio do projeto D580'
headers = {'content-type': 'application/json;charset=utf8'}

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

resultRequest = apiRest.createGlossary(glossaryName, shortDescription)

print(apiRest.getStatusCode())

print (resultRequest)
