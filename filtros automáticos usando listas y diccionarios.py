# Ejemplo de mensajes
mensajes =[
    {"remitente": "profesor@uni.edu", "asunto": "Tarea", "etiquetas": ["importante"]},
    {"remitente": "spam@promo.com", "asunto": "Oferta", "etiquetas": ["spam"]},
    {"remitente": "amigo@mail.com", "asunto": "Reunión", "etiquetas": ["personal"]}]

# Reglas definidas por el usuario
reglas = {
    "importante": [],
    "spam": [],
    "personal": []}

# Filtro automático
for mensaje in mensajes:
    for etiqueta in mensaje["etiquetas"]:
        if etiqueta in reglas:
            reglas[etiqueta].append(mensaje)

# Resultado
for categoria, lista in reglas.items():
    print(f"\nMensajes en '{categoria}':")
    for m in lista:
        print(f"  - {m['asunto']} de {m['remitente']}")
