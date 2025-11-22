from usuario import Usuario
from servidor import ServidorCorreo
from filtros import aplicar_filtros

def menu():
    print("\n--- MENU CORREO ---")
    print("1 - Cambiar usuario")
    print("2 - Ver bandeja de entrada")
    print("3 - Ver enviados")
    print("4 - Ver Trabajo")
    print("5 - Ver Personal")
    print("6 - Enviar mensaje")
    print("7 - Marcar urgente")
    print("8 - Ver urgentes")
    print("9 - Aplicar filtros")
    print("10 - Salir")
    return input("Opción: ")

def elegir_usuario(usuarios):
    print("\nUsuarios:")
    for i, u in enumerate(usuarios):
        print(f"{i+1} - {u.nombre}")

    op = input("Elegí usuario: ")
    try:
        indice = int(op) - 1
        return usuarios[indice]
    except:
        print("Inválido.")
        return None

def elegir_mensaje(carpeta):
    if not carpeta.mensajes:
        print("No hay mensajes.")
        return None

    print("\nMensajes:")
    for i, m in enumerate(carpeta.mensajes):
        print(f"{i+1} - {m.asunto} (De {m.remitente})")

    op = input("Elegí: ")
    try:
        indice = int(op) - 1
        return carpeta.mensajes[indice]
    except:
        print("Inválido.")
        return None

def main():
    servidor = ServidorCorreo("S1")

    sofi = Usuario("Sofi")
    luci = Usuario("Luci")
    profe = Usuario("Bianco")

    usuarios = [sofi, luci, profe]
    for u in usuarios:
        servidor.registrar_usuario(u)

    actual = sofi

    while True:
        print(f"\nUsuario actual: {actual.nombre}")
        op = menu()

        if op == "1":
            nuevo = elegir_usuario(usuarios)
            if nuevo:
                actual = nuevo

        elif op == "2":
            for m in actual.bandeja.listar_mensajes():
                print(m)

        elif op == "3":
            for m in actual.enviados.listar_mensajes():
                print(m)

        elif op == "4":
            for m in actual.carpetas["Trabajo"].listar_mensajes():
                print(m)

        elif op == "5":
            for m in actual.carpetas["Personal"].listar_mensajes():
                print(m)

        elif op == "6":
            dest = input("A quién (Sofi/Luci/Bianco): ")

            if dest == "Sofi":
                d = sofi
            elif dest == "Luci":
                d = luci
            elif dest == "Bianco":
                d = profe
            else:
                print("Inválido.")
                continue

            asunto = input("Asunto: ")
            cuerpo = input("Mensaje: ")
            actual.enviar_mensaje(d, asunto, cuerpo, servidor)
            print("Enviado.")

        elif op == "7":
            msg = elegir_mensaje(actual.bandeja)
            if msg:
                actual.marcar_como_urgente(msg)
                print("Marcado.")

        elif op == "8":
            for m in actual.urgentes.obtener_todos():
                print(m)

        elif op == "9":
            reglas = {
                "Trabajo": ["TP", "informe"],
                "Personal": ["cumple", "hola"]
            }
            aplicar_filtros(actual, reglas)
            print("Filtros aplicados.")

        elif op == "10":
            print("Adios")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()