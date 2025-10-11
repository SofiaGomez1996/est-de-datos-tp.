class Carpeta(ICarpeta):
        def __init__(self, nombre):
         self.__nombre = nombre
         self.__mensajes = []

        def agregar_mensaje(self, mensaje):
         self.__mensajes.append(mensaje)
#Agrega un mensaje a la carpeta
        def listar_mensajes(self):
         return [mensaje.mostrar_mensaje() for mensaje in self.__mensajes]
#Devuelve la lista de mensajes en formato de texto