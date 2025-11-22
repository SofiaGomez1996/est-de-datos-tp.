def aplicar_filtros(usuario, reglas):
    #reglas, es un diccionario: {"Trabajo": ["asunto1", "asunto2"]}

    for nombre_carpeta, palabras in reglas.items():
        carpeta_destino = usuario.carpetas.get(nombre_carpeta)

        if carpeta_destino:
            #recorre bandeja de entrada
            nuevos = []
            for msg in usuario.bandeja.mensajes:
                if any(p in msg.asunto for p in palabras):
                    carpeta_destino.agregar_mensaje(msg)
                else:
                    nuevos.append(msg)

            usuario.bandeja.mensajes = nuevos