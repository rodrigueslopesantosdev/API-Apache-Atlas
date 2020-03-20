import pandas as pd
from Funcoes import Funcoes

alfabeto = Funcoes.criarAlfabetoUnicode()

frase = 'Márcio'
teste = Funcoes.replaceSequenceEscape(frase, alfabeto)
print(teste)