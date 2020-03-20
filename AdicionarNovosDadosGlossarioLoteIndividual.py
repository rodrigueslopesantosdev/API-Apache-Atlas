# -*- coding: utf-8 -*-
"""
Programa Python para adicionar novos dados ao glossário através da execução em lote.

Data de criação: 02/03/2020
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
import json
from CallAPIRest import CallAPIRest
from Funcoes import Funcoes
import pandas as pd
import time
from dill.tests.test_recursive import obj1


hostname = ""
port = ""
username = ""
password = ""
glossaryName = ""
dataDefColName = ""
pathCSVFile = ""
delimiter = ";"

#encodingCSVFile = "Windows-1252"
encodingCSVFile = "unicode_escape"
apiPath = '/api/atlas/v2'
headers = {'content-type': 'application/json;charset=utf8'}

df = pd.read_csv(pathCSVFile, sep=';', encoding=encodingCSVFile)
objs = df.to_dict(orient='records')

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)
glossaryGuid = apiRest.getGlossaryGuid(glossaryName)

alfabeto = Funcoes.criarAlfabetoUnicode()

num_records = 400

objs_to_send = objs[3198:3200]
for i in range(len(objs_to_send)):
    listTerms = apiRest.createTerm(objs_to_send[i], dataDefColName, glossaryGuid, alfabeto)
    resultRequest = apiRest.createGlossaryTerm(listTerms, dataDefColName, glossaryName, alfabeto)
    codeStatus = apiRest.getStatusCode()
    # saidaArquivo.write(str(codeStatus) + "\n")
    # saidaArquivo.write(str(resultRequest) + "\n")
    print(objs_to_send[i])
    print(codeStatus)
    print(resultRequest.text)