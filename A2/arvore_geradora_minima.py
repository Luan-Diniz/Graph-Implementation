# -*- coding: UTF-8 -*-
from grafo_nao_dirigido import GrafoNaoDirigido

class Prim:
    @staticmethod
    def executar(nome_arquivo)->None:
        G = GrafoNaoDirigido(nome_arquivo)
        A = Prim.prim(G)

        #O print não é o que deve ser feito.
        print(A)
        #Deve printar uma linha com a soma do peso das arestas
        #Deve printar outra linha com as arestas que estao na árvore geradora

    @staticmethod
    def prim(G: GrafoNaoDirigido) -> list:
        r = 1  #Vértice arbitrário.
        numero_vertices = G.qtd_vertices()
        A = [None for _ in range(numero_vertices)]
        K = [float('inf') for _ in range(numero_vertices)]
        K[r - 1] = 0
        
        Q = [True for _ in range(numero_vertices)]

        while Q != []:
            minimo = float('inf')
            u = int     #vértice com K mínimo e que é candidato a entrar na árvore
            for i in range(0, numero_vertices):
                if Q[i] == True and K[i] < minimo:
                    minimo = K[i]
                    u = i + 1       #u é o "vértice mínimo"

            Q[u - 1] = False    #u entrará na árvore

            for v in G.vizinhos(u):
                if Q[v - 1] == True and G.peso(u,v) < K[v-1]:
                    A[v - 1] = u
                    K[v - 1] = G.peso(u,v)

        return A







if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Prim.executar(sys.argv[1])