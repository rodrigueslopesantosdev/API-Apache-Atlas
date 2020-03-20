# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:30:36 2019

@author: tiago.santos
"""

def getTodasEntidades(hostname, port, username, password):
    return 'curl -X GET \
    http://'+hostname+':'+port+'/api/atlas/v2/types/typedefs \
    -u '+username+':'+password       


#def constroiJsonGlossaryTerm (hostname, port, username, password, metadados, guidGlossario):
def adicionaNovosDadosGlossario(hostname, port, username, password, metadados, guidGlossario):
    estruturaBasicaJson = 'curl -X POST \
  http://'+hostname+':'+port+'/api/atlas/v2/glossary/terms \
  -u '+username+':'+password+' \
  -H \''+'content-type: application/json'+'\' \
  -d \'['
    for pos in metadados:
        estruturaDadosGlossario='{"name" : "'+pos['Nome do dado']+'",\
        "Nome do dado" : "'+pos['Nome do dado']+'",\
        "Definicao semantica de negocio" : "'+pos['Definicao semantica de negocio']+'",\
        "Dado sensivel" : "'+pos['Dado sensivel']+'",\
        "Area responsavel" : "'+pos['Area responsavel']+'",\
        "Fonte de origem" : "'+pos['Fonte de origem']+'",\
        "longDescription" : "",\
        "anchor" : {"glossaryGuid" : "'+guidGlossario+'"}\
        },'
        estruturaBasicaJson = estruturaBasicaJson + estruturaDadosGlossario
    
    fim = len(estruturaBasicaJson)
    estruturaBasicaJson = estruturaBasicaJson[0:fim-1] + ']'+'\''
    return estruturaBasicaJson


def getDadosGlossario(hostname, port, username, password, guidGlossario):
    estruturaComando = 'curl -X GET \
  http://'+hostname+':'+port+'/api/atlas/v2/glossary/'+guidGlossario+'/terms\
  -u '+username+':'+password+'\
  -H \''+'content-type: application/json'+'\''
    
    return estruturaComando

        
def criaGlossario(hostname, port, username, password, nomeGlossario):
    return 'curl -X POST \
  http://'+hostname+':'+port+'/api/atlas/v2/glossary/ \
  -u '+username+':'+password+' \
  -H \''+'content-type: application/json'+'\' \
  -d \'{"name" : "'+nomeGlossario+'","shortDescription" : "glossario projeto D580","guid" : "-1"}\''
  

def getGlossario(hostname, port, username, password):
    return 'curl -X GET \
  http://'+hostname+':'+port+'/api/atlas/v2/glossary/ \
  -u '+username+':'+password+' \
  -H \''+'content-type: application/json'+'\''