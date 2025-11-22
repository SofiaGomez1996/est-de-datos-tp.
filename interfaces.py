from abc import ABC, abstractmethod

class ICarpeta(ABC):
    #interfaz que define las operaciones básicas de una carpeta de correo

    @abstractmethod
    def agregar_mensaje(self, mensaje):
        #agrega un mensaje a la carpeta
        pass

    @abstractmethod
    def listar_mensajes(self):
        #devuelve la lista de mensajes contenidos en la carpeta
        pass

    @abstractmethod
    def buscar(self, asunto):
        #busca mensajes por asunto o remitente
        pass


class IUsuario(ABC):
    #interfaz que define las operaciones que puede realizar un usuario
    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto, contenido, servidor):
        #envía un mensaje a través del servidor de correo
        pass

    @abstractmethod
    def recibir_mensaje(self, mensaje):
        #recibe un mensaje y lo almacena en la bandeja de entrada
        pass


class IServidorCorreo(ABC):
    #interfaz que define las operaciones del servidor de correo
    @abstractmethod
    def registrar_usuario(self, usuario):
        #registra un nuevo usuario en el servidor
        pass

    @abstractmethod
    def entregar(self, destinatario, mensaje):
        #entrega un mensaje al usuario destinatario
        pass