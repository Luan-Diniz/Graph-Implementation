class GrafoDirigido:
    
    def __init__(self, nome_arquivo: str) -> None:
        self.__quantidade_vertices = 0
        self.__quantidade_arcos = 0
        self.__matriz = None
        self.__rotulos_vertices = []
        self.__lista_arcos = []
        
        self.lerArquivo(nome_arquivo)
        
    def qtd_vertices(self) -> int:
        return self.__quantidade_vertices

    def qtd_arcos(self) -> int:
        return self.__quantidade_arcos
    
    def grau_entrante(self, v: int) -> int:
        grau = 0
        for i in range(1, self.__quantidade_vertices + 1):
            if self.__matriz[i-1][v-1] > 0:
                grau += 1
        return grau
    
    def grau_sainte(self, v: int) -> int:
        grau = 0
        for j in range(1, self.__quantidade_vertices + 1):
            if self.__matriz[v-1][j-1] > 0:
                grau += 1
        return grau

    def rotulo(self, v: int) -> str:
        return self.__rotulos_vertices[v-1]

    def vizinhos_antecessores(self, v: int) -> list:
        vizinhos = []
        for i in range(1, self.__quantidade_vertices + 1):
            if self.__matriz[i-1][v-1] > 0:
                vizinhos.append(i)
        return vizinhos
    
    def vizinhos_sucessores(self, v: int) -> list:
        vizinhos = []
        for j in range(1, self.__quantidade_vertices + 1):
            if self.__matriz[v-1][j-1] > 0:
                vizinhos.append(j)
        return vizinhos

    def ha_arco(self, u: int, v: int) -> bool:
        ha_arco = False
        if self.__matriz[u-1][v-1] > 0:
            ha_arco = True
        return ha_arco

    def peso(self, u: int, v: int) -> float:
        if self.__matriz[u-1][v-1] > 0:
                peso = self.__matriz[u-1][v-1]
        else:
            peso = float("inf")
        return peso
    
    def get_arcos(self) -> list:
        if len(self.__lista_arcos) == 0:
            num_vertices = self.qtd_vertices()
            for i in range(1, num_vertices + 1):
                for j in range(1, num_vertices + 1):
                    if self.__matriz[i-1][j-1] != 0:
                        self.__lista_arcos.append((i,j))
        return self.__lista_arcos
    
    def lerArquivo(self, nome_arquivo: str) -> None:
        arquivo = open(nome_arquivo, "r")
        lendo_vertices = True
        for linha_string in arquivo:
            linha = linha_string.split()
            if lendo_vertices and linha[0] == "*vertices":
                self.__quantidade_vertices = int(linha[1])
            elif lendo_vertices and linha[0] == "*arcs":
                lendo_vertices = False
                self.__inicializar_matriz()
            elif lendo_vertices:
                self.__rotulos_vertices.append(linha[1])
            else:
                u = int(linha[0])
                v = int(linha[1])
                self.__matriz[u-1][v-1] = float(linha[2])
                self.__quantidade_arcos += 1
            
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
