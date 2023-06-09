class Grafo:
    def __init__(self, nome_arquivo: str) -> None:
        self.__quantidade_vertices = 0
        self.__quantidade_arestas = 0
        self.__matriz = None
        self.__rotulos_vertices = []
        self.__lista_arestas = []
        self.__lista_arestas_duplicado = []
        
        self.lerArquivo(nome_arquivo)
        
    def qtdVertices(self) -> int:
        return self.__quantidade_vertices

    def qtdArestas(self) -> int:
        return self.__quantidade_arestas
    
    def grau(self, v: int) -> int:
        grau = 0
        for j in range(v-1):
            if self.__matriz[v-1][j] > 0:
                grau += 1
        for i in range(v, self.__quantidade_vertices):
            if self.__matriz[i][v-1]:
                grau += 1
        return grau

    def rotulo(self, v: int) -> str:
        return self.__rotulos_vertices[v-1]

    def vizinhos(self, v: int) -> list:
        vizinhos = []
        for j in range(v-1):
            if self.__matriz[v-1][j] > 0:
                vizinhos.append(j+1)
        for i in range(v, self.__quantidade_vertices):
            if self.__matriz[i][v-1]:
                vizinhos.append(i+1)
        return vizinhos

    def haAresta(self, u: int, v: int) -> bool:
        u, v = self.ordernar_vertices(u, v)
        haAresta = False
        if self.__matriz[u-1][v-1] > 0:
            haAresta = True
        return haAresta

    def peso(self, u: int, v: int) -> float:
        u, v = self.ordernar_vertices(u, v)
        if self.__matriz[u-1][v-1] > 0:
                peso = self.__matriz[u-1][v-1]
        else:
            peso = float("inf")
        return peso
    
    def getArestas(self) -> list:
        if len(self.__lista_arestas) == 0:
            num_vertices = self.qtdVertices()
            for i in range(1, num_vertices):
                for j in range(0, i):
                    if self.__matriz[i][j] != 0:
                        self.__lista_arestas.append((i+1,j+1))
        return self.__lista_arestas
    
    def getArestasDuplicado(self) -> list:
        if len(self.__lista_arestas_duplicado) == 0:
            num_vertices = self.qtdVertices()
            for i in range(1,num_vertices + 1):
                for j in range(1,num_vertices + 1):
                    if self.haAresta(i,j):
                        self.__lista_arestas_duplicado.append((i,j))
        return self.__lista_arestas_duplicado

    def lerArquivo(self, nome_arquivo: str) -> None:
        arquivo = open(nome_arquivo, "r")
        lendo_vertices = True
        for linha_string in arquivo:
            linha = linha_string.split()
            if lendo_vertices and linha[0] == "*vertices":
                self.__quantidade_vertices = int(linha[1])
            elif lendo_vertices and linha[0] == "*edges":
                lendo_vertices = False
                self.__inicializar_matriz()
            elif lendo_vertices:
                self.__rotulos_vertices.append(linha[1])
            else:
                u = int(linha[0])
                v = int(linha[1])
                u, v = self.ordernar_vertices(u, v)
                self.__matriz[u-1][v-1] = float(linha[2])
                self.__quantidade_arestas += 1
            
    def __inicializar_matriz(self) -> None:
        self.__matriz = [[0 for j in range(self.__quantidade_vertices)] for i in range(self.__quantidade_vertices)]
        
    def __get_indice(self, rotulo: str) -> int:
        for i in range(len(self.__rotulos_vertices)):
            if rotulo == self.__rotulos_vertices[i]:
                return i + 1
        return -1
    
    def imprimir_matriz(self) -> None:
        for i in range(self.__quantidade_vertices):
            print(self.__matriz[i])

    def ordernar_vertices(self, u: int, v: int) -> tuple:
        if (u < v):
            return(v, u)
        else:
            return(u, v)
