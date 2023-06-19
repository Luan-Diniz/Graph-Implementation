from grafo import Grafo

class Hierholzer:
    
    @staticmethod
    def encontrar_ciclo_euleriano(grafo: Grafo):
        resposta, ciclo = Hierholzer.__encontrar_ciclo_euleriano(grafo)
        if (resposta == False):
            print("0")
        else:
            print("1")
            print(str(ciclo).replace(" ","").replace("[","").replace("]",""))

    @staticmethod
    def __encontrar_ciclo_euleriano(grafo: Grafo):
        conhecidas = {}
        arestas = grafo.getArestas()
        for aresta in arestas:
            conhecidas[aresta] = False
            
        # Seleciona um v conectado a uma aresta
        for v in range(1, grafo.qtdVertices() + 1):
            if grafo.grau(v) > 0:
                break
        
        resposta, ciclo = Hierholzer.__encontrar_subciclo_euleriano(grafo, v, conhecidas)
        if (resposta == False) :
            return (False, None)
        
        for aresta in arestas:
            if (conhecidas[aresta] == False) :
                return (False, None)
                
        return (True, ciclo)

    @staticmethod
    def __encontrar_subciclo_euleriano(grafo: Grafo, v: int, conhecidas: list) -> tuple:
        ciclo = [v]
        t = v
        while True:
            v, u = Hierholzer.__selecionar_aresta_nao_visitada(grafo, conhecidas, v)
            if (v == -1 or u == -1):
                return (False, None)
            else:
                conhecidas[grafo.ordernar_vertices(v, u)] = True
                v = u
                ciclo.append(v)
            
            if (t == v):
                break
            
        for x in ciclo:
            u, w = Hierholzer.__selecionar_aresta_nao_visitada(grafo, conhecidas, x)
            if (u == -1 or w == -1):
                continue
            
            r, subciclo = Hierholzer.__encontrar_subciclo_euleriano(grafo, x, conhecidas)
            if r == False:
                return (False, None)
            Hierholzer.__juntar_ciclos(ciclo, subciclo)
                
        return (True, ciclo)
    
    @staticmethod
    def __selecionar_aresta_nao_visitada(grafo:Grafo, conhecidas: dict, v: int) -> tuple:
        vizinhanca = grafo.vizinhos(v)
        for u in vizinhanca:
            if not conhecidas[grafo.ordernar_vertices(u, v)]:
                return (v, u)
        return (-1, -1)
    
    @staticmethod
    def __juntar_ciclos(ciclo: list, subciclo: list):
        x = subciclo[0]
        for i in range(len(ciclo)):
            if ciclo[i] == x:
                ciclo[i:i + 1] = subciclo
                break

if __name__ == "__main__":
    import sys
    quantidade_args = len(sys.argv)
    if quantidade_args != 2:
        print("1 argumento necessário: nome_arquivo")
    else:
        grafo = Grafo(sys.argv[1])
        Hierholzer.encontrar_ciclo_euleriano(grafo)
