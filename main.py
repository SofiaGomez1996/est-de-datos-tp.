# main.py
# Cliente de correo - 

from codigo_cliente_correo import Usuario, ServidorCorreo, Carpeta

def mostrar_menu():
    print("\n----- CLIENTE DE CORREO -----")
    print("1 - Ver bandeja de entrada")
    print("2 - Ver carpeta Trabajo")
    print("3 - Enviar mensaje")
    print("4 - Ver todos los mensajes")
    print("5 - Salir")
    return input("Elegí una opción: ")


def mostrar_carpeta(usuario, nombre_carpeta):
    carpeta = usuario.obtener_carpeta(nombre_carpeta)
    if carpeta:
        mensajes = carpeta.listar_mensajes()
        print("\n--- " + nombre_carpeta + " ---")
        if not mensajes:
            print("(vacío)")
        else:
            for m in mensajes:
                print(str(m))
    else:
        print("La carpeta no existe.")


def enviar_mensaje_desde_cli(remitente, servidor):
    print("\n--- Enviar mensaje ---")
    destinatario = input("Destinatario: ")
    asunto = input("Asunto: ")
    cuerpo = input("Cuerpo: ")
    remitente.enviar_mensaje(destinatario, asunto, cuerpo, servidor)
    print("Mensaje enviado correctamente.")


def main():
    # Crear servidor
    servidor = ServidorCorreo("ServidorCentral")

    # Crear usuarios
    sofia = Usuario("Lucia")
    profe = Usuario("Profe")

    # Registrar usuarios
    servidor.registrar_usuario(Lucia)
    servidor.registrar_usuario(profe)

    # Crear subcarpeta de trabajo
    trabajo = Carpeta("Trabajo")
    Lucia.obtener_carpeta("Bandeja de entrada").agregar_subcarpeta(trabajo)

    # Filtro: mensaje con “tp” -> carpeta Trabajo
    servidor.agregar_filtro("tp", "Trabajo")

    # CLI
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_carpeta(Lucia, "Bandeja de entrada")

        elif opcion == "2":
            mostrar_carpeta(Lucia, "Trabajo")

        elif opcion == "3":
            enviar_mensaje_desde_cli(profe, servidor)

        elif opcion == "4":
            print("\n--- TODOS LOS MENSAJES ---")
            todos = Lucia.listar_mensajes()
            if not todos:
                print("(vacío)")
            else:
                for m in todos:
                    print(str(m))

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
