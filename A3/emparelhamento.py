from grafo_nao_dirigido import GrafoNaoDirigido

class Emparelhamento:
    @staticmethod
    def hopcroft_karp(nome_arquivo: str):
        G = GrafoNaoDirigido(nome_arquivo)

        D = [float('inf') for _ in range(G.qtd_vertices() + 1)]

        mate = [0 for _ in range(G.qtd_vertices() + 1)]

        m = 0

        while(Emparelhamento.bfs(G, mate, D)):
            for x in G.X():
                if(mate[x] == 0):
                    if(Emparelhamento.dfs(G, mate, x, D)):
                        m += 1
        
        i = 0
        emparelhamento = []
        for u, v in G.get_arestas():
            if mate[u] == v:
                if u < v:
                    emparelhamento.append((u,v))
                else:
                    emparelhamento.append((v,u))
            
        print("\nEmparelhamento máximo = ", m, "\n")
        print("Arestas do emparelhamento = ", str(emparelhamento).replace("[", "").replace("]", "").replace("),", ")"), "\n")
        
    @staticmethod
    def bfs(G, mate, D):
        Q = []

        for x in G.X():
            if (mate[x] == 0):
                D[x] = 0
                Q.append(x)
            else:
                D[x] = float('inf')
        
        D[0] = float('inf')

        while(Q != []):
            x = Q.pop(0)
            if(D[x] < D[0]):
                for y in G.vizinhos(x):
                    if (D[mate[y]] == float('inf')):
                        D[mate[y]] = D[x] + 1
                        Q.append(mate[y])
        
        return D[0] != float('inf')

    @staticmethod
    def dfs(G, mate, x, D):
        if (x != 0):
            for y in G.vizinhos(x):
                if(D[mate[y]] == D[x] + 1):
                    if(Emparelhamento.dfs(G, mate, mate[y], D)):
                        mate[x] = y
                        mate[y] = x
                        return True
            D[x] = float('inf')
            return False
        return True


if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Emparelhamento.hopcroft_karp(sys.argv[1])