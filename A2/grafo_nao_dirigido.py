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
        for j in range(v-1):
            if self._matriz[v-1][j] > 0:
                grau += 1
        for i in range(v, self._quantidade_vertices):
            if self._matriz[i][v-1]:
                grau += 1
        return grau

    def vizinhos(self, v: int) -> list:
        vizinhos = []
        for j in range(v-1):
            if self._matriz[v-1][j] > 0:
                vizinhos.append(j+1)
        for i in range(v, self._quantidade_vertices):
            if self._matriz[i][v-1]:
                vizinhos.append(i+1)
        return vizinhos

    def ha_aresta(self, u: int, v: int) -> bool:
        u, v = self.ordernar_vertices(u, v)
        haAresta = False
        if self._matriz[u-1][v-1] > 0:
            haAresta = True
        return haAresta
    
    def ordernar_vertices(self, u: int, v: int) -> tuple:
        if (u < v):
            return(v, u)
        else:
            return(u, v)
    
    def get_arestas(self) -> list:
        if len(self.__lista_arestas) == 0:
            num_vertices = self.qtdVertices()
            for i in range(1, num_vertices):
                for j in range(0, i):
                    if self._matriz[i][j] != 0:
                        self.__lista_arestas.append((i+1,j+1))
        return self.__lista_arestas
    
    def get_arestas_duplicadas(self) -> list:
        if len(self.__lista_arestas_duplicado) == 0:
            num_vertices = self.qtdVertices()
            for i in range(1,num_vertices + 1):
                for j in range(1,num_vertices + 1):
                    if self.haAresta(i,j):
                        self.__lista_arestas_duplicado.append((i,j))
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
                self.__quantidade_arestas += 1
