from grafo_dirigido import GrafoDirigido

class OrdenacaoTopologica:
    @staticmethod
    def dfs_para_ot(nome_arquivo: str):
        G = GrafoDirigido(nome_arquivo)

        C = [False for v in range(G.qtd_vertices())]

        T = [float('inf') for v in range(G.qtd_vertices())]

        F = [float('inf') for v in range(G.qtd_vertices())]
        
        tempo = 0
        O = []

        for u in range(1, G.qtd_vertices() + 1):
            if (C[u-1] == False):
                OrdenacaoTopologica.__dfs_visit_ot(G, u, C, T, F, tempo, O)
                tempo = F[u-1]
        
        i = 0
        for vertice in O:
            i += 1
            if (i < len(O)):
                print(G.rotulo(vertice), end = " -> ")
            else:
                print(G.rotulo(vertice), end = ".")
        print()

    @staticmethod
    def __dfs_visit_ot(G: GrafoDirigido, v: int, C: list, T: list, F: list, tempo: int, O: list):
        C[v - 1] = True
        tempo += 1
        T[v - 1] = tempo

        for u in G.vizinhos_sucessores(v):
            if (C[u - 1] == False):
                OrdenacaoTopologica.__dfs_visit_ot(G, u, C, T, F, tempo, O)
                tempo = F[u-1]
        
        tempo += 1
        F[v - 1] = tempo
        O.insert(0, v)



if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        OrdenacaoTopologica.dfs_para_ot(sys.argv[1])