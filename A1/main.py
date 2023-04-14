from grafo import Grafo
from test_grafo import TesteGrafo
from busca import Busca
from hierholzer import Hierholzer
from caminho_minimo import CaminhoMinimo

print("Questão 1, Representação:\n")
grafo = Grafo("grafo.txt")
teste_grafo = TesteGrafo(grafo)
teste_grafo.realizar_todos_testes()

print("\n\nQuestão 2, Buscas:\n")
Busca.buscar("grafo.txt", 1)

print("\n\nQuestão 3, Hierholzer:\n")
grafo = Grafo("grafo.txt")
Hierholzer.encontrar_ciclo_euleriano(grafo)

print("\n\nQuestão 4, Bellman-Ford:\n")
CaminhoMinimo.buscar("grafo.txt", 1)

