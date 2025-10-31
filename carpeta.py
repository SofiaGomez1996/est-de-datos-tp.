class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []  # lista de diccionarios o Mensajes
        self.subcarpetas = []  # lista de Carpetas hijas

    def agregar_mensaje(self, asunto, remitente):
        self.mensajes.append({"asunto": asunto, "remitente": remitente})

    def agregar_subcarpeta(self, carpeta):
        self.subcarpetas.append(carpeta)

    def listar_mensajes(self):
        for m in self.mensajes:
            print(f"Asunto: {m['asunto']} - De: {m['remitente']}")

    def buscar_mensaje(self, asunto=None, remitente=None):
        resultados = []
        for m in self.mensajes:
            if (asunto and asunto in m["asunto"]) or (remitente and remitente in m["remitente"]):
                resultados.append(m)

        # Buscar también en las subcarpetas (recursivamente)
        for sub in self.subcarpetas:
            resultados.extend(sub.buscar_mensaje(asunto, remitente))

        return resultados

    def mover_mensaje(self, asunto, remitente, carpeta_destino):
        # Busca el mensaje y lo mueve si lo encuentra
        for m in self.mensajes:
            if m["asunto"] == asunto and m["remitente"] == remitente:
                carpeta_destino.mensajes.append(m)
                self.mensajes.remove(m)
                return True

        # Si no está, busca en subcarpetas
        for sub in self.subcarpetas:
            if sub.mover_mensaje(asunto, remitente, carpeta_destino):
                return True

        return False