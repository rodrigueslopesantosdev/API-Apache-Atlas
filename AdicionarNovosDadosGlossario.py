# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:08:57 2019

@author: tiago.santos
"""
import csv
from CallAPIRest import CallAPIRest
#import normalize

apiPath = '/api/atlas/v2'
hostname=''
port=''
username=''
password=''
glossaryName=''
dataDefColName='Nome do dado'


headers = {'content-type': 'application/json;charset=utf8'}

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

arquivoCSV = csv.DictReader (open ("C:\Tiago\Apache_Atlas\GlossarioNegocio.csv"))

resultRequest = apiRest.createGlossaryTerms (arquivoCSV, dataDefColName, glossaryName)

print(apiRest.getStatusCode())

print (resultRequest)