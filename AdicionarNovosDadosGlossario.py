# -*- coding: utf-8 -*-
"""
Programa Python para adicionar novos dados ao glossário.

Data de criação: 08/10/2019
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
from CallAPIRest import CallAPIRest
import argparse
#import normalize

apiPath = '/api/atlas/v2'
headers = {'content-type': 'application/json;charset=utf8'}

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
delimiter= args.dl

encodingCSVFile='utf-8'

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

#arquivoCSV = csv.DictReader (open ("C:\Tiago\Apache_Atlas\GlossarioNegocio.csv", encoding = encodingCSVFile, delimiter=';'))
csvFile = csv.DictReader (open (pathCSVFile, encoding = encodingCSVFile), delimiter=delimiter)

resultRequest = apiRest.createGlossaryTerms (csvFile, dataDefColName, glossaryName)

print(apiRest.getStatusCode())

print (resultRequest.text)