def aplicar_filtros(mensajes, filtros):
    # filtros es un diccionario con palabras clave: nombre_carpeta
    # ejemplo: {"urgente": "Prioritarios", "trabajo": "Laboral"}
    resultado = {}

    for palabra, carpeta in filtros.items():
        resultado[carpeta] = []
        for m in mensajes:
            if palabra in m["asunto"].lower():
                resultado[carpeta].append(m)

    return resultado
