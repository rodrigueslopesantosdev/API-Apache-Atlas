# -*- coding: utf-8 -*-
"""
Programa Python para associar uma classificação a algum termo técnico no Apache Atlas.

Data de criação: 26/12/2019
@author: Tiago Rodrigues Lopes dos Santos
"""
import csv
from CallAPIRest import CallAPIRest
import json
import boto3
import argparse
import os.path
import time
from Funcoes import Funcoes

timeOut = 60 #segundos
cicloTimeOut = 60
contCicloTimeOut = 0

parser = argparse.ArgumentParser(description='Script para associar uma classificação a algum termo técnico no Apache Atlas.')
parser.add_argument("--key", default=1, help="AWS Access Key usada para inicar a sessão.")
parser.add_argument("--saKey", default=1, help="AWS Secret Access Key usada para inicar a sessão.")
parser.add_argument("--reg", default=1, help="Região da AWS do onde o banco de dados do Athena está configurado.")
parser.add_argument("--ht", default=1, help="Hostname Apache Atlas.")
parser.add_argument("--pt", default=1, help="Porta de conexão Apache Atlas.")
parser.add_argument("--us", default=1, help="Usuário para autenticação Apache Atlas.")
parser.add_argument("--pw", default=1, help="Password para autenticação Apache Atlas.")
parser.add_argument("--db", default=1, help="Nome do banco de dados no AWS Glue.")
parser.add_argument("--tb", default=1, help="Nome da tabela no AWS Glue.")
parser.add_argument("--cf", default=1, help="Nome da classificação ou tag para associar ao termo técnico.")
parser.add_argument("--ds", default=1, help="Breve descrição sobre a classificação.")
parser.add_argument("--ph", default=1, help="Localização da tabela/arquivo no Data Lake.")

args = parser.parse_args()
awsAccessKeyId = args.key
awsSecretAccessKey = args.saKey
awsDefaultRegion = args.reg
hostname = args.ht
port = args.pt
username = args.us
password = args.pw
bancoTabela = args.db
tabela = args.tb
classificationName = args.cf
descricao = args.ds
localDataLake = args.ph

#lista de arquivos passada como parametro
fileNameProcurado = '<path>/crw_'+tabela+'_READY_MARCACAO'

#Loop de espera dos arquivos
while contCicloTimeOut < cicloTimeOut:
    # Testa se os arquivos ainda não foram encontrados
    if not os.path.isfile(fileNameProcurado):
        time.sleep(timeOut)
        contCicloTimeOut = contCicloTimeOut + 1
    # Se os arquivos forem encontrados, atribui as variaveis abaixo para sair do loop principal.
    else:
        contCicloTimeOut = cicloTimeOut


if os.path.isfile(fileNameProcurado):

    client = boto3.client('glue',
                          aws_access_key_id=awsAccessKeyId,
                          aws_secret_access_key=awsSecretAccessKey,
                          region_name=awsDefaultRegion)
    result = client.get_table(DatabaseName=bancoTabela, Name=tabela)
    listaTermoTecnico = list()
    for pos in result["Table"]["StorageDescriptor"]["Columns"]:
        listaTermoTecnico.append(pos["Name"])

    encodingCSVFile = 'utf-8'
    headers = {'content-type': 'application/json;charset=utf8'}
    apiPath = '/api/atlas/v2'

    apiRest = CallAPIRest(apiPath, hostname, port, username, password, headers)

    resultRequest = list()
    guidTermoTecnico = list()
    jsonGuid = dict()

    for posSearch in listaTermoTecnico:
        jsonResultRequest = apiRest.searchBasicTermosTecnicos(posSearch)
        guidTermoTecnico = apiRest.getGuidTermosTecnicos(bancoTabela, tabela, jsonResultRequest["entities"])
        jsonGuid[posSearch] = guidTermoTecnico

    for pos in listaTermoTecnico:
        for posGuid in jsonGuid[pos]:
            apiRest.createTermosTecnicosClassificacaoAssociation(classificationName,
                                                                 Funcoes.remover_acentos(descricao),
                                                                 localDataLake, posGuid)
else:
    print("Time out!! Arquivo não encontrado!")

try:
    os.remove(fileNameProcurado)
except FileNotFoundError as err:
    print(err)

print("Programa finalizado com sucesso!!")
