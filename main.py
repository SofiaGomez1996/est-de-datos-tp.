from usuario import Usuario
from servidor import ServidorCorreo
from filtros import aplicar_filtros
from cola_prioridades import ColaPrioridades

# Crear servidor y usuarios
servidor = ServidorCorreo()
sofi = Usuario("Sofi@correo.com")
luci = Usuario("Luci@correo.com")
bianco = Usuario("Profe_Bianco@profe.com")

# Registrar usuarios
servidor.registrar_usuario(sofi)
servidor.registrar_usuario(luci)
servidor.registrar_usuario(bianco)

# Sofi envía mensajes
sofi.enviar_mensaje(luci, "Entrega urgente del TP", "No te olvides de subir el trabajo", servidor)
sofi.enviar_mensaje(bianco, "Consulta sobre nota", "Hola profe, quería preguntar por la nota del tp", servidor)

# Mostrar bandeja de entrada de Luci
print("\nMensajes de Luci:")
luci.inbox.listar_mensajes()

# Aplicar filtros automáticos
mensajes = luci.inbox.mensajes
filtros = {"urgente": "Prioritarios"}
clasificados = aplicar_filtros(mensajes, filtros)
print("\nMensajes clasificados por filtros:", clasificados)

# Usar cola de prioridades
cola = ColaPrioridades()
cola.agregar_mensaje(1, {"asunto": "Entrega urgente del TP"})
cola.agregar_mensaje(3, {"asunto": "Otros"})
print("\nMensaje más urgente:", cola.obtener_siguiente())