from grafo_dirigido import GrafoDirigido

class OrdenacaoTopologica:
    @staticmethod
    def dfs_para_ot(nome_arquivo: str):
        G = GrafoDirigido(nome_arquivo)

        C = {}
        for vertice in range(1, G.qtd_vertices() + 1):
            C[vertice] = False

        T = {}
        for vertice in range(1, G.qtd_vertices() + 1):
            T[vertice] = float('inf')

        F = {}
        for vertice in range(1, G.qtd_vertices() + 1):
            F[vertice] = float('inf')
        
        tempo = 0
        O = []

        for u in range(1, G.qtd_vertices() + 1):
            if (C[u] == False):
                OrdenacaoTopologica.__dfs_visit_ot(G, u, C, T, F, tempo, O)
        
        i = 0
        for vertice in O:
            i += 1
            if (i < len(O)):
                print(G.rotulo(vertice), end = " -> ")
            else:
                print(G.rotulo(vertice), end = ".")

    @staticmethod
    def __dfs_visit_ot(G: GrafoDirigido, v: int, C: dict, T: dict, F: dict, tempo: int, O: list):
        C[v] = True
        tempo += 1
        T[v] = tempo

        for u in G.vizinhos_antecessores(v):
            if (C[u] == False):
                OrdenacaoTopologica.__dfs_visit_ot(G, u, C, T, F, tempo, O)
        
        tempo += 1
        F[v] = tempo
        O.append(v)

if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        OrdenacaoTopologica.dfs_para_ot(sys.argv[1])