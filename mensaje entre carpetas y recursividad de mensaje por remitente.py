class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []  # Lista de mensajes: {'asunto': ..., 'remitente': ...}
        self.subcarpetas = []

    def agregar_subcarpeta(self, subcarpeta):
        self.subcarpetas.append(subcarpeta)

    def agregar_mensaje(self, asunto, remitente):
        self.mensajes.append({'asunto': asunto, 'remitente': remitente})

    def mostrar_estructura(self, nivel=0):
        print('  ' * nivel + f" {self.nombre}")
        for mensaje in self.mensajes:
            print('  ' * (nivel + 1) + f" {mensaje['asunto']} - {mensaje['remitente']}")
        for sub in self.subcarpetas:
            sub.mostrar_estructura(nivel + 1)

    def buscar_mensaje(self, asunto, remitente):
        for mensaje in self.mensajes:
            if mensaje['asunto'] == asunto and mensaje['remitente'] == remitente:
                return mensaje
        for sub in self.subcarpetas:
            resultado = sub.buscar_mensaje(asunto, remitente)
            if resultado:
                return resultado
        return None

    def eliminar_mensaje(self, asunto, remitente):
        for mensaje in self.mensajes:
            if mensaje['asunto'] == asunto and mensaje['remitente'] == remitente:
                self.mensajes.remove(mensaje)
                return mensaje
        for sub in self.subcarpetas:
            resultado = sub.eliminar_mensaje(asunto, remitente)
            if resultado:
                return resultado
        return None

    def buscar_por_remitente(self, remitente):
        encontrados = [m for m in self.mensajes if m['remitente'] == remitente]
        for sub in self.subcarpetas:
            encontrados.extend(sub.buscar_por_remitente(remitente))
        return encontrados
