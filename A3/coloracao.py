from grafo_nao_dirigido import GrafoNaoDirigido
from itertools import chain, combinations

class Coloracao:
    @staticmethod
    def printa_resultado(nome_arquivo: str):
        numero_cores, vertices_coloridos = Coloracao.welsh_powell(nome_arquivo)
        print(f"Número de Cores: {numero_cores}")

        for i in range(1, len(vertices_coloridos) + 1):
            print(f"\tO vértice {i} tem cor {vertices_coloridos[i-1]}")


    @staticmethod
    def welsh_powell(nome_arquivo: str):
        G = GrafoNaoDirigido(nome_arquivo)
        graus =  [i + 1 for i in range(0, G.qtd_vertices())]

        # As cores serao representadas por números inteiros, começando por 1.
        coloracao = [0 for i in range(0, G.qtd_vertices())]

        #Lista decrescente dos vértices baseados em seu grau.
        graus.sort(key=G.grau, reverse=True)  

        index = int
        cor = 0 
        #Enquanto houver algum vertice sem cor
        while 0 in coloracao:
            for i in graus:
                if coloracao[i - 1] == 0:
                    cor += 1
                    coloracao[i - 1] = cor
                    index = i     #Agora temos o vertice com maior grau sem cor ainda
                    break  
            
            for i in graus:
                if i == index:
                    continue
                #Os vertices nao conectados ao vertice de numero index recebem a mesma cor que ele
                elif (not G.ha_aresta(i, index)):
                    coloracao[i - 1] = cor

        return (cor, coloracao)




if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        Coloracao.printa_resultado(sys.argv[1])