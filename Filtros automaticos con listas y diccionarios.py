class Mensaje:
    def __init__(self, asunto, texto, remitente):
        self.asunto = asunto
        self.texto = texto
        self.remitente = remitente

    def __str__(self):
        return "Asunto: " + self.asunto + " - De: " + self.remitente
class ServidorCorreo:
    def __init__(self):
        # Diccionario para guardar carpetas y sus mensajes
        self.carpetas = {
            "Bandeja de entrada": [],
            "Trabajo": [],
            "Amigos": [],
            "Otros": []
        }

        # Diccionario de filtros automáticos
        self.filtros = {}

    def agregar_filtro(self, palabra_clave, carpeta_destino):
        # Agrega una regla de filtrado automática
        self.filtros[palabra_clave.lower()] = carpeta_destino

    def recibir_mensaje(self, mensaje):
        # Organiza el mensaje automáticamente según los filtros
        for palabra, carpeta in self.filtros.items():
            if palabra in mensaje.asunto.lower() or palabra in mensaje.texto.lower():
                self.carpetas[carpeta].append(mensaje)
                print("Mensaje '" + mensaje.asunto + "' enviado a la carpeta '" + carpeta + "'")
                return
        # Si no coincide con ningún filtro, va a la bandeja principal
        self.carpetas["Bandeja de entrada"].append(mensaje)
        print("Mensaje '" + mensaje.asunto + "' enviado a la Bandeja de entrada")
