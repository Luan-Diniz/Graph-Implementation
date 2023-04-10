from grafo import Grafo
from test_grafo import TesteGrafo
from busca import Busca

print("Questão 1, Representação:\n")
grafo = Grafo("grafo.txt")
teste_grafo = TesteGrafo(grafo)
teste_grafo.realizar_todos_testes()

print("\n\nQuestão 2, Buscas:\n")
Busca.buscar("grafo.txt", 1)
