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



parser = argparse.ArgumentParser(description='Script para criar uma classificacao no Apache Atlas')
parser.add_argument("--ht", default=1, help="Hostname")
parser.add_argument("--pt", default=1, help="Porta de conexão.")
parser.add_argument("--us", default=1, help="Usuário para autenticação.")
parser.add_argument("--pw", default=1, help="Password para autenticação.")
parser.add_argument("--gn", default=1, help="Nome do glossário.")


apiPath = '/api/atlas/v2'
headers = {'content-type': 'application/json;charset=utf8'}

args = parser.parse_args()
hostname = args.ht
port = args.pt
username = args.us
password = args.pw
glossaryName = args.gn

encodingCSVFile = 'utf-8'

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

listGuids = apiRest.getDataFieldsTable(glossaryName, <table_name>)

for pos in listGuids:
    apiRest.createGlossaryTermAssociation ('<zone_name>', '', pos)