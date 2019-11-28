# -*- coding: utf-8 -*-
"""
Classe que permite criar objetos para chamada da API do Apache Atlas.
Nessa classe foram construídos métodos para criar classificações com atributos, criar glossários,
criar dados para o glossário e associar a classificação criada nos dados do glossário.

Data de criação: 08/10/2019
@author: Tiago Rodrigues Lopes dos Santos
"""

import requests
from requests.auth import HTTPBasicAuth
from Funcoes import Funcoes
import json


class CallAPIRest:
    """
        Construtor com parâmetros:

        apiPath: caminho com a versão da api
        hostname: host onde a api está localizada
        port: porta de conexão da api
        username: usuário com acesso ao uso da api
        password: password da senha do usuário
        headers: cabeçalho para a chamada da api
    """
    def __init__(self, apiPath, hostname, port, username, password, headers):
        self.setURL(hostname, port, apiPath)
        self.setAuth(username, password)
        self.setHeaders(headers)
        self.__resultResponse = {}
        self.__status_code = {}

    """
        Método para alterar o valor do atributo apiPath
        
        Parâmetros:
            apiPath: caminho com a versão da api
    """
    def __setApiPath(self, apiPath):
        self.apiPath = apiPath

    """
          Método para alterar o valor do atributo hostname

          Parâmetros:
              hostname: host onde a api está localizada
    """
    def __setHostName(self, hostname):
        self.hostname = hostname

    """
          Método para alterar o valor do atributo port

          Parâmetros:
              port: porta de conexão da api
    """
    def __setPort(self, port):
        self.port = port

    """
          Método para alterar o valor do atributo headers

          Parâmetros:
              headers: cabeçalho para a chamada da api
    """
    def setHeaders(self, headers):
        self.headers = headers

    """
          Método para alterar o usuário na autenticação para consumo da API

          Parâmetros:
              username: usuário com acesso ao uso da api
              password: password da senha do usuário
    """
    def setAuth(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    """
          Método para alterar a url da API

          Parâmetros:
            hostname: host onde a api está localizada
            port: porta de conexão da api
            apiPath: caminho com a versão da api
    """
    def setURL(self, hostname, port, apiPath):
        self.__setHostName(hostname)
        self.__setPort(port)
        self.__setApiPath(apiPath)
        self.url = 'http://'+self.getHostName()+':'+self.getPort()+self.getApiPath()

    """
           Método para alterar o atributo status_code de retorno das respostas de chamadas da API

           Parâmetros:
             status_code: código de status retornado pelas chamadas das APIs
    """
    def __setStatusCode(self, status_code):
        self.status_code = status_code

    """
           Método para alterar o atributo resultResponse que apresenta o log de resposta das chamadas da API

           Parâmetros:
             resultResponse: dicionário com o log de resposta das chamadas da API
    """
    def __setResultResponse(self, resultResponse):
        self.resultResponse = resultResponse

    """
           Método para retornar o atributo resultResponse que apresenta o log de resposta das chamadas da API.
           Retorno:
                Tipo: dictionary
    """
    def __getResultResponse(self):
        return self.resultResponse

    """
               Método para retornar o apiPath da API
               Retorno:
                    Tipo: string
    """
    def getApiPath(self):
        return self.apiPath

    """
               Método para retornar o hostname da API
               Retorno:
                    Tipo: string
    """
    def getHostName(self):
        return self.hostname

    """
               Método para retornar a porta de conexão da API
               Retorno:
                    Tipo: string
                    
    """
    def getPort(self):
        return self.port

    """
               Método para retornar o objeto HTTPBasicAuth usado para autenticação na API.
               Retorno:
                    Tipo: HTTPBasicAuth
    """
    def getAuth(self):
        return self.auth

    """
               Método para retornar a URL completa da API.
               Retorno:
                    Tipo: string
    """
    def getUrl(self):
        return self.url

    """
               Método para retornar o cabeçalho usado na API.
               Retorno:
                    Tipo: string
                
    """
    def getHeaders(self):
        return self.headers

    """
               Método para retornar o status_code das respostas das chamadas da API.
               Return:
                    Tipo: tinyint
    """
    def getStatusCode(self):
        return self.status_code

    """
               Método para criar os atributos usados na classificação.
               
               Parâmetros:
                    attributes: dicionário contendo o arquivo CSV. Tipo: DictReader
    """
    def __createAttributes(self, attributes):
        listAttributes=''
        for pos in attributes.fieldnames:        
            listAttributes = listAttributes + '{"name":"'+Funcoes.remover_acentos(pos)+'","typeName":"string"},'
            
        return listAttributes

    """
               Método para criar os dados do glossário de dados.

               Parâmetros:
                    listTerms: Lista de termos. Tipo: DictReader
                    dataDefColName: Nome da coluna no glossário em que está definido o nome do dado
                    glossaryGuid: identificador interno do glossário no Apache Atlas.
    """
    def __createTerms(self, listTerms, dataDefColName, glossaryGuid):
        listResultTerms=''
        for pos in listTerms:
            listResultTerms = listResultTerms + '{"anchor":{"glossaryGuid":"'+glossaryGuid+'"},"longDescription":"","name":"'\
                              +Funcoes.remover_acentos(pos[dataDefColName])+'"},'
        return listResultTerms

    """
               Método para criar um glossário de dados.

               Parâmetros:
                    glossaryName: Nome do glossário de dados. Tipo: string
                    shortDescription: Descrição breve sobre o glossário. Tipo: string.
    """
    def createGlossary (self, glossaryName, shortDescription):
        urlPostGlossary =  self.getUrl() + '/glossary/'
        jsonData = '{"name" : "'+Funcoes.remover_acentos(glossaryName)+'","shortDescription":"' +Funcoes.remover_acentos(shortDescription)+'","guid" : "-1"}'
        resultResponse = requests.post(url=urlPostGlossary, auth=self.getAuth(), headers=self.getHeaders(), data=jsonData)
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (self.__getResultResponse())

    """
               Método para criar uma classificação no Apache Atlas.

               Parâmetros:
                    classificationName: Nome da classificação. Tipo: string.
                    classDescription: Descrição breve sobre a classificação. Tipo: string.
                    attributes: Lista de atributos (metadados) do glossário. Tipo: string.
    """
    def createClassification (self, classificationName, classDescription, attributes):
        urlPostClassification = self.getUrl() + '/types/typedefs'
        paramsList= {'type':'classification'}
        jsonData = '{"classificationDefs":[{"name":"'+Funcoes.remover_acentos(classificationName)+'","description":"'\
                   +Funcoes.remover_acentos(classDescription)+'","superTypes":[],"attributeDefs":['
        listAttirbutes = self.__createAttributes(attributes)
        jsonData = jsonData + listAttirbutes[0:(len(listAttirbutes)-1)] + ']}]}'
        resultResponse = requests.post(url=urlPostClassification, params=paramsList, data=jsonData, auth=self.getAuth(), headers=self.getHeaders())
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (self.__getResultResponse())
    
    """
               Método para encontrar o id interno do glossário(guid).

               Parâmetros:
                    glossaryName: nome do glossário de dados. Tipo: string.
                    
                Retorno: 
                    Tipo: string                    
    """
    def getGlossaryGuid(self, glossaryName):
        urlGetGlossary = self.getUrl()+'/glossary'
        resultResponse = requests.get(url=urlGetGlossary, auth=self.getAuth(), headers=self.getHeaders())
        jsonResult = json.loads(resultResponse.text)
        glossaryGuid=''
        pos=0
        while (pos < len(jsonResult)):
            if(jsonResult[pos]['name']==glossaryName):
                glossaryGuid = jsonResult[pos].get('guid')
                pos = len(jsonResult)
                
            pos=pos+1
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (glossaryGuid)

    """
                   Método para criar os dados no glossário de dados.

                   Parâmetros:
                        listTerms: Lista de termos. Tipo: DictReader
                        dataDefColName: Nome da coluna no glossário em que está definido o nome do dado. Tipo: string.
                        glossaryGuid: identificador interno do glossário no Apache Atlas. Tipo: string.
    """
    def createGlossaryTerms (self, listTerms, dataDefColName, glossaryName):
        urlPostGlossaryTerms = self.getUrl() + '/glossary/terms'
        glossaryGuid = self.getGlossaryGuid(Funcoes.remover_acentos(glossaryName))
        listResulTerms = self.__createTerms(listTerms, Funcoes.remover_acentos(dataDefColName), glossaryGuid)
        jsonData = '[' + listResulTerms[0:(len(listResulTerms)-1)] + ']'
        resultResponse = requests.post(url=urlPostGlossaryTerms, data=jsonData, auth=self.getAuth(), headers=self.getHeaders())
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (self.__getResultResponse())

    """
                   Método para encontrar os identificadores (guid) dos dados criados no glossário.

                   Parâmetros:
                        glossaryName: nome do glossário no Apache Atlas. Tipo: string.
                    
                    Retorno:
                        Tipo: dictionary
    """
    def __getTermsGuid(self, glossaryName):
        glossaryGuid = self.getGlossaryGuid(glossaryName)
        urlGetGlossaryTerms = self.getUrl()+'/glossary/'+glossaryGuid+'/terms'        
        resultResponse = requests.get(url=urlGetGlossaryTerms, auth=self.getAuth(), headers=self.getHeaders())
        jsonResult = json.loads(resultResponse.text)
        listTermsGuid='{'
        for pos in jsonResult:
            listTermsGuid = listTermsGuid + '"'+pos.get('name')+'":"'+pos.get('guid')+'",'
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (listTermsGuid[0:(len(listTermsGuid)-1)]+'}')

    """
                   Método para encontrar os metadados (atributos) criados na classificação.

                   Parâmetros:
                        classificationName: nome da classificação no Apache Atlas. Tipo: string.
                    
                    Retorno:
                        Tipo: list
    """
    def __getAttributesClassification(self, classificationName):
        urlGetAttributesClass = self.getUrl()+'/types/classificationdef/name/'+classificationName
        resultResponse = requests.get(url=urlGetAttributesClass, auth=self.getAuth(), headers=self.getHeaders())
        jsonResult = json.loads(resultResponse.text)
        listAttributes=[]
        for pos in jsonResult['attributeDefs']:
            listAttributes.append(pos.get('name'))
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (listAttributes)

    """
                   Método para encontrar os dados e seus metadados e associá-los à classificação.

                   Parâmetros:
                        glossaryName: nome do glossário no Apache Atlas. Tipo: string.
                        dataDefColName: nome da coluna no arquivo CSV correspondente aos dados. Tipo: string.
                        classificationName: nome da classificação associada ao glossário no Apache Atlas. Tipo: string.
                        attributes: arquivo com os dados que compõem o glossário. Tipo: string.
                    Retorno:
                        Tipo: DictReader
    """
    def __getPairAttributeValue (self, glossaryName, dataDefColName, classificationName, attributes):
        listAttributes = self.__getAttributesClassification(classificationName)
        #dicionario termos par nome:guid
        dictTerms = self.__getTermsGuid(glossaryName)
        jsonPairTermGuid = json.loads(dictTerms)
        dictPairTermAttributes= '{'
        guidTerm = ''
        attributeFormated=''
        dataFormated=''
        for pos in attributes:
            posList=0
            attributeFormated = Funcoes.remover_acentos(listAttributes[posList])
            if(attributeFormated==dataDefColName):
                dataFormated = Funcoes.remover_acentos(pos[attributeFormated])
                guidTerm = jsonPairTermGuid[dataFormated]
            dictPairTermAttributes = dictPairTermAttributes + '"'+guidTerm+'": [{'
            while (posList < len(listAttributes)):
                attributeFormated = Funcoes.remover_acentos(listAttributes[posList])
                dataFormated = Funcoes.remover_acentos(pos[attributeFormated])
                dictPairTermAttributes = dictPairTermAttributes +'"'+attributeFormated+'":"'+dataFormated+'",'
                posList = posList + 1
            dictPairTermAttributes = dictPairTermAttributes[0:(len(dictPairTermAttributes)-1)] + '}],'
        return (dictPairTermAttributes[0:(len(dictPairTermAttributes)-1)]+'}')
                
    """
                   Método para associar a classificação com os metadados aos dados adicionados no glossário.

                   Parâmetros:
                        glossaryName: nome do glossário no Apache Atlas. Tipo: string.
                        dataDefColName: nome da coluna no arquivo CSV correspondente aos dados. Tipo: string.
                        classificationName: nome da classificação associada ao glossário no Apache Atlas. Tipo: string.
                        attributes: arquivo com os dados que compõem o glossário. Tipo: DictReader.
    """
    def createGlossaryTermsAssociation (self, glossaryName, dataDefColName, classificationName, attributes):
        urlPostGlossaryTermsAssociation = self.getUrl() + '/entity/bulk/classification'
        dictPairAttributeValue = self.__getPairAttributeValue(Funcoes.remover_acentos(glossaryName), Funcoes.remover_acentos(dataDefColName), Funcoes.remover_acentos(classificationName), attributes)
        jsonDictPairAttributeValue = json.loads(dictPairAttributeValue)
        #jsonDictPairAttributeValue = json.loads(json.dumps(dictPairAttributeValue))
        jsonData = ""
        resultResponse = {}
        statusCode = {}
        for pos in jsonDictPairAttributeValue:
            jsonData = '{"classification":{\
            "typeName":"'+Funcoes.remover_acentos(classificationName)+'",\
            "attributes":'+str(jsonDictPairAttributeValue[pos][0]).replace('\'','"')+'},\
            "entityGuids":["'+pos+'"]\
            }'
            resultResponse[jsonDictPairAttributeValue[pos][0][Funcoes.remover_acentos(dataDefColName)]] = requests.post(url=urlPostGlossaryTermsAssociation, data=jsonData, auth=self.getAuth(), headers=self.getHeaders())
            statusCode[jsonDictPairAttributeValue[pos][0][Funcoes.remover_acentos(dataDefColName)]] = resultResponse[jsonDictPairAttributeValue[pos][0][Funcoes.remover_acentos(dataDefColName)]].status_code
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)
        return (self.__getResultResponse())