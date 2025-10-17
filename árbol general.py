# árbol general
class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcarpetas = []  # Lista de subcarpetas

    def agregar_subcarpeta(self, subcarpeta):
        """Agrega una subcarpeta dentro de la carpeta actual."""
        if isinstance(subcarpeta, Carpeta):
            self.subcarpetas.append(subcarpeta)

    def mostrar_estructura(self, nivel=0):
        """Muestra la estructura jerárquica de carpetas."""
        print('  ' * nivel + "Carpeta: " + self.nombre)
        for sub in self.subcarpetas:
            sub.mostrar_estructura(nivel + 1)

# Carpeta raíz
bandeja = Carpeta("Bandeja de Entrada")

# Subcarpetas principales
trabajo = Carpeta("Trabajo")
personal = Carpeta("Personal")

# Subcarpetas dentro de "Trabajo"
proyectos = Carpeta("Proyectos")

# Construcción del árbol
bandeja.agregar_subcarpeta(trabajo)
bandeja.agregar_subcarpeta(personal)
trabajo.agregar_subcarpeta(proyectos)

# Mostrar el árbol
bandeja.mostrar_estructura()
