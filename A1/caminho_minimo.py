from grafo import Grafo
from util import Util

class CaminhoMinimo:
    @staticmethod
    def buscar(nome_arquivo: str, s: int):
        grafo = Grafo(nome_arquivo)
        (funcionou, distancia, antecessor) = CaminhoMinimo.BellmanFord(grafo, s)
        if funcionou != True:
            print("BellmanFord failed!")
        else:

            for i in range(1, grafo.qtdVertices() + 1):
                print(f"{i}: {CaminhoMinimo.getPath(antecessor, (s,i))}; d={Util.convert_float(distancia[i-1])}")             

    @staticmethod
    def BellmanFord(grafo: Grafo, s: int) -> tuple:
        distancia = [float('inf') for i in range(grafo.qtdVertices())]
        antecessor = [None for i in range(grafo.qtdVertices())]

        distancia[s - 1] = 0

        for _ in range(1, grafo.qtdVertices() - 1):
            for u,v in grafo.getArestas():
                #relaxamento
                if distancia[v-1] > distancia[u-1] + grafo.peso(u,v):
                    distancia[v-1] = distancia[u-1] + grafo.peso(u,v)
                    antecessor[v-1] = u

        #verifica se ha ciclo negativo
        for _ in range(1, grafo.qtdVertices() - 1):
            for u,v in grafo.getArestas():
                if distancia[v-1] > distancia[u-1] + grafo.peso(u,v):
                    return (False,None,None)
        
        return (True, distancia, antecessor)
    
    @staticmethod
    def getPath(antecessor: list, vertices: tuple) -> str:
        inicio, destino = vertices
        caminho = [destino]

        k = destino 
        while True:
            if antecessor[k-1] == None:
                break
            caminho.insert(0,antecessor[k-1])
            k = antecessor[k-1]
        

        return str(caminho).replace("[","").replace("]","").replace(" ","")

if __name__ == "__main__":
    import sys
    
    quantidade_args = len(sys.argv)
    if quantidade_args != 3:
        print("2 argumentos necessários: nome_arquivo e indice_vertice")
    else:
        CaminhoMinimo.buscar(sys.argv[1], int(sys.argv[2]))