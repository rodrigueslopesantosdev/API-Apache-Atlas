# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:08:57 2019

@author: tiago.santos
"""
import csv
from FuncoesCargaGlossario import *
from ConexaoSSH import ConexaoSSH

hostname=''
port=''
username=''
password=''
guidGlossario = ''
 
arquivoCSV = csv.DictReader (open ("<path>"))

#cabecalhoCSV = arquivoCSV.fieldnames

#print (cabecalhoCSV)

#jsonFinal = constroiJsonPutTypeDef(cabecalhoCSV)
        
#print (jsonFinal)

#result = jsonFinal.strip('\n').strip('\t').strip(' ')

#print (result)

#conexao = ConexaoSSH(hostname,port,username,password)
#conexao.exec_cmd (result)


jsonFinalTerm = constroiJsonGlossaryTerm(arquivoCSV, guidGlossario)

resultTerm = jsonFinalTerm.strip('\n').strip('\t').strip(' ')

print (resultTerm)

conexao = ConexaoSSH(hostname,port,username,password)

conexao.exec_cmd (resultTerm)

