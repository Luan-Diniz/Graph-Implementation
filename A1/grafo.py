import aresta

class Grafo:
    def __init__(self):
        self.__quantidade_vertices = 0
        self.__matriz = None
        self.__rotulos_vertices = []
        
    def qtdVertices():
        pass

    def qtdArestas():
        pass
    
    def grau():
        pass

    def rotulo():
        pass

    def vizinhos():
        pass

    def haAresta():
        pass

    def peso():
        pass

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
                origem = self.__get_indice(linha[0]) - 1
                destino = self.__get_indice(linha[1]) - 1
                self.__matriz[destino][origem] = int(linha[2])
            
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


grafeto = Grafo()
grafeto.lerArquivo("grafo.txt")
grafeto.imprimir_matriz()
        