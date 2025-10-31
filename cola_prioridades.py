import heapq  # módulo que maneja colas de prioridad

class ColaPrioridades:
    def __init__(self):
        self.cola = []

    def agregar_mensaje(self, prioridad, mensaje):
        # prioridad: número, mientras menor, más urgente
        heapq.heappush(self.cola, (prioridad, mensaje))

    def obtener_siguiente(self):
        # Devuelve el mensaje más urgente
        if self.cola:
            return heapq.heappop(self.cola)
        return None