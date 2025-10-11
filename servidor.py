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