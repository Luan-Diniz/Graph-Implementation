from grafo import Grafo
from test_grafo import TesteGrafo
from busca import Busca
from hierholzer import Hierholzer
from caminho_minimo import CaminhoMinimo
from todos_caminhos_minimos import TodosCaminhosMinimos

print("Questão 1, Representação:\n")
grafo = Grafo("grafo.txt")
teste_grafo = TesteGrafo(grafo)
teste_grafo.realizar_todos_testes()

print("\n\nQuestão 2, Buscas:\n")
Busca.buscar("grafo.txt", 1)

print("\n\nQuestão 3, Hierholzer:\n")
print("Teste1: Grafo sem Ciclo Euleriano\n")
grafo = Grafo("grafo.txt")
Hierholzer.encontrar_ciclo_euleriano(grafo)
print("\nTeste2: Grafo com Ciclo Euleriano\n")
grafo = Grafo("grafo3.txt")
Hierholzer.encontrar_ciclo_euleriano(grafo)

print("\n\nQuestão 4, Bellman-Ford:\n")
CaminhoMinimo.buscar("grafo2.txt", 1)

print("\n\nQuestão 5, Floyd-Warshall:\n")
TodosCaminhosMinimos.buscar("grafo4.txt")


