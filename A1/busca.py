from grafo import Grafo

class Busca:
    
    @staticmethod
    def buscar(nome_arquivo: str, s: int):
        grafo = Grafo(nome_arquivo)
        
        distancia, antecessor = Busca.__busca_largura(grafo, s)
        for nivel in range(max(distancia) + 1):
            saida_nivel = f"{nivel}: "
            for v in range(len(distancia)):
                if distancia[v] == nivel:
                    saida_nivel += f"{v+1} "
            print(saida_nivel)

    @staticmethod       
    def __busca_largura(grafo: Grafo, s: int)  -> tuple:
        visitados = [False for i in range(grafo.qtdVertices())]
        distancia = [float("inf") for i in range(grafo.qtdVertices())]
        antecessor = [None for i in range(grafo.qtdVertices())]
        
        visitados[s-1] = True
        distancia[s-1] = 0
        
        fila = []
        fila.append(s)
        
        while len(fila) > 0:
            u = fila.pop(0)
            for v in grafo.vizinhos(u):
                if not visitados[v-1]:
                    visitados[v-1] = True
                    distancia[v-1] = distancia[u-1] + 1
                    antecessor[v-1] = u
                    fila.append(v)
        
        return (distancia, antecessor)
