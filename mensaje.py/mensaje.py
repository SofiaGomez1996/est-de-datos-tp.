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