# -*- coding: utf-8 -*-
"""
Programa Python para adicionar novos dados ao glossário.

Data de criação: 08/10/2019
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
import json
from CallAPIRest import CallAPIRest
import pandas as pd
from Funcoes import Funcoes
import argparse
#import normalize


parser = argparse.ArgumentParser(description='Script para adição de dados em um glossário no Apache Atlas')

parser.add_argument("--ht", default=1, help="Hostname")
parser.add_argument("--pt", default=1, help="Porta de conexão.")
parser.add_argument("--us", default=1, help="Usuário para autenticação.")
parser.add_argument("--pw", default=1, help="Password para autenticação.")
parser.add_argument("--gn", default=1, help="Nome do glossário.")
parser.add_argument("--dc", default=1, help="Nome do metadado de definição do dado.")
parser.add_argument("--ph", default=1, help="Caminho do arquivo CSV.")
parser.add_argument("--dl", default=1, help="Delimitador do arquivo CSV")

args = parser.parse_args()
hostname = args.ht
port = args.pt
username = args.us
password = args.pw
glossaryName = args.gn
dataDefColName = args.dc
pathCSVFile = args.ph
delimiter=args.dl

encodingCSVFile = "unicode_escape"
apiPath = '/api/atlas/v2'
headers = {'content-type': 'application/json;charset=utf8'}

df = pd.read_csv(pathCSVFile, sep=';', encoding=encodingCSVFile)
objs = df.to_dict(orient='records')

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)
glossaryGuid = apiRest.getGlossaryGuid(glossaryName)
#Cria o alfabeto de Unicode Escape para os caracteres de 0 a 255.
alfabeto = Funcoes.criarAlfabetoUnicode()

#tamanho do lote
num_records = 400
#execução de 9 lotes para importação dos dados no glossário.
for i in range(9):
    if (i == 0):
        posInicial = 0
        posFinal = posInicial + (num_records - 1)
    else:
        posInicial = (i*num_records)
        posFinal = (i * num_records) + (num_records - 1)
    objs_to_send = objs[posInicial:(posFinal+1)]
    print(str(posInicial) + " : " + str(posFinal))
    if len(objs_to_send) > 0:
        listTerms = apiRest.createTerms(objs_to_send, dataDefColName, glossaryGuid, alfabeto)
        resultRequest = apiRest.createGlossaryTerms(listTerms, dataDefColName, glossaryName)
        codeStatus = apiRest.getStatusCode()
        print(codeStatus)
        print(resultRequest.text)