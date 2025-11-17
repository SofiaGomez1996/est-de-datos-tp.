from sistema_correo import SistemaCorreo

def mostrar_menu():
    print("Menu del Cliente de Correo")
    print("1. Iniciar sesion")
    print("2. Enviar mensaje")
    print("3. Ver bandeja de entrada")
    print("4. Ver carpetas")
    print("5. Salir")

def main():
    sistema = SistemaCorreo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuario = input("Nombre de usuario: ")
            sistema.iniciar_sesion(usuario)

        elif opcion == "2":
            remitente = input("Su usuario: ")
            destinatario = input("Destinatario: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")
            sistema.enviar_mensaje(remitente, destinatario, asunto, contenido)

        elif opcion == "3":
            usuario = input("Usuario: ")
            mensajes = sistema.ver_bandeja_entrada(usuario)
            for m in mensajes:
                print("De: ", m.remitente)
                print("Asunto: ", m.asunto)
                print("Contenido: ", m.contenido)
                print("----")

        elif opcion == "4":
            usuario = input("Usuario: ")
            sistema.ver_carpetas(usuario)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()
