#Clase que representa un mensaje de correo 
class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__contenido = contenido
#propiedades para acceder a los datos
@property
def get_remitente(self):
        return self.__remitente 
@property
def get_destinatario(self):
        return self.__destinatario
#metodo para mostrar el mensaje completo
def mostrar_mensaje(self):
        return f"De: {self.__remitente}\nPara: {self.__destinatario}\nAsunto: {self.__asunto}\n\n{self.__contenido}"
#clase que representa una carpeta de mensajes(como bandeja de entrada)
class Carpeta:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []
#metodo para agregar un mensaje a la carpeta
def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)
#metodo para listar los mensajes en la carpeta
def listar_mensajes(self):
        return [mensaje.mostrar_mensaje() for mensaje in self.__mensajes]
#clase que representa a un usuario del sistema de correo
class Usuario:  
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__bandeja_entrada = Carpeta("Bandeja de entrada")
        self.__enviados = Carpeta("Enviados")
#propiedad para acceder al nombre del usuario
@property
def get_nombre(self):
        return self.__nombre
#metodo para recibir un mensaje y agregarlo a la bandeja de entrada               
def recibir_mensaje(self, mensaje):
        self.__bandeja_entrada.agregar_mensaje(mensaje)
#metodo para enviar mensaje
def enviar_mensaje(self, destinatario, asunto, contenido,servidor):
        mensaje = Mensaje(self.__nombre, destinatario.get_nombre(), asunto, contenido,servidor)
        self.__enviados.agregar_mensaje(mensaje)
        servidor.entregar_mensaje(destinatario,mensaje)         
#metodo para ver la bandeja de entrada
def ver_bandeja_entrada(self):
        return self.__bandeja_entrada.listar_mensajes() 
#metodo para ver los mensajes enviados
def ver_mensajes_enviados(self):
        return self.__enviados.listar_mensajes()
#clase que representa el servidor de correo
class ServidorCorreo:
    def __init__(self):
        self.__usuarios = {}
#metodo para registrar un usuario en el servidor
def registrar_usuario(self, usuario):
        self.__usuarios[usuario.get_nombre] = usuario
#metodo para entregar un mensaje a su destinatario
def entregar_mensaje(self, destinatario, mensaje):
        if destinatario.get_nombre in self.__usuarios:
            self.__usuarios[destinatario.get_nombre].recibir_mensaje(mensaje)
        else:
            print("Error: Usuario destinatario no registrado en el servidor.")      
