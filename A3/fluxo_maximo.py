from grafo_dirigido import GrafoDirigido

class FluxoMaximo:
    @staticmethod
    def edmonds_karp(nome_arquivo: str, s: int, t: int, Gf: str): # Gf precisa ser implementado
        G = GrafoDirigido(nome_arquivo)

        C = [False for _ in range(G.qtd_vertices())]

        A = [None for _ in range(G.qtd_vertices())]

        C[s - 1] = True

        Q = [s]

        while(Q != []):
            u = Q.pop(0)
            for v in G.vizinhos_sucessores(u):
                if(C[v - 1] == False and G.ha_arco(u, v)): # Pode não ser "ha_arco()"
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
    if quantidade_args != 5:
        print("4 argumentos necessários: nome_arquivo, vétice fonte, vértice sorvedouro e rede residual")
    else:
        FluxoMaximo.edmonds_karp(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])