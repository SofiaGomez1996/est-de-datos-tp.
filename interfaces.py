from abc import ABC, abstractmethod
from typing import List, Optional

class ICarpeta(ABC):
    """Interfaz que define las operaciones básicas de una carpeta de correo."""

    @abstractmethod
    def agregar_mensaje(self, mensaje) -> None:
        """Agrega un mensaje a la carpeta."""
        pass

    @abstractmethod
    def listar_mensajes(self) -> List:
        """Devuelve la lista de mensajes contenidos en la carpeta."""
        pass

    @abstractmethod
    def buscar_mensaje(self, asunto: Optional[str] = None, remitente: Optional[str] = None) -> List:
        """Busca mensajes por asunto o remitente."""
        pass

    @abstractmethod
    def mover_mensaje(self, mensaje, carpeta_destino) -> bool:
        """Mueve un mensaje a otra carpeta. Retorna True si tuvo éxito."""
        pass


class IUsuario(ABC):
    """Interfaz que define las operaciones que puede realizar un usuario."""

    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto: str, cuerpo: str, servidor) -> None:
        """Envía un mensaje a través del servidor de correo."""
        pass

    @abstractmethod
    def recibir_mensaje(self, mensaje) -> None:
        """Recibe un mensaje y lo almacena en la bandeja de entrada."""
        pass

    @abstractmethod
    def listar_mensajes(self, nombre_carpeta: str = None) -> List:
        """Lista los mensajes de una carpeta específica (o todos)."""
        pass


class IServidorCorreo(ABC):
    """Interfaz que define las operaciones del servidor de correo."""

    @abstractmethod
    def registrar_usuario(self, usuario) -> None:
        """Registra un nuevo usuario en el servidor."""
        pass

    @abstractmethod
    def entregar_mensaje(self, destinatario, mensaje) -> None:
        """Entrega un mensaje al usuario destinatario."""
        pass

    @abstractmethod
    def enviar_mensaje(self, remitente, destinatario, asunto: str, cuerpo: str) -> None:
        """Gestiona el envío de un mensaje entre usuarios."""
        pass