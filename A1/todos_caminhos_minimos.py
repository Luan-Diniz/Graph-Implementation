from grafo import Grafo

class TodosCaminhosMinimos:
    @staticmethod
    def buscar(nome_arquivo: str):
         grafo = Grafo(nome_arquivo)
         #usar FloydWarshall e printar certo
        

    @staticmethod
    def FloydWarshall(grafo: Grafo) -> list:
        pass





if __name__ == "__main__":
    import sys
    
    quantidade_args = len(sys.argv)
    if quantidade_args != 3:
        print("2 argumentos necessários: nome_arquivo e indice_vertice")
    else:
        TodosCaminhosMinimos.buscar(sys.argv[1], int(sys.argv[2]))