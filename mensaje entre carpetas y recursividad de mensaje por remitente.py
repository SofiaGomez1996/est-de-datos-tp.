
# TRABAJO PRÁCTICO - ENTREGA 2
# ESTRUCTURAS DE DATOS Y RECURSIVIDAD

class Carpeta:
    def __init__(self, nombre):
        # Constructor de la clase Carpeta.
        # Cada carpeta puede contener subcarpetas y mensajes.
        self.nombre = nombre
        self.mensajes = []      # Lista de mensajes (diccionarios con asunto y remitente)
        self.subcarpetas = []   # Lista de objetos Carpeta

    # MÉTODOS DE GESTIÓN DE CARPETAS
    def agregar_subcarpeta(self, subcarpeta):
        """Agrega una subcarpeta dentro de la carpeta actual."""
        if isinstance(subcarpeta, Carpeta):
            self.subcarpetas.append(subcarpeta)

    # MÉTODOS DE GESTIÓN DE MENSAJES
    def agregar_mensaje(self, asunto, remitente):
        """Agrega un nuevo mensaje a la carpeta."""
        self.mensajes.append({'asunto': asunto, 'remitente': remitente})

    def eliminar_mensaje(self, asunto, remitente):
        """
        Elimina un mensaje por asunto y remitente.
        Si no está en la carpeta actual, busca recursivamente en las subcarpetas.
        Retorna el mensaje eliminado o None si no se encontró.
        """
        # Buscar en la carpeta actual
        for mensaje in self.mensajes:
            if mensaje['asunto'] == asunto and mensaje['remitente'] == remitente:
                self.mensajes.remove(mensaje)
                return mensaje

        # Búsqueda recursiva en subcarpetas
        for sub in self.subcarpetas:
            resultado = sub.eliminar_mensaje(asunto, remitente)
            if resultado:
                return resultado
        return None

    def mover_mensaje(self, asunto, remitente, carpeta_destino):
        """
        Mueve un mensaje desde esta carpeta (o subcarpeta) a otra carpeta destino.
        """
        mensaje = self.eliminar_mensaje(asunto, remitente)
        if mensaje:
            carpeta_destino.mensajes.append(mensaje)
            return True
        return False

    # MÉTODOS DE BÚSQUEDA
    def buscar_mensaje(self, asunto, remitente):
        """Busca un mensaje por asunto y remitente recursivamente."""
        # Buscar en la carpeta actual
        for mensaje in self.mensajes:
            if mensaje['asunto'] == asunto and mensaje['remitente'] == remitente:
                return mensaje

        # Buscar recursivamente en subcarpetas
        for sub in self.subcarpetas:
            resultado = sub.buscar_mensaje(asunto, remitente)
            if resultado:
                return resultado
        return None

    def buscar_por_remitente(self, remitente):
        """
        Busca recursivamente todos los mensajes de un remitente.
        Retorna una lista de mensajes.
        """
        encontrados = [m for m in self.mensajes if m['remitente'] == remitente]
        for sub in self.subcarpetas:
            encontrados.extend(sub.buscar_por_remitente(remitente))
        return encontrados

    # VISUALIZACIÓN DE LA ESTRUCTURA
    def mostrar_estructura(self, nivel=0):
        """
        Muestra por pantalla la estructura jerárquica de carpetas y mensajes.
        Utiliza recursividad para imprimir todo el árbol.
        """
        print('  ' * nivel + "Carpeta: " + self.nombre)
        for mensaje in self.mensajes:
            print('  ' * (nivel + 1) + "Mensaje: " + mensaje['asunto'] + " - " + mensaje['remitente'])
        for sub in self.subcarpetas:
            sub.mostrar_estructura(nivel + 1)

  
    



