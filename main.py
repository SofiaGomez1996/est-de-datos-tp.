from abc import ABC, abstractmethod 
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
#Esta interfaz define el contraro que debe cumplir cualquier clase que represente una "carpeta" de mensajes.
#Es decir, toda carpeta debe poder agregar mensajes y listar los mensajes que contiene.
class ICarpeta(ABC):
        @abstractmethod
        def agregar_mensaje(self, mensaje):
            pass
        @abstractmethod
        def listar_mensajes(self):
            pass
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

# Esta interfaz define el contrato para un "Usuario" del sistema de correo.
# Todo usuario debe poder:
# 1) Enviar mensajes
# 2) Recibir mensajes
# 3) Ver su bandeja de entrada
# 4) Ver los mensajes enviados
class IUsuario(ABC):
      @abstractmethod
      def enviar_mensaje(self, mensaje):
            pass 
# Envìa un mensaje a otro usuario usando el servidor                               
      @abstractmethod
      def recibir_mensaje(self, mensaje):
                pass
      @abstractmethod
      def ver_bandeja_entrada(self):
                pass
      
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
   
class IServidorCorreo(ABC):
    @abstractmethod
    def registrar_usuario(self, usuario):
        pass

    @abstractmethod
    def entregar_mensaje(self, destinatario, mensaje):
        pass

#Clase ServidorCorreo
class ServidorCorreo(IServidorCorreo):
    def __init__(self):
        self.__usuarios = {}

    def registrar_usuario(self, usuario):
        self.__usuarios[usuario.get_nombre] = usuario

    def entregar_mensaje(self, destinatario, mensaje):
        if destinatario.get_nombre in self.__usuarios:
            self.__usuarios[destinatario.get_nombre].recibir_mensaje(mensaje)
        else:
            print("Error: Usuario destinatario no registrado en el servidor.")

    

c