from carpeta import Carpeta
from mensaje import Mensaje

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inbox = Carpeta("Bandeja de entrada")
        self.enviados = Carpeta("Enviados")

    def enviar_mensaje(self, destinatario, asunto, cuerpo, servidor):
        mensaje = Mensaje(self.nombre, destinatario.nombre, asunto, cuerpo)
        self.enviados.agregar_mensaje(asunto, self.nombre)
        servidor.entregar_mensaje(destinatario, mensaje)

    def recibir_mensaje(self, mensaje):
        self.inbox.agregar_mensaje(mensaje.asunto, mensaje.remitente)