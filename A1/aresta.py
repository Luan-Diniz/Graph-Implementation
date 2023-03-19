class Aresta:
    def __init__(self, vertice1, vertice2, peso):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__peso = peso
    
    @property
    def getPeso(self):
        return self.__peso
    
    def retornaVertices(self):
        return (self.__vertice1, self.__vertice2)
    

