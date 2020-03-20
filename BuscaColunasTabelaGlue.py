import boto3
import argparse
import json
import time
import os.path

"""
parser = argparse.ArgumentParser(description='Script para encontrar os campos de uma tabela no AWS Glue Data Catalog.')
parser.add_argument("--tb", default=1, help="Tabela do AWS Glue Data Catalog.")
parser.add_argument("--db", default=1, help="Database onde está a tabela no AWS Glue Data Catalog.")
parser.add_argument("--key", default=1, help="AWS Access Key usada para inicar a sessão.")
parser.add_argument("--saKey", default=1, help="AWS Secret Access Key usada para inicar a sessão.")
parser.add_argument("--reg", default=1, help="Região da AWS do onde o banco de dados do Athena está configurado.")
"""
"""
args = parser.parse_args()
tabela = args.tb
dataBase = args.db
AWS_ACCESS_KEY_ID = args.key
AWS_SECRET_ACCESS_KEY = args.saKey
AWS_DEFAULT_REGION = args.reg
"""

tabela = "faturas_pf"
dataBase = "axxiom"
AWS_ACCESS_KEY_ID = "AKIA5XU3ATPDZKQJ77HP"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_REGION = "us-east-1"

client = boto3.client('glue',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_DEFAULT_REGION)


result=client.get_table(DatabaseName=dataBase, Name=tabela)

listCampos = []

listCampos = result["Table"]["StorageDescriptor"]["Columns"]

