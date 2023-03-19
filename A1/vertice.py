class Vertice:
    def __init__(self, identidade, rotulo):
        self.__identidade = identidade
        self.__rotulo = rotulo
    

    @property
    def identidade(self):
        return self.__identidade

    @property
    def getRotulo(self):
        return self.__rotulo