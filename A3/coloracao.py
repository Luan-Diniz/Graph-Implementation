from grafo_nao_dirigido import GrafoNaoDirigido
from itertools import chain, combinations

class Coloracao:
    @staticmethod
    def lawler(nome_arquivo: str):
        G = GrafoNaoDirigido(nome_arquivo)

        X = [i for i in range(2**G.qtd_vertices())]

        X[0] = 0

        cp = Coloracao.conjunto_potencia(G.get_arestas)

        for S in cp.remove(tuple(())):
            s = Coloracao.f(S) # Implementar f()
            X[s - 1] = float('inf')
            Gi = (S, set(cp).union(set(G.get_arestas())))
            for I in Coloracao.conjuntos_independentes_maximais(Gi):
                i = Coloracao.f(S.remove(I)) # Implementar f()
                if(X[i - 1] + 1 < X[s - 1]):
                    X[s - 1] = X[i - 1] + 1
        
        return X[2**G.qtd_vertices() - 1]

    @staticmethod
    def f(S: list) -> int:
        return 0

    @staticmethod
    def opt() -> int:
        return 0

    @staticmethod
    def conjuntos_independentes_maximais(G: GrafoNaoDirigido) -> list:
        S = Coloracao.conjunto_potencia(G.get_arestas()).reverse()
        R = []
        for X in S:
            c = True
            for v in X:
                for u in X:
                    if (G.ha_aresta(u, v)) :
                        c = False
                        break
            if (c) :
                R.append(X)
        return R

    @staticmethod
    def conjunto_potencia(lista: list) -> list:
        # "lista_potencia" é uma lista de todas as combinações de elementos de "lista" com exceção do elemento vazio
        # "combinations(list, size)" retorna uma lista com todas as combinações de tamanho "size" na lista "list"
        lista_potencia = list(chain.from_iterable(combinations(lista, tamanho) for tamanho in range(len(lista) + 1)))
        return lista_potencia



if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Coloracao.lawler(sys.argv[1])