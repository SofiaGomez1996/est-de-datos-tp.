class Usuario(IUsuario):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__bandeja_entrada = Carpeta("Bandeja de entrada")
        self.__enviados = Carpeta("Enviados")

    @property
    def get_nombre(self):
        return self.__nombre

    def enviar_mensaje(self, destinatario, asunto, contenido, servidor):
        mensaje = Mensaje(self.__nombre, destinatario.get_nombre, asunto, contenido)
        self.__enviados.agregar_mensaje(mensaje)
        servidor.entregar_mensaje(destinatario, mensaje)

    def recibir_mensaje(self, mensaje):
        self.__bandeja_entrada.agregar_mensaje(mensaje)

    def ver_bandeja_entrada(self):
        return self.__bandeja_entrada.listar_mensajes()

    def ver_mensajes_enviados(self):
        return self.__enviados.listar_mensajes()
 # ======================
# Esta interfaz define el contrato para un servidor de correo electrónico.
# Todo servidor debe poder:
# 1) Registrar usuarios
# 2) Entregar mensajes a los destinatarios correctos