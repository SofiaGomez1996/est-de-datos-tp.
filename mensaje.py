class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo

    def mostrar(self):
        # Devuelve el mensaje en forma de texto
        return f"De: {self.remitente} - Para: {self.destinatario}\nAsunto: {self.asunto}\n{self.cuerpo}\n"