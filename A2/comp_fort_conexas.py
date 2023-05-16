from grafo_dirigido import GrafoDirigido

class CompFortConexas:
    @staticmethod
    def comp_fort_conexas(nome_arquivo: str):
        G = GrafoDirigido(nome_arquivo)

        C, T, A, F = CompFortConexas.__dfs_para_cfc(G, False)

        Gt = G.criar_grafo_transposto()

        Ct, Tt, At, Ft = CompFortConexas.__dfs_para_cfc(Gt, True)
        
        print(At)

    @staticmethod
    def __dfs_para_cfc(G: GrafoDirigido, Alt = bool):

        C = [False for v in range(G.qtd_vertices())]

        T = [float('inf') for v in range(G.qtd_vertices())]

        A = [[] for v in range(G.qtd_vertices())]

        F = [float('inf') for v in range(G.qtd_vertices())]
        
        tempo = 0

        if (Alt):
            tmp = sorted(F, reverse=True)
            u = 0
            while(u < G.qtd_vertices()):
                if (F[u] == tmp[0]):
                    if (C[u] == False):
                        CompFortConexas.__dfs_visit_cfc(G, u + 1, C, T, A, F, tempo)
                    tmp.pop(0)
                    u = 0
                else:
                    u += 1
        else:
            for u in range(G.qtd_vertices()):
                if (C[u] == False):
                    CompFortConexas.__dfs_visit_cfc(G, u + 1, C, T, A, F, tempo)
        
        return (C, T, A, F)

    @staticmethod
    def __dfs_visit_cfc(G: GrafoDirigido, v: int, C: list, T: list, A: dict, F: list, tempo: int):
        C[v - 1] = True
        tempo += 1
        T[v - 1] = tempo

        for u in G.vizinhos_antecessores(v):
            if (C[u - 1] == False):
                A[u - 1].append(v)
                CompFortConexas.__dfs_visit_cfc(G, u, C, T, A, F, tempo)
        
        tempo += 1
        F[v - 1] = tempo

if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        CompFortConexas.comp_fort_conexas(sys.argv[1])