from grafo import Grafo
from util import Util

class TodosCaminhosMinimos:
    @staticmethod
    def buscar(nome_arquivo: str):
         grafo = Grafo(nome_arquivo)
         matriz_resultado = TodosCaminhosMinimos.FloydWarshall(grafo)

         quantidade_vertices = grafo.qtdVertices()
         for i in range(0, quantidade_vertices):
             print(f"{i+1}:", end = '')
             for j in range(0, quantidade_vertices):
                if j == quantidade_vertices - 1:
                    print(f"{Util.convert_float(matriz_resultado[i][j])}", end = "")
                else:
                    print(f"{Util.convert_float(matriz_resultado[i][j])},", end = "")
             print()
        
    @staticmethod
    def FloydWarshall(grafo: Grafo) -> list:
        number_of_vertices = grafo.qtdVertices()

        distance = [([float('inf') for j in range(number_of_vertices)]) for i in range(number_of_vertices)]   #Cria a matriz de distancias
        for i in range(0, number_of_vertices):
            distance[i][i] = 0
        for u,v in grafo.getArestasDuplicado():
            distance[u-1][v-1] = grafo.peso(u,v)
        
        for k in range(1, number_of_vertices + 1):
            for j in range(1, number_of_vertices + 1):
                for i in range(1, number_of_vertices + 1):
                    if distance[i-1][j-1] > distance[i-1][k-1] + distance[k-1][j-1]:
                        distance[i-1][j-1] = distance[i-1][k-1] + distance[k-1][j-1]
        
        return distance

if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumentos necessários: nome_arquivo")
    else:
        TodosCaminhosMinimos.buscar(sys.argv[1])