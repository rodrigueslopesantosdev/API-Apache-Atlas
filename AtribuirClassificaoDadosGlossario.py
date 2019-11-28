# -*- coding: utf-8 -*-
"""
Programa Python para criar uma associação entre a classificação e os dados no Apache Atlas.

Data de criação: 08/10/2019
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
from CallAPIRest import CallAPIRest
from Funcoes import Funcoes
import json
import argparse


#arquivoCSV = csv.reader (open ("C:\Tiago\Apache_Atlas\GlossarioNegocio_BKP.csv", encoding = encodingCSVFile))
#O código abaixo transformo o arquivo antigo em um novo sem acentos.
# with open ("C:\Tiago\Apache_Atlas\GlossarioNegocio.csv", encoding = encodingCSVFile) as fileReader:
#     with open ("C:\Tiago\Apache_Atlas\GlossarioNegocioNovo.csv", "w", encoding = encodingCSVFile) as fileWriter:
#         for line in fileReader:
#             fileWriter.write(Funcoes.remover_acentos(line))
#
# fileWriter.close()

parser = argparse.ArgumentParser(description='Script para criar uma classificacao no Apache Atlas')
parser.add_argument("--ht", default=1, help="Hostname")
parser.add_argument("--pt", default=1, help="Porta de conexão.")
parser.add_argument("--us", default=1, help="Usuário para autenticação.")
parser.add_argument("--pw", default=1, help="Password para autenticação.")
parser.add_argument("--gn", default=1, help="Nome do glossário.")
parser.add_argument("--dc", default=1, help="Nome do metadado de definição do dado.")
parser.add_argument("--cf", default=1, help="Nome da classificação.")
parser.add_argument("--ph", default=1, help="Caminho do arquivo CSV.")
parser.add_argument("--dl", default=1, help="Delimitador do arquivo CSV")

apiPath = '/api/atlas/v2'
headers = {'content-type': 'application/json;charset=utf8'}

args = parser.parse_args()
hostname = args.ht
port = args.pt
username = args.us
password = args.pw
glossaryName = args.gn
dataDefColName = args.dc
classificationName = args.cf
pathCSVFile = args.ph
delimiter = args.dl

encodingCSVFile='utf-8'

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

csvFile = csv.DictReader (open (pathCSVFile, encoding = encodingCSVFile), delimiter=delimiter)

#arquivoSaida = open("C:\Tiago\Apache_Atlas\ArquivoSaida.txt", "w+", encoding= encodingCSVFile)

resultRequest = apiRest.createGlossaryTermsAssociation(glossaryName, dataDefColName, classificationName, csvFile)

print(apiRest.getStatusCode())

#arquivoSaida.write(resultRequest)
#arquivoSaida.close()
print (resultRequest)