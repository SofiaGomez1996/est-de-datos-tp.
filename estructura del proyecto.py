proyecto_correo/
│
├── main.py
├── cli.py
│
├── src/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── mensaje.py
│   │   ├── usuario.py
│   │   ├── carpeta.py
│   │   ├── servidor_correo.py
│   │   ├── filtros.py
│   │   ├── cola_prioridad.py
│   │   ├── grafo_servidores.py
│   │
│   ├── interfaces/
│       ├── __init__.py
│       ├── icarpeta.py
│       ├── iusuario.py
│       ├── iservidor.py
│
└── docs/
    ├── diagramas_clases.pdf
    ├── arquitectura.txt
    ├── decisiones_disenio.txt


Qué contiene cada archivo
main.py
Punto de entrada principal del sistema.
Carga usuarios.
Crea el servidor.
Arranca el CLI.
cli.py

Interfaz de línea de comandos.
Menú de:
enviar mensajes
ver bandeja
crear subcarpetas
mover mensajes
aplicar filtros
ver árbol
usar BFS/DFS para servidores

 src/interfaces/
icarpeta.py
Interfaz abstracta de Carpeta.

iusuario.py
Interfaz de Usuario.

iservidor.py
Interfaz de ServidorCorreo.

📁 src/models/
mensaje.py
Clase Mensaje.
usuario.py
Usuario con:
bandeja
enviados
papelera
carpetas dinámicas
filtros
carpeta.py
Árbol de carpetas:
agregar subcarpetas
mover mensaje recursivo
búsqueda recursiva
mostrar árbol
    
servidor_correo.py
Envío de mensajes
Registro de usuarios

Entrega
Uso opcional de grafo para simular envío distribuido

filtros.py
Reglas como diccionario
Aplicación automática:
filtrar por remitente
por palabra clave
por prioridad

cola_prioridad.py
Implementación de heap para mensajes urgentes.

grafo_servidores.py
Modelo de red de servidores
BFS
DFS
    
