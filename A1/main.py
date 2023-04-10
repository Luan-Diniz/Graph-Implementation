from grafo import Grafo

grafeto = Grafo("grafo.txt")
grafeto.imprimir_matriz()
print("Quantidade de vertices e arestas:",grafeto.qtdVertices(), grafeto.qtdArestas())
print("Grau do vertice 2:", grafeto.grau(2))
print("Rotulo do vertice 2:", grafeto.rotulo(2))
print("Vizinhos de 2:", grafeto.vizinhos(2))
print("Há aresta 2 3:", grafeto.haAresta(2, 3))
print("Há aresta 3 2:", grafeto.haAresta(3, 2))
print("Há aresta 2 2:", grafeto.haAresta(2, 2))
print("Peso 2 3:", grafeto.peso(2, 3))
print("Peso 2 2:", grafeto.peso(2, 2))
