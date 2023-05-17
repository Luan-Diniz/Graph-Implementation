from grafo_nao_dirigido import GrafoNaoDirigido

class Prim:
    @staticmethod
    def executar(nome_arquivo)->None:
        G = GrafoNaoDirigido(nome_arquivo)
        A = Prim.prim(G)

        #printar A

    @staticmethod
    def prim(G: GrafoNaoDirigido) -> list:
        r = 1  #Vértice arbitrário.
        A = [None for _ in G.qtd_vertices()]
        K = [float('inf') for _ in G.qtd_vertices()]
        K[r - 1] = 0
        

        #Continuar








if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Prim.executar(sys.argv[1])