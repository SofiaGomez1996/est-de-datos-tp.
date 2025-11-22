class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self.remitente = remitente #nombre del que envía
        self.destinatario = destinatario #nombre del que recibe
        self.asunto = asunto
        self.contenido = contenido

    def mostrar(self):
        return f"De: {self.remitente}\nPara: {self.destinatario}\nAsunto: {self.asunto}\n{self.contenido}"