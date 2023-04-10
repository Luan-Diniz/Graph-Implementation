from grafo import Grafo
from test_grafo import TesteGrafo

grafo = Grafo("grafo.txt")
teste_grafo = TesteGrafo(grafo)

teste_grafo.realizar_todos_testes()
