from grafo import Grafo

class GrafoDirigido(Grafo):
    
    def __init__(self, origem) -> None:
        super().__init__()
        self.__quantidade_arcos = 0
        self.__lista_arcos = []
        
        if type(origem) == str:
            self.ler_arquivo(origem)
        else:
            self.__criar_grafo_transposto(origem)
        
    def qtd_arcos(self) -> int:
        return self.__quantidade_arcos
    
    def grau_entrante(self, v: int) -> int:
        grau = 0
        for i in range(1, self._quantidade_vertices + 1):
            if self._matriz[i-1][v-1] > 0:
                grau += 1
        return grau
    
    def grau_sainte(self, v: int) -> int:
        grau = 0
        for j in range(1, self._quantidade_vertices + 1):
            if self._matriz[v-1][j-1] > 0:
                grau += 1
        return grau

    def vizinhos_antecessores(self, v: int) -> list:
        vizinhos = []
        for i in range(1, self._quantidade_vertices + 1):
            if self._matriz[i-1][v-1] > 0:
                vizinhos.append(i)
        return vizinhos
    
    def vizinhos_sucessores(self, v: int) -> list:
        vizinhos = []
        for j in range(1, self._quantidade_vertices + 1):
            if self._matriz[v-1][j-1] > 0:
                vizinhos.append(j)
        return vizinhos

    def ha_arco(self, u: int, v: int) -> bool:
        ha_arco = False
        if self._matriz[u-1][v-1] > 0:
            ha_arco = True
        return ha_arco
    
    def get_arcos(self) -> list:
        if len(self.__lista_arcos) == 0:
            num_vertices = self.qtd_vertices()
            for i in range(1, num_vertices + 1):
                for j in range(1, num_vertices + 1):
                    if self._matriz[i-1][j-1] != 0:
                        self.__lista_arcos.append((i,j))
        return self.__lista_arcos
    
    def peso(self, u: int, v: int) -> float:
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
            elif lendo_vertices and linha[0] == "*arcs":
                lendo_vertices = False
                self._inicializar_matriz()
            elif lendo_vertices:
                self._rotulos_vertices.append(" ".join(linha[1:]))
            else:
                u = int(linha[0])
                v = int(linha[1])
                self._matriz[u-1][v-1] = float(linha[2])
                self.__quantidade_arcos += 1
                
    def __criar_grafo_transposto(self, grafo: 'GrafoDirigido'):
        self._quantidade_vertices = grafo.qtd_vertices()
        self.__quantidade_arcos = grafo.qtd_arcos()
        
        for v in range(1, self._quantidade_vertices + 1):
            self._rotulos_vertices.append(grafo.rotulo(v))
          
        matriz_original = grafo.get_matriz()
        self._inicializar_matriz()
        for i in range(self._quantidade_vertices):
            for j in range(self._quantidade_vertices):
                self._matriz[i][j] = matriz_original[j][i]
                
    def criar_grafo_transposto(self):
        return GrafoDirigido(self)
    