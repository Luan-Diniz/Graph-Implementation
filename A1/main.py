from grafo import Grafo
from test_grafo import TesteGrafo

grafeto = Grafo("grafo.txt")
teste_grafo = TesteGrafo(grafeto)

teste_grafo.realizar_todos_testes()