class ColaPrioridad:
    def __init__(self):
        self.urgentes = [] #mensajes urgentes

    def agregar(self, mensaje):
        self.urgentes.append(mensaje)

    def obtener_todos(self):
        return [m.mostrar() for m in self.urgentes]