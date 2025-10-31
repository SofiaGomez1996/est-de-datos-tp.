class ServidorCorreo:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.nombre] = usuario

    def entregar_mensaje(self, destinatario, mensaje):
        if destinatario.nombre in self.usuarios:
            self.usuarios[destinatario.nombre].recibir_mensaje(mensaje)
        else:
            print(f"No existe el destinatario {destinatario.nombre}")