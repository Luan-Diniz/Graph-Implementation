from grafo_dirigido import GrafoDirigido

class FluxoMaximo:
    @staticmethod
    def edmonds_karp(nome_arquivo: str, s: int, t: int):
        G = GrafoDirigido(nome_arquivo)

        Gf = G.criar_rede_residual() # Gf precisa ser implementado

        C = [False for _ in range(G.qtd_vertices())]

        A = [None for _ in range(G.qtd_vertices())]

        C[s - 1] = True

        Q = [s]

        while(Q != []):
            u = Q.pop(0)
            for v in G.vizinhos_sucessores(u):
                if(C[v - 1] == False and Gf.peso(u, v) > 0): # Gf precisa ser implementado
                    C[v - 1] = True
                    A[v - 1] = u
                    if(v == t):
                        p = [t]
                        w = t
                        while(w != s):
                            w = A[w - 1]
                            p.append(w)
                        return p
                    Q.append(v)
        return None



if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 4:
        print("3 argumentos necessários: nome_arquivo, vétice fonte e vértice sorvedouro")
    else:
        FluxoMaximo.edmonds_karp(sys.argv[1], sys.argv[2], sys.argv[3])