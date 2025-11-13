from collections import deque

class Mensaje:
    def __init__(self, asunto, contenido):
        self.asunto = asunto
        self.contenido = contenido


class ServidorCorreo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def conectar(self, otro_servidor):
        if otro_servidor not in self.conexiones:
            self.conexiones.append(otro_servidor)
        if self not in otro_servidor.conexiones:
            otro_servidor.conexiones.append(self)

   
    # BFS → Busca la ruta más corta

    def encontrar_ruta_BFS(self, destino):
        visitados = set()
        cola = deque()
        cola.append((self, [self]))

        while cola:
            actual, ruta = cola.popleft()

            if actual == destino:
                return ruta

            visitados.add(actual)

            for vecino in actual.conexiones:
                if vecino not in visitados:
                    cola.append((vecino, ruta + [vecino]))

        return None


    # DFS → Busca cualquier ruta válida

    def encontrar_ruta_DFS(self, destino, visitados=None, ruta=None):
        if visitados is None:
            visitados = set()
        if ruta is None:
            ruta = []

        ruta.append(self)
        visitados.add(self)

        if self == destino:
            return ruta

        for vecino in self.conexiones:
            if vecino not in visitados:
                nueva_ruta = vecino.encontrar_ruta_DFS(destino, visitados, ruta[:])
                if nueva_ruta:
                    return nueva_ruta

        return None


  # Simulación del envío de mensaje
  
    def enviar_mensaje(self, destino, mensaje, modo="BFS"):
        print("---------------------------------------------------")
        print("Enviando mensaje desde " + self.nombre + " a " + destino.nombre)

        if modo == "BFS":
            ruta = self.encontrar_ruta_BFS(destino)
            if ruta:
                nombres = [s.nombre for s in ruta]
                print("Ruta elegida (BFS): " + " → ".join(nombres))
            else:
                print("No se encontró ruta entre los servidores")

        elif modo == "DFS":
            ruta = self.encontrar_ruta_DFS(destino)
            if ruta:
                nombres = [s.nombre for s in ruta]
                print("Ruta elegida (DFS): " + " → ".join(nombres))
            else:
                print("No se encontró ruta entre los servidores")

        print("---------------------------------------------------")
 

