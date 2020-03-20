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
import pandas as pd
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
                    alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                    correspondente a chave.
    """
    def __createAttributes(self, attributes, alfabeto):
        listAttributes=''
        stringAtributte=''
        for pos in attributes.fieldnames:
            stringAtributte = Funcoes.replaceSequenceEscape(pos, alfabeto)
            if (stringAtributte != Funcoes.replaceSequenceEscape('n. sequencial', alfabeto)):
                listAttributes = listAttributes + '{"name":"'+stringAtributte+'","typeName":"string"},'
            
        return listAttributes

    """
               Método para criar os dados do glossário de dados.

               Parâmetros:
                    listTerms: Lista de termos. Tipo: DictReader
                    dataDefColName: Nome da coluna no glossário em que está definido o nome do dado
                    glossaryGuid: identificador interno do glossário no Apache Atlas.
                    alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                    correspondente a chave.
    """
    def createTerms(self, listTerms, dataDefColName, glossaryGuid, alfabeto):
        listResultTerms=''
        for pos in listTerms:
            if(pd.isnull(pos[dataDefColName])!= True):
                listResultTerms = listResultTerms + '{"name":"'+Funcoes.replaceSequenceEscape(str(pos[dataDefColName]), alfabeto)+'", "shortDescription":"", "longDescription":"", "anchor":{"glossaryGuid":"' + glossaryGuid + '"}},'
        return listResultTerms

    """
               Método para criar os dados do glossário de dados.

               Parâmetros:
                    listTerms: Lista de termos. Tipo: DictReader
                    dataDefColName: Nome da coluna no glossário em que está definido o nome do dado
                    glossaryGuid: identificador interno do glossário no Apache Atlas.
                    alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                    correspondente a chave.
    """
    def createTerm(self, termo, dataDefColName, glossaryGuid, alfabeto):
        listResultTerm=''
        if (pd.isnull(termo[dataDefColName]) != True):
            listResultTerm = listResultTerm + '{"name":"'+Funcoes.replaceSequenceEscape(str(termo[dataDefColName]), alfabeto)+'", "shortDescription":"", "longDescription":"", "anchor":{"glossaryGuid":"' + glossaryGuid + '"}},'
        return listResultTerm

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
                    alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                    correspondente a chave. Tipo: Dict
    """
    def createClassification (self, classificationName, classDescription, attributes, alfabeto):
        urlPostClassification = self.getUrl() + '/types/typedefs'
        paramsList= {'type':'classification'}
        jsonData = '{"classificationDefs":[{"name":"'+Funcoes.replaceSequenceEscape(classificationName, alfabeto)+'","description":"'\
                   +Funcoes.replaceSequenceEscape(classDescription, alfabeto)+'","superTypes":[],"attributeDefs":['
        listAttirbutes = self.__createAttributes(attributes, alfabeto)
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
            pos = pos+1
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
        glossaryGuid = self.getGlossaryGuid(glossaryName)
        listResulTerms = listTerms
        jsonData = '[' + listResulTerms[0:(len(listResulTerms) - 1)] + ']'
        resultResponse = requests.post(url=urlPostGlossaryTerms, data=jsonData, auth=self.getAuth(), headers=self.getHeaders())
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (self.__getResultResponse())

    """
                   Método para criar os dados no glossário de dados.

                   Parâmetros:
                        listTerms: Lista de termos. Tipo: DictReader
                        dataDefColName: Nome da coluna no glossário em que está definido o nome do dado. Tipo: string.
                        glossaryGuid: identificador interno do glossário no Apache Atlas. Tipo: string.
                        alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                        correspondente a chave. Tipo: Dict.
    """
    def createGlossaryTerm (self, listTerms, dataDefColName, glossaryName, alfabeto):
        urlPostGlossaryTerms = self.getUrl() + '/glossary/term'
        glossaryGuid = self.getGlossaryGuid(glossaryName)
        listResulTerms = listTerms
        jsonData = listResulTerms[0:(len(listResulTerms) - 1)]
        resultResponse = requests.post(url=urlPostGlossaryTerms, data=jsonData, auth=self.getAuth(), headers=self.getHeaders())
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (self.__getResultResponse())


    """
                   Método para encontrar os identificadores (guid) dos dados criados no glossário.

                   Parâmetros:
                        glossaryName: nome do glossário no Apache Atlas. Tipo: string.
                        alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                        correspondente a chave. Tipo: Dict.
                         
                    Retorno:
                        Tipo: dictionary
    """
    def __getTermsGuid(self, glossaryName, alfabeto):
        glossaryGuid = self.getGlossaryGuid(glossaryName)
        urlGetGlossaryTerms = self.getUrl()+'/glossary/'+glossaryGuid+'/terms'        
        resultResponse = requests.get(url=urlGetGlossaryTerms, auth=self.getAuth(), headers=self.getHeaders())
        jsonResult = json.loads(resultResponse.text)
        listTermsGuid='{'
        for pos in jsonResult:
            listTermsGuid = listTermsGuid + '"'+Funcoes.replaceSequenceEscape(pos.get('name'), alfabeto)+'":"'+pos.get('guid')+'",'
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
                        alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                        correspondente a chave. Tipo: Dict.
                        
                    Retorno:
                        Tipo: DictReader
    """
    def __getPairAttributeValue (self, glossaryName, dataDefColName, classificationName, attributes, alfabeto):
        listAttributes = self.__getAttributesClassification(classificationName)
        print('getAttributesClassification() - CONCLUÍDO !!!')
        #dicionario termos par nome:guid
        dictTerms = self.__getTermsGuid(glossaryName, alfabeto)
        print('getTermsGuid() - CONCLUÍDO !!!')
        jsonPairTermGuid = json.loads(dictTerms)
        dictPairTermAttributes= '{'
        guidTerm = ''
        attributeFormated=''
        dataFormated=''
        for pos in attributes:
            posList=0
            attributeFormated = listAttributes[posList]
            if(attributeFormated==dataDefColName):
                dataFormated = pos[attributeFormated]
                guidTerm = jsonPairTermGuid[dataFormated]
            dictPairTermAttributes = dictPairTermAttributes + '"'+guidTerm+'": [{'
            while (posList < len(listAttributes)):
                attributeFormated = listAttributes[posList]
                dataFormated = pos[attributeFormated]
                dictPairTermAttributes = dictPairTermAttributes +'"'+Funcoes.replaceSequenceEscape(attributeFormated, alfabeto)+'":"'\
                                         +Funcoes.replaceSequenceEscape(dataFormated, alfabeto)+'",'
                posList = posList + 1
            dictPairTermAttributes = dictPairTermAttributes[0:(len(dictPairTermAttributes)-1)] + '}],'
        return (dictPairTermAttributes[0:(len(dictPairTermAttributes)-1)]+'}')

    """
                   Método para tratar os caracteres especiais dos valores dos metadados.

                   Parâmetros:
                        jsonDictPairAttributeValue: json contendo os metadados e seus valores, amobos com caracteres especiais.
                        alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                        correspondente a chave. Tipo: Dict.
                    Retorno:
                        Tipo: Dict
    """
    def __trataValorMetadado(self, jsonDictPairAttributeValue, alfabeto):
        listAtributes = "{"
        for chave in jsonDictPairAttributeValue:  # guid: [{chave:valor}]
            for chave2 in jsonDictPairAttributeValue[chave]:
                for pos in chave2:
                    listAtributes = listAtributes + '"' + Funcoes.replaceSequenceEscape(pos, alfabeto) + '"' + \
                                    ": " + '"' + Funcoes.replaceSequenceEscape(chave2[pos], alfabeto) + '",'
                jsonDictPairAttributeValue[chave][0] = listAtributes[0:(len(listAtributes) - 1)] + "}"
        return jsonDictPairAttributeValue

    """
                   Método para associar a classificação com os metadados aos dados adicionados no glossário.

                   Parâmetros:
                        glossaryName: nome do glossário no Apache Atlas. Tipo: string.
                        dataDefColName: nome da coluna no arquivo CSV correspondente aos dados. Tipo: string.
                        classificationName: nome da classificação associada ao glossário no Apache Atlas. Tipo: string.
                        attributes: arquivo com os dados que compõem o glossário. Tipo: DictReader.
                        alfabeto: dicionário contendo chave = caracter Unicode e valor = Unicode Escape Sequence 
                        correspondente a chave. Tipo: Dict.
    """
    def createGlossaryTermsAssociation (self, glossaryName, dataDefColName, classificationName, attributes, alfabeto):
        urlPostGlossaryTermsAssociation = self.getUrl() + '/entity/bulk/classification'
        dictPairAttributeValue = self.__getPairAttributeValue(glossaryName,
                                                              dataDefColName,
                                                              classificationName,
                                                              attributes,
                                                              alfabeto)
        print('getPairAttributeValue() - CONCLUÍDO !!!')
        jsonDictPairAttributeValue = json.loads(dictPairAttributeValue)
        jsonDictPairAttributeValueTratado = self.__trataValorMetadado(jsonDictPairAttributeValue, alfabeto)
        jsonData = ""
        responseRequest=""
        statusCodeRequest=""
        resultResponse = {}
        statusCode = {}
        for pos in jsonDictPairAttributeValueTratado:
            jsonData = '{"classification":{\
                        "typeName":"' + classificationName + '",\
                        "attributes":' + str(jsonDictPairAttributeValueTratado[pos][0])+ '},\
                        "entityGuids":["' + pos + '"]\
                        }'
            responseRequest = requests.post(url=urlPostGlossaryTermsAssociation, data=jsonData,
                                            auth=self.getAuth(), headers=self.getHeaders())
            resultResponse[json.loads(jsonDictPairAttributeValueTratado[pos][0])[dataDefColName]] = \
                str(responseRequest.text)
            statusCode[json.loads(jsonDictPairAttributeValueTratado[pos][0])[dataDefColName]] = \
                resultResponse[json.loads(jsonDictPairAttributeValueTratado[pos][0])[dataDefColName]].status_code

        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)
        return (self.__getResultResponse())


    """
                   Método para buscar os termos de um glossário.

                   Parâmetros:
                        listTerms: Lista de termos. Tipo: DictReader
                        dataDefColName: Nome da coluna no glossário em que está definido o nome do dado. Tipo: string.
                        glossaryGuid: identificador interno do glossário no Apache Atlas. Tipo: string.
    """
    def __getGlossaryTerms (self, glossaryName):
        glossaryGuid = self.getGlossaryGuid(Funcoes.remover_acentos(glossaryName))
        urlGetGlossaryTerms = self.getUrl() + '/glossary/' + glossaryGuid + '/terms'
        resultResponse = requests.get(url=urlGetGlossaryTerms, auth=self.getAuth(), headers=self.getHeaders())
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(self.resultResponse.status_code)
        return (self.__getResultResponse())


    """
                   Método para associar a classificação a um dado do glossário.

                   Parâmetros:
                        glossaryName: nome do glossário no Apache Atlas. Tipo: string.
                        dataDefColName: nome da coluna no arquivo CSV correspondente aos dados. Tipo: string.
                        classificationName: nome da classificação associada ao glossário no Apache Atlas. Tipo: string.
                        attributes: arquivo com os dados que compõem o glossário. Tipo: DictReader.
    """
    def createGlossaryTermAssociation (self, classificationName, attributes, guidDataGlossary):
        urlPostGlossaryTermsAssociation = self.getUrl() + '/entity/bulk/classification'
        jsonData = '{"classification":{\
        "typeName":"'+Funcoes.remover_acentos(classificationName)+'",\
        "attributes": {'+attributes+'}},'\
        '"entityGuids":["'+guidDataGlossary+'"]}'
        resultResponse = requests.post(url=urlPostGlossaryTermsAssociation, data=jsonData, auth=self.getAuth(), headers=self.getHeaders())
        statusCode = resultResponse.status_code
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)


    """
                   Método para fazer a busca dos termos técnicos importados para o Apache Atlas através do endpoint
                   /v2/search/basic da API Apache Atlas.

                   Parâmetros:
                       nomeTermoTecnico: nome do termo técnico para ser buscado dentro do Apache Atlas. Tipo: string.
                       
                   Retorno:
                       jsonResult: retorno da busca nos formatos do retorno do endpoint /search/basic da API Apache Atlas. 
                                             
    """
    def searchBasicTermosTecnicos(self, nomeTermoTecnico):
        urlPostSearchBasic = self.getUrl() + '/search/basic'
        jsonData = '{"' \
                   'excludeDeletedEntities":true, ' \
                   '"includeSubClassifications":true, ' \
                   '"includeSubTypes":true, ' \
                   '"includeClassificationAttributes":true,' \
                   '"entityFilters":null, ' \
                   '"tagFilters":null, ' \
                   '"attributes":[], ' \
                   '"query":"'+nomeTermoTecnico+'", ' \
                   '"limit":25, ' \
                   '"offset":0, ' \
                   '"typeName":"hive_column", ' \
                   '"classification":null, ' \
                   '"termName":null ' \
                   '}'
        resultResponse = requests.post(url=urlPostSearchBasic, data=jsonData, auth=self.getAuth(),
                                       headers=self.getHeaders())
        statusCode = resultResponse.status_code
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)
        jsonResult = json.loads(self.__getResultResponse().text)
        return (jsonResult)


    """
                   Método para encontrar o guid dos termos tecnicos encontrados armazenados no Json 
                   de retorno do método searchBasicTermosTecnicos. Os parâmetros são referentes ao banco Hive e a tabela 
                   Hive, pois na arquitetura centralizamos a integração do Apache Atlas através do metastore do Apache Hive.

                   Parâmetros:
                       nomeBancoHive: Nome do banco de dados do Hive onde se encontra a tabela que deseja-se 
                       tagear com as marcações de zonas lógicas. Tipo: string.
                       
                       nomeTabelaHive: nome da tabela do Hive onde são encontrados os campos que serão tageados 
                       com a marcação lógica das zonas. Tipo: string.
                       
                       resultadoBuscaCampo: resultado da busca do campo retornada pelo Apache Atlas. 
                        
                   Retorno:
                       listGuidsTermosTecnicos: lista de guids para cada campo da tabela identificada pelos parâmetros 
                       nomeBancoHive e nomeTabelaHive
                                             
    """
    def getGuidTermosTecnicos(self, nomeBancoHive, nomeTabelaHive, resultadoBuscaCampo):
        qualifiedName = ""
        listGuidsTermosTecnicos = list()
        tamPalavraBanco = len(nomeBancoHive)
        tamPalavraTabela = len(nomeTabelaHive)
        for pos in resultadoBuscaCampo:
            if pos["typeName"] == "hive_column":
                qualifiedName = pos["attributes"]["qualifiedName"]
                #Com a primeira posição de cada palavra (palavraBancoEncontrada e palavraTabelaEncontrada) é possível buscar
                #dentro do qualifiedName o banco e a tabela analisada no laço de loop.
                palavraBancoEncontrada = qualifiedName[0:tamPalavraBanco]
                palavraTabelaEncontrada = qualifiedName[(tamPalavraBanco + 1):(tamPalavraBanco + 1) + tamPalavraTabela]
                #If para verificar se o campo encontrado hive_column pertence ao banco de dados correto
                if palavraBancoEncontrada == nomeBancoHive and palavraTabelaEncontrada == nomeTabelaHive:
                    listGuidsTermosTecnicos.append(pos["guid"])
        #retorno da funcao.
        return listGuidsTermosTecnicos


    """
                      Método para encontrar o guid dos termos tecnicos encontrados no Json 
                      de retorno do método searchBasicTermosTecnicos. Os parâmetros são referentes ao banco Hive e a tabela 
                      Hive, pois na arquitetura foi centralizado a integração do Apache Atlas através 
                      do metastore do Apache Hive.

                      Parâmetros:
                          nomeBancoHive: Nome do banco de dados do Hive onde se encontra a tabela que deseja-se 
                          tagear com as marcações de zonas lógicas. Tipo: string.

                          nomeTabelaHive: nome da tabela do Hive onde são encontrados os campos que serão tageados 
                          com a marcação lógica das zonas. Tipo: string.

                          resultadoBuscaCampo: resultado da busca do campo retornada pelo Apache Atlas.  

                      Retorno:
                          guidTermoTecnico: guids do campo da tabela identificada pelos parâmetros 
                          nomeBancoHive, nomeTabelaHive e resultadoBuscaCampo

       """

    def getGuidTermoTecnicoUnitario(self, nomeBancoHive, nomeTabelaHive, resultadoBuscaCampo):
        qualifiedName = ""
        guidTermoTecnico = None
        tamPalavraBanco = len(nomeBancoHive)
        tamPalavraTabela = len(nomeTabelaHive)
        for pos in resultadoBuscaCampo:
            if pos["typeName"] == "hive_column":
                qualifiedName = pos["attributes"]["qualifiedName"]
                # Com a primeira posição de cada palavra (palavraBancoEncontrada e palavraTabelaEncontrada) é possível buscar
                # dentro do qualifiedName o banco e a tabela analisada no laço de loop.
                palavraBancoEncontrada = qualifiedName[0:tamPalavraBanco]
                palavraTabelaEncontrada = qualifiedName[(tamPalavraBanco+1):(tamPalavraBanco+1) + tamPalavraTabela]
                # If para verificar se o campo encontrado hive_column pertence ao banco de dados correto
                if palavraBancoEncontrada == nomeBancoHive and palavraTabelaEncontrada == nomeTabelaHive:
                    guidTermoTecnico = pos["guid"]
                    # retorno da funcao.
                    return guidTermoTecnico

    """
                   Método para associar uma classificação de tageamento de zonas ao termo técnico proveniente de colunas 
                   do Hive (hive_column).

                   Parâmetros:
                       classificationName: nome da classificação que será associada ao termo técnico (hive_column). Tipo: string.
                       
                       attributeDefinition: descrição da definição da zona. Tipo: string.
                       
                       guidTermoTecnico: guid do termo técnico encontrado através do método searchBasicTermosTecnicos. Tipo: string.
    """
    def createTermosTecnicosClassificacaoAssociation (self, classificationName, breveDescricao, localizacaoDataLake, guidTermoTecnico):
        urlPostGlossaryTermsAssociation = self.getUrl() + '/entity/bulk/classification'
        jsonData = '{"classification":{\
        "typeName":"'+Funcoes.remover_acentos(classificationName)+'",\
        "attributes":{"Descricao":"'+breveDescricao+'", \
                                                         "Localizacao":"'+localizacaoDataLake+'"},\
        "propagate":true,\
        "validityPeriods":[]}, \
        "entityGuids":["'+guidTermoTecnico+'"] \
        }'
        resultResponse = requests.post(url=urlPostGlossaryTermsAssociation, data=jsonData, auth=self.getAuth(),
                                       headers=self.getHeaders())
        statusCode = resultResponse.status_code
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)
        return (self.__getResultResponse().text)

    """
                    Método para associar uma classificação de tageamento de zonas ao termo técnico proveniente de colunas 
                    do Hive (hive_column).

                    Parâmetros:
                        classificationName: nome da classificação que será associada ao termo técnico (hive_column). Tipo: string.

                        attributeDefinition: descrição da definição da zona. Tipo: string.

                        guidTermoTecnico: guid do termo técnico encontrado através do método searchBasicTermosTecnicos. Tipo: string.
    """
    def createTermosTecnicosClassificacaoAssociationZonaCrua(self, classificationName, dataGovernado, localOrigemDado, localDestinoDado,
                                                             nomeArquivoFisico, guidTermoTecnico):
        urlPostGlossaryTermsAssociation = self.getUrl() + '/entity/bulk/classification'
        jsonData = '{"classification":{\
         "typeName":"' + Funcoes.remover_acentos(classificationName) + '",\
         "attributes":{"Data que foi governado":"' + dataGovernado + \
                   '", "Local de origem do dado":"' + localOrigemDado + \
                   '", "Local de destino do dado":"'+ localDestinoDado +\
                   '", "Nome do arquivo fisico no destino":"'+nomeArquivoFisico+'"},\
         "propagate":true,\
         "validityPeriods":[]}, \
         "entityGuids":["' + guidTermoTecnico + '"] \
         }'

        resultResponse = requests.post(url=urlPostGlossaryTermsAssociation, data=jsonData, auth=self.getAuth(),
                                       headers=self.getHeaders())
        statusCode = resultResponse.status_code
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)
        return (self.__getResultResponse().text)


    """
                Método para fazer a busca das propriedades do dado técnico governado e tagueado na Zona Crua 
                no Apache Atlas. Esse método implementa o endpoint /v2/entity/{guid}/audit da API do Apache Atlas.

                Parâmetros:
                    guidDadoTecnico: valor do guid que correspondente ao termo técnico já governado e tagueado para 
                    a Zona Crua. Tipo: guid.

                Retorno:
                    jsonResult: retorno da busca nos formatos do retorno do endpoint /v2/entity/{guid}/audit da API Apache Atlas. 
    """
    def getPropriedadesDadoZonaCrua(self, guidDadoTecnico):
        urlPostGlossaryTermsAssociation = self.getUrl() + '/entity/'+guidDadoTecnico+'/audit'
        resultResponse = requests.get(url=urlPostGlossaryTermsAssociation, auth=self.getAuth(), headers=self.getHeaders())
        statusCode = resultResponse.status_code
        self.__setResultResponse(resultResponse)
        self.__setStatusCode(statusCode)
        return (self.__getResultResponse().text)


    """
        
    """
    def encontraAtributosClassificacaoZona(self, resultadoBuscaPropriedades, nomeZona):
        for pos in resultadoBuscaPropriedades:
            if pos['action'] == 'CLASSIFICATION_ADD':
                tamPos = pos['details'].find('{')
                tamTotal = len(pos['details'])
                jsonLoads = json.loads(pos['details'][tamPos:tamTotal])
                if(jsonLoads['typeName'] == nomeZona):
                    return (jsonLoads['attributes'])
