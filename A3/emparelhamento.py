from grafo_nao_dirigido import GrafoNaoDirigido

class Emparelhamento:
    @staticmethod
    def hopcroft_karp(nome_arquivo: str):
        G = GrafoNaoDirigido(nome_arquivo)

        D = [float('inf') for _ in range(G.qtd_vertices())]

        mate = [None for _ in range(G.qtd_vertices())]

        m = 0

        while(Emparelhamento.bfs(G, mate, D)):
            for x in G.X: # O conjunto X precisa ser implementado
                if(mate[x - 1] == None):
                    if(Emparelhamento.dfs(G, mate, x, D)):
                        m += 1
        return m, mate

    @staticmethod
    def bfs(G, mate, D):
        Q = []

        for x in G.X: # O conjunto X precisa ser implementado
            if (mate[x - 1] == None):
                D[x - 1] = 0
                Q.append(x)
            else:
                D[x - 1] = float('inf')
        
        Dnull = float('inf')

        while(Q != []):
            x = Q.pop(0)
            if(D[x - 1] < Dnull):
                for y in G.vizinhos(x):
                    if(D[mate[y - 1]] == float('inf')):
                        D[mate[y - 1]] = D[x - 1] + 1
                        Q.append(mate[y - 1])
        
        return Dnull != float('inf')

    @staticmethod
    def dfs(G, mate, x, D):
        if (x != None):
            for y in G.vizinhos(x):
                if(D[mate[y - 1]] == D[x - 1] + 1):
                    if(Emparelhamento.dfs(G, mate, mate[y - 1], D)):
                        mate[x - 1] = y
                        mate[y - 1] = x
                        return True
            D[x - 1] = float('inf')
            return False
        return True


if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Emparelhamento.hopcroft_karp(sys.argv[1])