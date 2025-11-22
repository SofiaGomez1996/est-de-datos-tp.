from collections import deque

class GrafoServidores:
    def __init__(self):
        self.ady = {} #diccionario con conexiones

    def agregar_servidor(self, nombre):
        if nombre not in self.ady:
            self.ady[nombre] = []

    def conectar(self, a, b):
        #grafo NO dirigido
        #si los nodos no existen, los añadimos
        if a not in self.ady:
            self.ady[a] = []
        if b not in self.ady:
            self.ady[b] = []
        if b not in self.ady[a]:
            self.ady[a].append(b)
        if a not in self.ady[b]:
            self.ady[b].append(a)

    def bfs(self, inicio, final):
        #devuelve el camino entre servidores
        if inicio not in self.ady or final not in self.ady:
            return None
        visitado = set()
        cola = deque([(inicio, [inicio])])

        while cola:
            actual, camino = cola.popleft()

            if actual == final:
                return camino

            visitado.add(actual)

            for vecino in self.ady.get(actual, []):
                if vecino not in visitado and vecino not in [n for n in camino]:
                    cola.append((vecino, camino + [vecino]))

        return None