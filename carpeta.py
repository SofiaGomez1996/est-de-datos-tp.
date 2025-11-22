from interfaces import ICarpeta

class Carpeta(ICarpeta):
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = [] #lista de mensajes
        self.subcarpetas = [] #para guardar subcarpetas

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def listar_mensajes(self):
        #devuelve los mensajes en texto
        return [m.mostrar() for m in self.mensajes]

    def agregar_subcarpeta(self, carpeta):
        #función para agregar subcarpetas
        self.subcarpetas.append(carpeta)

    def buscar(self, asunto):
        #búsqueda recursiva
        for m in self.mensajes:
            if m.asunto == asunto:
                return m

        for sub in self.subcarpetas:
            encontrado = sub.buscar(asunto)
            if encontrado:
                return encontrado

        return None