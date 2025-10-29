import heapq

class GestorUrgentes:
    def __init__(self):
        # La cola guarda tuplas (prioridad, mensaje)
        self.cola = []

    def agregar_mensaje(self, mensaje, prioridad):
        # Agrega un mensaje con su prioridad (1 = más urgente)
        heapq.heappush(self.cola, (prioridad, mensaje))
        print("Mensaje '" + mensaje.asunto + "' agregado con prioridad " + str(prioridad))

    def procesar_mensaje(self):
        # Procesa el mensaje más urgente
        if self.cola:
            prioridad, mensaje = heapq.heappop(self.cola)
            print("Procesando mensaje urgente: " + mensaje.asunto + " (Prioridad " + str(prioridad) + ")")
        else:
            print("No hay mensajes urgentes para procesar.")
