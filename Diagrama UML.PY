INTERFACES:
interface ICarpeta {
    +agregar_mensaje(mensaje)
    +listar_mensajes()
    +buscar_mensaje(asunto, remitente)
    +mover_mensaje(mensaje, carpeta_destino)}

interface IUsuario {
    +enviar_mensaje(destinatario, asunto, cuerpo, servidor)
    +recibir_mensaje(mensaje)
    +listar_mensajes(nombre_carpeta)}

interface IServidorCorreo {
    +registrar_usuario(usuario)
    +entregar_mensaje(destinatario, mensaje)
    +enviar_mensaje(remitente, destinatario, asunto, cuerpo)}

CLASE MENSAJE
class Mensaje {
    -asunto : str
    -cuerpo : str
    -remitente : str
    -prioridad : int
    +__str__()}

CLASE CARPETA
class Carpeta {
    -nombre : str
    -_mensajes : List<Mensaje>
    -_subcarpetas : List<Carpeta>
    +agregar_subcarpeta(carpeta)
    +agregar_mensaje(mensaje)
    +listar_mensajes()
    +buscar_mensaje(asunto, remitente)
    +eliminar_mensaje(mensaje)
    +mover_mensaje(mensaje, carpeta_destino)}

Carpeta ..|> ICarpeta

USUARIO:
class Usuario {
    -nombre : str
    -_carpetas : Dict
    -_urgentes : List
    +recibir_mensaje(mensaje)
    +enviar_mensaje(destinatario, asunto, cuerpo, servidor)
    +listar_mensajes(nombre_carpeta)
    +obtener_carpeta(nombre)}

Usuario ..|> IUsuario

COLA DE PRIORIDADES:
class ColaPrioridades {
    -_cola : List
    +agregar(prioridad, mensaje)
    +obtener()}

SERVIDOR CORREO:
class ServidorCorreo {
    -nombre : str
    -_usuarios : Dict<str, Usuario>
    -conexiones : List<ServidorCorreo>
    -filtros : Dict
    +registrar_usuario(usuario)
    +conectar(servidor)
    +agregar_filtro(palabra, carpeta_destino)
    +entregar_mensaje(destinatario, mensaje)
    +enviar_mensaje(remitente, destinatario, asunto, cuerpo)
    +encontrar_ruta_BFS(destino)
    +encontrar_ruta_DFS(destino, visitados, ruta)}

ServidorCorreo ..|> IServidorCorreo

RELACIONES PRINCIPALES:
Usuario "1" --> "*" Carpeta : contiene >
Usuario "1" --> "*" Mensaje : recibe >
Carpeta "1" --> "*" Mensaje : almacena >
Carpeta "1" --> "*" Carpeta : subcarpetas >

ServidorCorreo "1" --> "*" Usuario : gestiona >
ServidorCorreo "1" --> "*" ServidorCorreo : conecta >

@enduml
