from grafo import Grafo
from test_grafo import TesteGrafo

grafeto = Grafo("grafo.txt")
teste_grafo = TesteGrafo(grafeto)

teste_grafo.matriz()
print()
teste_grafo.qtdVertices()
print()
teste_grafo.qtdArestas()
print()
teste_grafo.grau()
