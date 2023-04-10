from grafo import Grafo

class TesteGrafo:
    def __init__(self, grafo: Grafo ) -> None:
        self.grafo = grafo
    
    def matriz(self) -> None:
        print("Teste da matriz")
        self.grafo.imprimir_matriz()
        
    def qtdVertices(self) -> None:
        print("Teste de qtdVertices()")
        print(self.grafo.qtdVertices())
        
    def qtdArestas(self) -> None:
        print("Teste de qtdArestas()")
        print(self.grafo.qtdArestas())
        
    def grau(self) -> None:
        print("Teste de grau()")
        for i in range(self.grafo.qtdVertices()):
            print(f"Vertice {i+1}: {self.grafo.grau(i+1)}")