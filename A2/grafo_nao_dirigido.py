from grafo import Grafo

class GrafoNaoDirigido(Grafo):
    
    def __init__(self, nome_arquivo: str) -> None:
        super().__init__()
        self.__quantidade_arestas = 0
        self.__lista_arestas = []
        self.__lista_arestas_duplicado = []
        
        self.ler_arquivo(nome_arquivo)

    def qtd_arestas(self) -> int:
        return self.__quantidade_arestas
    
    def grau(self, v: int) -> int:
        grau = 0
        for i in range(v-1):
            if self._matriz[i][v-1] > 0:
                grau += 1
        for j in range(v, self._quantidade_vertices):
            if self._matriz[v-1][j]:
                grau += 1
        return grau

    def vizinhos(self, v: int) -> list:
        vizinhos = []
        for i in range(v-1):
            if self._matriz[i][v-1] > 0:
                vizinhos.append(i+1)
        for j in range(v, self._quantidade_vertices):
            if self._matriz[v-1][j]:
                vizinhos.append(j+1)
        return vizinhos

    def ha_aresta(self, u: int, v: int) -> bool:
        u, v = self.ordernar_vertices(u, v)
        haAresta = False
        if self._matriz[u-1][v-1] > 0:
            haAresta = True
        return haAresta
    
    def ordernar_vertices(self, u: int, v: int) -> tuple:
        if (u < v):
            return(u, v)
        else:
            return(v, u)
    
    def get_arestas(self) -> list:
        return self.__lista_arestas
    
    def get_arestas_duplicadas(self) -> list:
        if len(self.__lista_arestas_duplicado) == 0:
            for u,v in self.__lista_arestas:
                self.__lista_arestas_duplicado.append((u,v))
                self.__lista_arestas_duplicado.append((v,u))
            self.__lista_arestas_duplicado.sort()
        return self.__lista_arestas_duplicado
    
    def peso(self, u: int, v: int) -> float:
        u, v = self.ordernar_vertices(u, v)
        if self._matriz[u-1][v-1] > 0:
                peso = self._matriz[u-1][v-1]
        else:
            peso = float("inf")
        return peso

    def ler_arquivo(self, nome_arquivo: str) -> None:
        arquivo = open(nome_arquivo, "r")
        lendo_vertices = True
        for linha_string in arquivo:
            linha = linha_string.split()
            if lendo_vertices and linha[0] == "*vertices":
                self._quantidade_vertices = int(linha[1])
            elif lendo_vertices and linha[0] == "*edges":
                lendo_vertices = False
                self._inicializar_matriz()
            elif lendo_vertices:
                self._rotulos_vertices.append(" ".join(linha[1:]))
            else:
                u = int(linha[0])
                v = int(linha[1])
                u, v = self.ordernar_vertices(u, v)
                self._matriz[u-1][v-1] = float(linha[2])
                self.__lista_arestas.append((u, v))
                self.__quantidade_arestas += 1
        self.__lista_arestas.sort()
