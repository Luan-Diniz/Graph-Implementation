from grafo import Grafo

class Hierholzer:

    @staticmethod
    def encontrar_ciclo_euleriano(grafo: Grafo) :
        conhecidas = [False for i in range(grafo.qtdArestas())]
        resposta, ciclo = Hierholzer.__encontrar_subciclo_euleriano(grafo, 1, conhecidas)

        if (resposta == False) :
            print("0")
            return
        else:
            for aresta in conhecidas:
                if (aresta == False) :
                    print("0")
                    return
            print("1")
            print(ciclo)
            return

    @staticmethod
    def __encontrar_subciclo_euleriano(grafo: Grafo, v: int, conhecidas: list) -> tuple:
        ciclo = [v]
        t = v
        while True:
            cont1 = 0
            cont2 = 0
            for i in range(grafo.qtdArestas()) :
                if (conhecidas[i] == False) :
                    if (grafo.getArestasNaoDirigido()[i][0] == t) :
                        t = grafo.getArestasNaoDirigido()[i][1]
                        conhecidas[i] = True
                        ciclo.append(t)
                    elif (grafo.getArestasNaoDirigido()[i][1] == t) :
                        t = grafo.getArestasNaoDirigido()[i][0]
                        conhecidas[i] = True
                        ciclo.append(t)
                    else:
                        cont2 += 1
                else:
                    cont1 += 1
            if ((cont1 + cont2) == grafo.qtdArestas()) :
                return (False, None)
            if (t == v) :
                break
        for i in range(grafo.qtdArestas()) :
            if (conhecidas[i] == False) :
                for x in range(len(ciclo)) :
                    if (grafo.getArestasNaoDirigido()[i][0] == ciclo[x] or grafo.getArestasNaoDirigido()[i][1] == ciclo[x]) :
                        resposta, ciclo2 = Hierholzer.__encontrar_subciclo_euleriano(grafo, ciclo[x], conhecidas)
                        if (resposta == False) :
                            return (False, None)
                        ciclo[x:x] = ciclo2
        return (True, ciclo)


if __name__ == "__main__":
    import sys

    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: grafo")
    else:
        grafo = Grafo(sys.argv[1])
        Hierholzer.encontrar_ciclo_euleriano(grafo)
