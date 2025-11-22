from interfaces import IUsuario
from carpeta import Carpeta
from cola_prioridad import ColaPrioridad

class Usuario(IUsuario):
    def __init__(self, nombre):
        self.nombre = nombre
        self.bandeja = Carpeta("Bandeja de entrada")
        self.enviados = Carpeta("Enviados")
        self.carpetas = {"Trabajo": Carpeta("Trabajo"), "Personal": Carpeta("Personal")}
        self.urgentes = ColaPrioridad()

    def enviar_mensaje(self, destinatario, asunto, contenido, servidor):
        from mensaje import Mensaje
        msg = Mensaje(self.nombre, destinatario.nombre, asunto, contenido)
        self.enviados.agregar_mensaje(msg)
        servidor.entregar(destinatario, msg)

    def recibir_mensaje(self, mensaje):
        self.bandeja.agregar_mensaje(mensaje)

    def marcar_como_urgente(self, mensaje):
        self.urgentes.agregar(mensaje)