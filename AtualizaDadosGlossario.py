# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:08:57 2019

@author: tiago.santos
"""
import csv
from FuncoesCargaGlossario import *
from ConexaoSSH import ConexaoSSH
import json

hostname='srvpednd01.axxiom1.local'
port='21000'
username='admin'
password='Axxiom@2019'
nomeGlossario='Glossario D580'

hostnameSSH='192.168.46.135'
portSSH='22'
usernameSSH='root'
passwordSSH='cenhaPadra0'

conexao = ConexaoSSH(hostnameSSH,portSSH,usernameSSH,passwordSSH)

arquivoCSV = csv.DictReader (open ("C:\Tiago\Apache_Atlas\GlossarioNegocio.csv"))

for posMeta in arquivoCSV:
    comando = atualizaValoresAtributosDados (hostname, port, username, password, posMeta , nomeGlossario)
    resultComando = comando.strip('\n').strip('\t').strip(' ')
    #print (resultComando)
    dadosAtualizados = conexao.exec_cmd(resultComando)
    print (dadosAtualizados)

#dadosAtualizados = conexao.exec_cmd(resultComando)

conexao.fecharConexao()