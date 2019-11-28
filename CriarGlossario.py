# -*- coding: utf-8 -*-
"""
Programa Python para criar um novo glossário no Apache Atlas.

Data de criação: 08/10/2019
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
import sys
import argparse
from CallAPIRest import CallAPIRest
from Funcoes import Funcoes
import json

apiPath = '/api/atlas/v2'
headers = {'content-type': 'application/json;charset=utf8'}

parser = argparse.ArgumentParser(description='Script para criação de glossário de dados no Apache Atlas')

parser.add_argument("--ht", default=1, help="Hostname")
parser.add_argument("--pt", default=1, help="Porta de conexão")
parser.add_argument("--us", default=1, help="Usuário para autenticação")
parser.add_argument("--pw", default=1, help="Password para autenticação")
parser.add_argument("--gn", default=1, help="Nome do glossário.")
parser.add_argument("--sd", default=1, help="Descrição breve.")

args = parser.parse_args()
hostname = args.ht
port = args.pt
username = args.us
password = args.pw
glossaryName = args.gn
shortDescription = args.sd

apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

resultRequest = apiRest.createGlossary(Funcoes.remover_acentos(glossaryName), Funcoes.remover_acentos(shortDescription))

print(apiRest.getStatusCode())

print (resultRequest)