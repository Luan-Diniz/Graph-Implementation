from abc import ABC, abstractmethod

# Classe abstrata
class Grafo(ABC):
    
    def __init__(self) -> None:
        self._quantidade_vertices = 0
        self._matriz = None
        self._rotulos_vertices = []
        
    def qtd_vertices(self) -> int:
        return self._quantidade_vertices

    def rotulo(self, v: int) -> str:
        return self._rotulos_vertices[v-1]
        
    def get_indice(self, rotulo: str) -> int:
        for i in range(len(self._rotulos_vertices)):
            if rotulo == self._rotulos_vertices[i]:
                return i + 1
        return -1
    
    def imprimir_matriz(self) -> None:
        for i in range(self._quantidade_vertices):
            print(self._matriz[i])
            
    def _inicializar_matriz(self) -> None:
        self._matriz = [[0 for j in range(self._quantidade_vertices)] for i in range(self._quantidade_vertices)]
            
    @abstractmethod
    def peso(self, u: int, v: int) -> float:
        pass
    
    @abstractmethod
    def ler_arquivo(self, nome_arquivo: str) -> None:
        pass
