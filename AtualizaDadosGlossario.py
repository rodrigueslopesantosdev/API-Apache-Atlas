# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:08:57 2019

@author: tiago.santos
"""
import csv
from FuncoesCargaGlossario import *
from ConexaoSSH import ConexaoSSH
import json

hostname=''
port=''
username=''
password=''
nomeGlossario=''

hostnameSSH=''
portSSH=''
usernameSSH=''
passwordSSH=''

conexao = ConexaoSSH(hostnameSSH,portSSH,usernameSSH,passwordSSH)

arquivoCSV = csv.DictReader (open ("<path>"))

for posMeta in arquivoCSV:
    comando = atualizaValoresAtributosDados (hostname, port, username, password, posMeta , nomeGlossario)
    resultComando = comando.strip('\n').strip('\t').strip(' ')
    #print (resultComando)
    dadosAtualizados = conexao.exec_cmd(resultComando)
    print (dadosAtualizados)

#dadosAtualizados = conexao.exec_cmd(resultComando)

conexao.fecharConexao()