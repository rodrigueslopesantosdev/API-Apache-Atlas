from unicodedata import normalize

class Funcoes:

    def __init__(self):
        self.resultado=''

    #Função estática que retira os acentos das letras.
    #Referência da função: https://wiki.python.org.br/RemovedorDeAcentos
    @staticmethod
    def remover_acentos(texto):
        return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')