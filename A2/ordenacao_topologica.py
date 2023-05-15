from grafo_dirigido import GrafoDirigido

class OrdenacaoTopologica:
    @staticmethod
    def dfs_para_ot(nome_arquivo: str):
        G = GrafoDirigido(nome_arquivo)

        C = []
        for v in range(G.qtd_vertices()):
            C.append(False)

        T = []
        for v in range(G.qtd_vertices()):
            T.append(float('inf'))

        F = []
        for v in range(G.qtd_vertices()):
            F.append(float('inf'))
        
        tempo = 0
        O = []

        for u in range(G.qtd_vertices()):
            if (C[u] == False):
                OrdenacaoTopologica.__dfs_visit_ot(G, u + 1, C, T, F, tempo, O)
        
        i = 0
        for vertice in O:
            i += 1
            if (i < len(O)):
                print(G.rotulo(vertice), end = " -> ")
            else:
                print(G.rotulo(vertice), end = ".")

    @staticmethod
    def __dfs_visit_ot(G: GrafoDirigido, v: int, C: list, T: list, F: list, tempo: int, O: list):
        C[v - 1] = True
        tempo += 1
        T[v - 1] = tempo

        for u in G.vizinhos_antecessores(v):
            if (C[u - 1] == False):
                OrdenacaoTopologica.__dfs_visit_ot(G, u, C, T, F, tempo, O)
        
        tempo += 1
        F[v - 1] = tempo
        O.append(v)

if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        OrdenacaoTopologica.dfs_para_ot(sys.argv[1])