from grafo_dirigido import GrafoDirigido

class CompFortConexas:
    @staticmethod
    def comp_fort_conexas(nome_arquivo: str):
        G = GrafoDirigido(nome_arquivo)

        C, T, A, F = CompFortConexas.__dfs_para_cfc(G)

        Gt = G.criar_grafo_transposto()

        Ct, Tt, At, Ft = CompFortConexas.__dfs_para_cfc(Gt, alterado=True, F_anterior=F)
        
        print(At)
        
    @staticmethod
    def __dfs_para_cfc(G: GrafoDirigido, alterado: bool=False, F_anterior: list= None):

        C = [False for v in range(G.qtd_vertices())]

        T = [float('inf') for v in range(G.qtd_vertices())]

        A = [None for v in range(G.qtd_vertices())]

        F = [float('inf') for v in range(G.qtd_vertices())]
        
        tempo = 0

        if (alterado):
            tempo_vertice = []
            for v in range(1, G.qtd_vertices() + 1):
                tempo_vertice.append((F_anterior[v-1], v))
            tempo_vertice.sort(reverse = True)
            
            for t, u in tempo_vertice:
                if C[u-1] == False:
                    CompFortConexas.__dfs_visit_cfc(G, u, C, T, A, F, tempo)
                    tempo = F[u-1]

        else:
            for u in range(1, G.qtd_vertices() + 1):
                if (C[u-1] == False):
                    CompFortConexas.__dfs_visit_cfc(G, u, C, T, A, F, tempo)
                    tempo = F[u-1]
        
        return (C, T, A, F)

    @staticmethod
    def __dfs_visit_cfc(G: GrafoDirigido, v: int, C: list, T: list, A: list, F: list, tempo: int):
        C[v - 1] = True
        tempo += 1
        T[v - 1] = tempo

        for u in G.vizinhos_sucessores(v):
            if (C[u - 1] == False):
                A[u - 1] = v
                CompFortConexas.__dfs_visit_cfc(G, u, C, T, A, F, tempo)
                tempo = F[u-1]
        
        tempo += 1
        F[v - 1] = tempo

if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        CompFortConexas.comp_fort_conexas(sys.argv[1])