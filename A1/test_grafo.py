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
    
    def rotulo(self) -> None:
        print("Teste de rotulo()")
        for i in range(self.grafo.qtdVertices()):
            print(f"Rotulo de {i+1}: {self.grafo.rotulo(i+1)}")
    
    def vizinhos(self) -> None:
        print("Teste de vizinhos()")
        for i in range(self.grafo.qtdVertices()):
            print(f"Vizinhos {i+1}: {self.grafo.vizinhos(i+1)}")
    
    def haAresta(self) -> None:
        print("Teste de haAresta()")
        for i in range(self.grafo.qtdVertices()):
            for j in range(self.grafo.qtdVertices()):
                print(f"Aresta {i+1}-{j+1}: {self.grafo.haAresta(i+1, j+1)}")
    
    def peso(self) -> None:
        print("Teste de peso()")
        for i in range(self.grafo.qtdVertices()):
            for j in range(self.grafo.qtdVertices()):
                print(f"Peso {i+1}-{j+1}: {self.grafo.peso(i+1, j+1)}")
            
    def realizar_todos_testes(self):
        self.matriz()
        print()
        self.qtdVertices()
        print()
        self.qtdArestas()
        print()
        self.grau()
        print()
        self.rotulo()
        print()
        self.vizinhos()
        print()
        self.haAresta()
        print()
        self.peso()
