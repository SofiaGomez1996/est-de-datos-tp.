                                             Servicio de Correo Electrónico
           CORREO EXPRESS
PARTE 1:                           
Para modelar un cliente de correo electrónico, se definen cuatro clases principales:
🔹MENSAJE:
 Esta clase representa un correo. Tiene los datos básicos de un mensaje: quién lo envía, a quién va, el asunto y el contenido.
🔹CARPETA:
 Representa una carpeta de correos, como "Bandeja de entrada" o "Enviados". Guarda una lista de mensajes.
🔹USUARIO:
 Es el que usa el sistema. Cada usuario tiene un nombre, una bandeja de entrada y una carpeta de enviados.
🔹SERVIDOR CORREO:
 Es el que conecta a los usuarios. Se encarga de entregar los mensajes.

🔹Encapsular significa proteger los datos internos de cada clase para que no se puedan modificar directamente desde afuera. Para eso, se uso doble guión bajo__delante de cada atributo.
ej: self.__remitente
Esto hace que esos atributos sean privados. Nadie desde afuera puede acceder a ello directamente.

🔹Para poder leer esos atributos privados sin romper la encapsulación, optamos por usar propiedades con el decorador @property
 ej: En la clase mensaje                                @property                                                   def remitente(self):                       
@property                                                   def destinatario(self):                                           return self.__destinatario

 -Esto permite acceder al valor como si fuera un atributo, pero en realidad es un método que lo devuelve de forma segura.                                 
🔹La interfaz en este caso son los métodos públicos que permiten usar el sistema. Está definido en la clase Usuario , el cual interactúa con los mensajes.

🔹ENVIAR MENSAJE
Este método:
• Crea un mensaje
• Lo guarda en la carpeta de enviados
• Le pide al servidor que lo entregue al destinatario

🔹RECIBIR MENSAJE 
Este método:
• Guarda el mensaje en la bandeja de entrada del usuario

🔹LISTAR MENSAJES 
Estos métodos:
• Devuelven una lista de mensajes en formato legible     

PARTE 2:
🔹Estructuras de Datos y Recursividad
Se implementó un sistema de gestión de carpetas y mensajes utilizando una estructura recursiva (árbol general). Cada carpeta puede contener mensajes y subcarpetas, permitiendo organizar la información de manera jerárquica y flexible.

El sistema permite realizar operaciones esenciales como:
 Agregar y eliminar mensajes en carpetas y subcarpetas.
 Crear nuevas subcarpetas dentro de cualquier carpeta.
 Buscar mensajes por asunto o remitente de manera recursiva.
 Mover mensajes entre carpetas, manteniendo la consistencia del árbol.

🔹 Estructura de datos
 Carpeta: nodo del árbol que contiene:
 Nombre de la carpeta.
 Lista de mensajes asociados.
Lista de subcarpetas, cada una con la misma estructura.
🔹Árbol general: cada carpeta puede tener múltiples subcarpetas, generando una jerarquía recursiva. Esto permite que cualquier operación se aplique en toda la estructura de manera uniforme.

🔹Operaciones implementadas
 Agregar mensajes: se añaden al final de la lista de mensajes de la carpeta.
 Eliminar mensajes: se busca y elimina un mensaje por asunto en la carpeta y todas sus subcarpetas.
 Buscar mensajes: se realiza de manera recursiva, por asunto o remitente, recorriendo toda la estructura.
 Agregar subcarpetas: permite crear nuevas ramas en el árbol de carpetas.
 Mover mensajes: combina búsqueda, eliminación y agregado en otra carpeta destino.
 🔹Análisis de eficiencia
 n representa la cantidad total de mensajes en la carpeta y todas sus subcarpetas.

La recursividad permite recorrer automáticamente todas las subcarpetas sin necesidad de iteraciones manuales.
 
PARTE 3:
🔹Algoritmos y Funcionalidades Avanzadas
En esta entrega agregamos nuevas funcionalidades al sistema de correo que había hecho antes. La idea fue hacerlo más completo y parecido a un correo real, pero aplicando estructuras de datos como listas, diccionarios y colas de prioridad.
🔹 Filtros automáticos con listas y diccionarios
Primero, implementamos un sistema de filtros automáticos.
La idea es que el usuario pueda definir reglas para que los mensajes se organicen automáticamente.
Por ejemplo:
 Si el remitente es “profesor@correo.com
