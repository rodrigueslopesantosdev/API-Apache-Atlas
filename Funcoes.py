from unicodedata import normalize
import pandas as pd
import re

class Funcoes:

    def __init__(self):
        self.resultado=''

    @staticmethod
    def removerAcentos(texto):
        return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

    @staticmethod
    def criarAlfabetoUnicode():
        alfabeto = {}
        letrasTabela = ['A', 'B', 'C', 'D', 'E', 'F']
        # Constroi o escape sequence dos caracteres especiais com \u00A0 .... \u00F9
        pos2 = 0
        contador = 0
        incrInicio = 16
        inicio = 160
        incrFim = 10
        while (contador < 6):
            for pos in range(inicio, (inicio + incrFim)):
                alfabeto[chr(pos)] = '\\u00' + str(letrasTabela[contador]) + str(pos2)
                pos2 = pos2 + 1
            pos2 = 0
            inicio = inicio + incrInicio
            contador = contador + 1

        # Constroi o escape sequence dos caracteres especiais com \u000A .... \u009F
        pos2 = 0
        contador = 0
        incrInicio = 16
        inicio = 10
        incrFim = 6
        while (contador < 10):
            for pos in range(inicio, (inicio + incrFim)):
                alfabeto[chr(pos)] = '\\u00' + str(contador) + str(letrasTabela[pos2])
                pos2 = pos2 + 1
            pos2 = 0
            inicio = inicio + incrInicio
            contador = contador + 1

        # Constroi o escape sequence dos caracteres especiais com \u0000 .... \u0099
        pos2 = 0
        contador = 0
        incrInicio = 16
        inicio = 0
        incrFim = 10
        while (contador < 10):
            for pos in range(inicio, (inicio + incrFim)):
                if pos <= 9:
                    alfabeto[chr(pos)] = '\\u000' + str(pos2)
                else:
                    alfabeto[chr(pos)] = '\\u00' + str((incrFim * contador) + pos2)
                pos2 = pos2 + 1
            pos2 = 0
            inicio = inicio + incrInicio
            contador = contador + 1

        # Constroi o escape sequence dos caracteres especiais com \u00AA .... \u00FF
        pos2 = 0
        incrInicio = 16
        inicio = 170
        incrFim = 6
        letras = 0
        while letras < len(letrasTabela):
            for pos in range(inicio, (inicio + incrFim)):
                alfabeto[chr(pos)] = '\\u00' + str(letrasTabela[letras]) + str(letrasTabela[pos2])
                pos2 = pos2 + 1
            pos2 = 0
            letras = letras + 1
            inicio = inicio + incrInicio

        return (alfabeto)

    @staticmethod
    def replaceSequenceEscape(frase, alfabetoUnicode):
        fraseAlterada=frase
        for letra in fraseAlterada:
            '''if (letra == 'á' or letra == 'à' or letra == 'â' or letra == 'ã' or letra == 'é'
                    or letra == 'è' or letra == 'ê' or letra == 'í' or letra == 'ì' or letra == 'î' or letra == 'ó' or letra == 'ò' or letra == 'ô' or letra == 'õ'
                    or letra == 'ç' or letra == '(' or letra == ')'):'''
            if(re.search(r'[^a-zA-Z0-9 ]', letra)):
                fraseAlterada = fraseAlterada.replace(letra, alfabetoUnicode[letra])

        return fraseAlterada


