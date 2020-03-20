# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:08:57 2019

@author: tiago.santos
"""
import csv
from FuncoesCargaGlossario import *
from ConexaoSSH import ConexaoSSH

hostname='192.168.46.135'
port='22'
username='root'
password='cenhaPadra0'
guidGlossario = 'aeaf31e0-db73-446c-b329-1ac589a5f15a'
 
arquivoCSV = csv.DictReader (open ("C:\Tiago\Apache_Atlas\GlossarioNegocio.csv"))

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

#retorno do comando
#[{"guid":"e37b85d7-3a51-4de7-8b30-0854969cccd8","qualifiedName":"CD_CLIENTE@Gloss\xc3\xa1rio P&D D-580","name":"CD_CLIENTE","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"fdabdb5b-f25c-4cb3-bac8-a83b18d7d193"}},{"guid":"759f1c72-c55c-48ce-8e73-ca08b68a93a7","qualifiedName":"NR_CPF@Gloss\xc3\xa1rio P&D D-580","name":"NR_CPF","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"01156a00-21d3-4ca1-984c-bd240e9186ae"}},{"guid":"349c34ac-bde9-48f0-aa22-042ab6865c8a","qualifiedName":"NM_NOME@Gloss\xc3\xa1rio P&D D-580","name":"NM_NOME","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"7e65ca6c-a1d1-4acc-8c48-2be759bba323"}},{"guid":"73d1a6a3-7312-457a-a8b4-c817a8f87e89","qualifiedName":"NR_IDADE@Gloss\xc3\xa1rio P&D D-580","name":"NR_IDADE","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"cc18c597-51bd-4054-aaca-6895244bdfa9"}},{"guid":"6e396501-c9d1-41ac-8325-bf76d1082544","qualifiedName":"DT_NASCIMENTO@Gloss\xc3\xa1rio P&D D-580","name":"DT_NASCIMENTO","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"392df336-8adb-4775-bac2-1eaa6a292773"}},{"guid":"a219045b-773c-4271-8490-add609c0783a","qualifiedName":"DS_ETNIA@Gloss\xc3\xa1rio P&D D-580","name":"DS_ETNIA","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"d438bcf9-422d-4d53-92aa-843b7062d83f"}},{"guid":"d37de998-4665-4385-ab0e-a2609e4a8486","qualifiedName":"DS_RELIGIAO@Gloss\xc3\xa1rio P&D D-580","name":"DS_RELIGIAO","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"01ba7425-a53f-4b22-8f4c-f277f80858eb"}},{"guid":"a2036441-cc9e-4475-b1a0-937b2de336b9","qualifiedName":"DS_SEXO@Gloss\xc3\xa1rio P&D D-580","name":"DS_SEXO","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"2f8c08b8-430c-409c-a389-6eeef22bfc21"}},{"guid":"af963a3a-f749-4d46-8249-ea02f0bb1a65","qualifiedName":"DS_ESTADO_CIVIL@Gloss\xc3\xa1rio P&D D-580","name":"DS_ESTADO_CIVIL","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"63d8d3e8-9aae-4eee-9149-742eece38cc9"}},{"guid":"209a6db4-4189-456a-994c-f333ac514378","qualifiedName":"DS_NACIONALIDADE@Gloss\xc3\xa1rio P&D D-580","name":"DS_NACIONALIDADE","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"08860e17-9b57-40b6-afe0-23f7f9cd13ae"}},{"guid":"d4adfcb5-fd4f-4b9b-b8e2-7c4325021953","qualifiedName":"DS_NATURALIDADE@Gloss\xc3\xa1rio P&D D-580","name":"DS_NATURALIDADE","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"e336bcc0-2232-4704-be8b-17a65ccf3b0c"}},{"guid":"769b2972-4860-4ad1-9ef5-afe516045041","qualifiedName":"DS_LOGRADOURO@Gloss\xc3\xa1rio P&D D-580","name":"DS_LOGRADOURO","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"bc740ca0-82e0-49e2-a5cd-170a074b322b"}},{"guid":"09391597-53ba-400b-94ee-cd792d0270d6","qualifiedName":"DS_CIDADE@Gloss\xc3\xa1rio P&D D-580","name":"DS_CIDADE","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"5597634b-1808-4ca5-9d75-afdf65e21e46"}},{"guid":"f423e762-0e85-4f66-83c0-75f18629d945","qualifiedName":"DS_UF@Gloss\xc3\xa1rio P&D D-580","name":"DS_UF","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"3f3d0959-7fe0-4fbf-b9e8-14f1d40d0830"}},{"guid":"5203df95-c561-4687-960d-c890de7cdc84","qualifiedName":"NR_CEP@Gloss\xc3\xa1rio P&D D-580","name":"NR_CEP","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"8ace4f1f-902b-470b-898c-a58cd5b0e367"}},{"guid":"13f251a1-8b7c-4e89-aedf-5ad8b1ce1b45","qualifiedName":"CD_UND_CONSUMIDORA@Gloss\xc3\xa1rio P&D D-580","name":"CD_UND_CONSUMIDORA","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"25a7efdd-f75c-4e25-956a-777bd2e95811"}},{"guid":"095e3d76-9d66-46d7-a441-54f6e50c64fb","qualifiedName":"CD_FATURA@Gloss\xc3\xa1rio P&D D-580","name":"CD_FATURA","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"7db2d7e0-5dfa-4d64-88ce-7e5ea5219a81"}},{"guid":"ddfc8178-1177-453d-9671-d9aae1bf4285","qualifiedName":"DT_VENCIMENTO@Gloss\xc3\xa1rio P&D D-580","name":"DT_VENCIMENTO","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"2431a725-63b4-4e02-9398-9a9ed348cf2e"}},{"guid":"2012c75f-300a-4383-b678-0edcb9dfba48","qualifiedName":"DT_PAGAMENTO@Gloss\xc3\xa1rio P&D D-580","name":"DT_PAGAMENTO","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"0f9974fb-427e-47f1-b61f-155a21e9e971"}},{"guid":"f77f50fa-644e-4898-97a0-a58e25643788","qualifiedName":"DT_LEITURA@Gloss\xc3\xa1rio P&D D-580","name":"DT_LEITURA","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"8d0b79a2-3e4a-4894-a566-4ffe962e6330"}},{"guid":"96f1a546-2df2-4b67-9ab8-36a1b09f059c","qualifiedName":"VR_FATURA@Gloss\xc3\xa1rio P&D D-580","name":"VR_FATURA","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"66fbe507-bc7a-4673-bd65-0fbeb3f71230"}},{"guid":"536618c5-a3d2-4d00-b13f-612839328482","qualifiedName":"QT_CONSUMO_KWh@Gloss\xc3\xa1rio P&D D-580","name":"QT_CONSUMO_KWh","anchor":{"glossaryGuid":"aeaf31e0-db73-446c-b329-1ac589a5f15a","relationGuid":"829273e4-f7b3-4cf0-bd34-689ae59d55b8"}}]'

