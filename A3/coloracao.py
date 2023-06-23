from grafo_nao_dirigido import GrafoNaoDirigido

class Coloracao:
    @staticmethod
    def lawler(nome_arquivo: str):
        G = GrafoNaoDirigido(nome_arquivo)

        X = [i for i in range(2**G.qtd_vertices())]

        X[0] = 0

        S = 2**G.qtd_vertices()

        for s in []: # Não entendi kkkkkkk
            s = Coloracao.f(S) # Implementar f()
            X[s - 1] = float('inf')
            Gi = None # Tbm não entendi
            for I in Coloracao.lcim(Gi): # Implementar I(), ou melhor, lcim()
                i = Coloracao.f(S - I) # Implementar f()
                if(X[i - 1] + 1 < X[s - 1]):
                    X[s - 1] = X[i - 1] + 1
        
        return X[2**G.qtd_vertices() - 1]

    @staticmethod
    def f(S):
        pass

    @staticmethod
    def lcim(G) -> list: # Retorna uma lista com os Conjuntos Independentes Maximais de um grafo
        return [] # Precisa implementar

    @staticmethod
    def opt():
        pass



if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Coloracao.lawler(sys.argv[1])