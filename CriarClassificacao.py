# -*- coding: utf-8 -*-
"""
Programa Python para criar uma classificação no Apache Atlas.

Data de criação: 08/10/2019
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
from CallAPIRest import CallAPIRest
import argparse
#import normalize

parser = argparse.ArgumentParser(description='Script para criar uma classificacao no Apache Atlas')
parser.add_argument("--ht", default=1, help="Hostname")
parser.add_argument("--pt", default=1, help="Porta de conexão.")
parser.add_argument("--us", default=1, help="Usuário para autenticação.")
parser.add_argument("--pw", default=1, help="Password para autenticação.")
parser.add_argument("--cf", default=1, help="Nome da classificação.")
parser.add_argument("--cd", default=1, help="Descrição breve da classificação")
parser.add_argument("--ph", default=1, help="Caminho do arquivo CSV.")
parser.add_argument("--dl", default=1, help="Delimitador do arquivo CSV.")

args = parser.parse_args()
hostname = args.ht
port = args.pt
username = args.us
password = args.pw
classificationName = args.cf
classDescription = args.cd
pathCSVFile = args.ph
delimiter = args.dl

encodingCSVFile='utf-8'
headers = {'content-type': 'application/json;charset=utf8'}
apiPath = '/api/atlas/v2'
#
# args = parser.parse_args()
# hostname = "ec2-3-86-115-15.compute-1.amazonaws.com"
# port = "21000"
# username = "admin"
# password = "admin"
# classificationName = "DefinicoesNegocio"
# classDescription = "Definicoes de negocio dos dados do projeto D580."
# #pathCSVFile = "C:\Tiago\Apache_Atlas\ArqGlossario_Novo_Teste.csv"
# pathCSVFile = "C:\Tiago\Apache_Atlas\GlossarioNegocio.csv"
# delimiter= ","


apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

csvFile = csv.DictReader (open (pathCSVFile, encoding = encodingCSVFile), delimiter=delimiter)

resultRequest = apiRest.createClassification(classificationName, classDescription, csvFile)

print(apiRest.getStatusCode())

print (resultRequest.text)