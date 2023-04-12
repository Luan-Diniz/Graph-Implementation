class Grafo:
    def __init__(self, nome_arquivo: str) -> None:
        self.__quantidade_vertices = 0
        self.__quantidade_arestas = 0
        self.__matriz = None
        self.__rotulos_vertices = []
        self.__lista_arestas = []
        
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
        u, v = self.__ordernar_vertices(u, v)
        haAresta = False
        if self.__matriz[u-1][v-1] > 0:
            haAresta = True
        return haAresta

    def peso(self, u: int, v: int) -> float:
        u, v = self.__ordernar_vertices(u, v)
        if self.__matriz[u-1][v-1] > 0:
                peso = self.__matriz[u-1][v-1]
        else:
            peso = float("inf")
        return peso

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
                u = self.__get_indice(linha[0])
                v = self.__get_indice(linha[1])
                u, v = self.__ordernar_vertices(u, v)
                self.__matriz[u-1][v-1] = int(linha[2])
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

    def __ordernar_vertices(self, u: int, v: int) -> tuple:
        if (u < v):
            return(v, u)
        else:
            return(u, v)
        


    def getArestas(self) -> list:
        if self.__lista_arestas == []:
            for i in range(self.qtdVertices()):
                for j in range(self.qtdVertices()):
                    if self.haAresta(i,j):
                        self.__lista_arestas.append((i,j))
                    if len(self.__lista_arestas) == self.qtdArestas():
                        return self.__lista_arestas

        return self.__lista_arestas
        

