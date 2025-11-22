from interfaces import IServidorCorreo
from grafo import GrafoServidores

class ServidorCorreo(IServidorCorreo):
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = {} #usuarios registrados
        self.red = GrafoServidores()
        self.red.agregar_servidor(nombre)

    def conectar_con(self, otro_servidor):
        #conecta servidores usando grafo
        self.red.agregar_servidor(otro_servidor.nombre)
        self.red.conectar(self.nombre, otro_servidor.nombre)

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.nombre] = usuario

    def entregar(self, destinatario, mensaje):
        #entrega dentro del servidor
        if destinatario.nombre in self.usuarios:
            self.usuarios[destinatario.nombre].recibir_mensaje(mensaje)
        else:
            print("El usuario no está en este servidor.")