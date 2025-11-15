"""
CLIENTE DE CORREO ELECTRÓNICO COMPLETO
Descripción: Implementación orientada a objetos de un cliente de correo electrónico,
con carpetas recursivas, usuarios, servidor, filtros, cola de prioridades y grafo de servidores.
"""


# INTERFACES


from abc import ABC, abstractmethod
from typing import List, Optional
import heapq
from collections import deque

class ICarpeta(ABC):
    @abstractmethod
    def agregar_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensajes(self):
        pass

    @abstractmethod
    def buscar_mensaje(self, asunto=None, remitente=None):
        pass

    @abstractmethod
    def mover_mensaje(self, mensaje, carpeta_destino):
        pass


class IUsuario(ABC):
    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto, cuerpo, servidor):
        pass

    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensajes(self, nombre_carpeta=None):
        pass


class IServidorCorreo(ABC):
    @abstractmethod
    def registrar_usuario(self, usuario):
        pass

    @abstractmethod
    def entregar_mensaje(self, destinatario, mensaje):
        pass

    @abstractmethod
    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        pass



# CLASE MENSAJE


class Mensaje:
    def __init__(self, asunto, cuerpo, remitente):
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.remitente = remitente

    def __str__(self):
        return "Asunto: " + self.asunto + " | Remitente: " + self.remitente



# CARPETA (ÁRBOL GENERAL RECURSIVO)


class Carpeta(ICarpeta):
    def __init__(self, nombre):
        self.nombre = nombre
        self._mensajes = []
        self._subcarpetas = []

    @property
    def mensajes(self):
        return self._mensajes

    @property
    def subcarpetas(self):
        return self._subcarpetas

    def agregar_subcarpeta(self, carpeta):
        if isinstance(carpeta, Carpeta):
            self._subcarpetas.append(carpeta)

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def listar_mensajes(self):
        return self._mensajes

    def buscar_mensaje(self, asunto=None, remitente=None):
        encontrados = []
        for m in self._mensajes:
            if (asunto is None or m.asunto == asunto) and (remitente is None or m.remitente == remitente):
                encontrados.append(m)
        for sub in self._subcarpetas:
            encontrados.extend(sub.buscar_mensaje(asunto, remitente))
        return encontrados

    def eliminar_mensaje(self, mensaje):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            return True
        for sub in self._subcarpetas:
            if sub.eliminar_mensaje(mensaje):
                return True
        return False

    def mover_mensaje(self, mensaje, carpeta_destino):
        if self.eliminar_mensaje(mensaje):
            carpeta_destino.agregar_mensaje(mensaje)
            return True
        return False

    def mostrar_estructura(self, nivel=0):
        print("  " * nivel + "Carpeta: " + self.nombre)
        for m in self._mensajes:
            print("  " * (nivel + 1) + "Mensaje: " + str(m))
        for sub in self._subcarpetas:
            sub.mostrar_estructura(nivel + 1)



# USUARIO


class Usuario(IUsuario):
    def __init__(self, nombre):
        self.nombre = nombre
        self._carpetas = {
            "Bandeja de entrada": Carpeta("Bandeja de entrada"),
            "Enviados": Carpeta("Enviados"),
            "Spam": Carpeta("Spam")
        }

    def recibir_mensaje(self, mensaje):
        self._carpetas["Bandeja de entrada"].agregar_mensaje(mensaje)

    def enviar_mensaje(self, destinatario, asunto, cuerpo, servidor):
        servidor.enviar_mensaje(self.nombre, destinatario, asunto, cuerpo)

    def listar_mensajes(self, nombre_carpeta=None):
        if nombre_carpeta and nombre_carpeta in self._carpetas:
            return self._carpetas[nombre_carpeta].listar_mensajes()
        resultado = []
        for carpeta in self._carpetas.values():
            resultado.extend(carpeta.listar_mensajes())
        return resultado

    def obtener_carpeta(self, nombre):
        return self._carpetas.get(nombre)



# COLA DE PRIORIDADES (URGENTES)


class ColaPrioridades:
    def __init__(self):
        self._cola = []

    def agregar(self, prioridad, mensaje):
        heapq.heappush(self._cola, (prioridad, mensaje))

    def obtener(self):
        if self._cola:
            return heapq.heappop(self._cola)
        return None



# SERVIDOR COMO GRAFO (BFS/DFS)


class ServidorCorreo(IServidorCorreo):
    def __init__(self, nombre):
        self.nombre = nombre
        self._usuarios = {}
        self.conexiones = []
        self.filtros = {}

    def registrar_usuario(self, usuario):
        self._usuarios[usuario.nombre] = usuario

    def conectar(self, servidor):
        if servidor not in self.conexiones:
            self.conexiones.append(servidor)
        if self not in servidor.conexiones:
            servidor.conexiones.append(self)

    def agregar_filtro(self, palabra, carpeta):
        self.filtros[palabra] = carpeta

    def entregar_mensaje(self, destinatario, mensaje):
        if destinatario in self._usuarios:
            usuario = self._usuarios[destinatario]
            for palabra, carpeta in self.filtros.items():
                if palabra in mensaje.asunto.lower():
                    usuario.obtener_carpeta(carpeta).agregar_mensaje(mensaje)
                    return
            usuario.recibir_mensaje(mensaje)

    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        mensaje = Mensaje(asunto, cuerpo, remitente)
        self.entregar_mensaje(destinatario, mensaje)

    # BFS
    def encontrar_ruta_BFS(self, destino):
        visitados = set()
        cola = deque([(self, [self])])
        while cola:
            actual, ruta = cola.popleft()
            if actual == destino:
                return ruta
            visitados.add(actual)
            for vecino in actual.conexiones:
                if vecino not in visitados:
                    cola.append((vecino, ruta + [vecino]))
        return None

    # DFS
    def encontrar_ruta_DFS(self, destino, visitados=None, ruta=None):
        if visitados is None:
            visitados = set()
        if ruta is None:
            ruta = []
        ruta.append(self)
        visitados.add(self)
        if self == destino:
            return ruta
        for vecino in self.conexiones:
            if vecino not in visitados:
                nueva = vecino.encontrar_ruta_DFS(destino, visitados, ruta[:])
                if nueva:
                    return nueva
        return None

    def simular_envio(self, destino, mensaje, metodo="BFS"):
        if metodo == "BFS":
            return self.encontrar_ruta_BFS(destino)
        return self.encontrar_ruta_DFS(destino)