”, el mensaje va directo a la carpeta “Universidad”.
Si el asunto contiene la palabra “URGENTE”, el mensaje se marca como prioritario.
 Para esto usamos un diccionario llamado filtros, donde cada clave representa una condición (como el remitente o el asunto), y el valor es la carpeta de destino.
 Cuando llega un nuevo mensaje, el sistema recorre la lista de filtros y lo guarda en la carpeta correspondiente.
Si no cumple ningún filtro, se guarda en “Bandeja de entrada”.
Esto lo hicimos usando listas (para almacenar los mensajes) y diccionarios (para guardar las reglas de clasificación).
🔹 Cola de prioridades para mensajes urgentes
Después agregamos una cola de prioridad, que sirve para manejar los mensajes urgentes.
La cola de prioridad me permite que los mensajes con mayor importancia se procesen antes.

Cada mensaje tiene un nivel de prioridad:
1 → Normal
2 → Importante
3 → Urgente
Cuando llega un mensaje urgente, se agrega a la cola de prioridad.
Después, al mostrar o procesar mensajes, el sistema siempre atiende primero los de mayor prioridad.
Esto lo implementamos usando una lista ordenada, donde los mensajes se insertan según su prioridad

🔹 Organización general del código
 El sistema tiene las clases principales:
Mensaje: guarda el contenido, remitente, asunto y prioridad.
Carpeta: contiene los mensajes y subcarpetas.
ServidorCorreo: maneja los filtros, las carpetas y la cola de prioridad.
Los filtros se aplican automáticamente cuando llega un mensaje nuevo, y si es urgente, también se agrega a la cola.

Con esta entrega aplicamos estructuras de datos más avanzadas:
Listas para almacenar mensajes.
Diccionarios para los filtros automáticos.
Cola de prioridad para manejar urgencias.
 El objetivo fue mejorar la organización y eficiencia del sistema de correo, haciendo que las operaciones de clasificación y prioridad se realicen de forma automática y ordenada.

🔹A su vez, fuimos modificando archivos tanto de la parte 1,2 como la parte 3, para que el main pueda tener una función correcta.

PARTE 4:
🔹Integración y presentación:
En está última entrega lo que hicimos fue enfocarnos en integrar las funciones que desarrollamos en entregas anteriores (entrega 1, entrega 2, y entrega 3)
Para ello, juntamos las clases y módulos del sistema
Implementamos todas las fuciones en un archivo principal
Y a su vez, implementamos una interfaz de usuario 
🔹La idea principal, es que cualquier usuario pudiera acceder a las funciones principales del proyecto de forma clara y sencilla, esto a través de un menú interactivo con opciones como "Registrar o Gestionar Datos".
Esto a su vez, nos lleva a pertmitir verificar que todas las partes del sistema funcionen de manera correcta al unirlas.
🔹Luego, en la domuntación de código, agregamos comentarios, métodos y atributos.
🔹Creamos un achivo README.md donde explicamos el paso a paso del proyecto, como se instala, como se ejecuta, expliamos como creamos cada entrega, la resolución que utilizamos y el mantenimiento del código que llevamos a cabo.
🔹Organizamos el proyecto y lo fuimos subiendo al repositorio GitHub.
-En está misma lo que hicimos fue crear diferentes archivos/carpetas de manera ordenadas.
-Incuimos los diferentes códigos, con y sin funcionamiento, y a su vez los diferentes documentos requeridos.
-Trabajamos en conjunto, siendo tres integrantes, dividiendonos diferentes etapas del dicho proyecto.
- En cada entrega subimos al repositorio lo corresponiente a cada entrega, en tiempo y forma.
- Usamos el Git para cada entrega, dejando evidencias de los diferentes cambios que fuimos haciendo a lo largo del proyecto y de cada entrega, a su vez dejando evidencia de cada colaboración en conjunto como ajustes y haciendo funcionar el main.

  En conclusión, seguimos trabajando para darle un cierre correspondiente y demostrar el funcionamiento, a su vez preparandonos para la defensa para poder demostrar lo entendido, lo aprendido y nuestro rendimiento siendo muy capaz.

