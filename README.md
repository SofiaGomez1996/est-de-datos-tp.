                                             Servicio de Correo Electrónico
           CORREO EXPRESS
PARTE 1:                           
Para modelar un cliente de correo electrónico, se definen cuatro clases principales:
MENSAJE:
 Esta clase representa un correo. Tiene los datos básicos de un mensaje: quién lo envía, a quién va, el asunto y el contenido.
CARPETA:
 Representa una carpeta de correos, como "Bandeja de entrada" o "Enviados". Guarda una lista de mensajes.
USUARIO:
 Es el que usa el sistema. Cada usuario tiene un nombre, una bandeja de entrada y una carpeta de enviados.
SERVIDOR CORREO:
 Es el que conecta a los usuarios. Se encarga de entregar los mensajes.

Encapsular significa proteger los datos internos de cada clase para que no se puedan modificar directamente desde afuera. Para eso, se uso doble guión bajo__delante de cada atributo.
ej: self.__remitente
Esto hace que esos atributos sean privados. Nadie desde afuera puede acceder a ello directamente.

Para poder leer esos atributos privados sin romper la encapsulación, optamos por usar propiedades con el decorador @property
 ej: En la clase mensaje                                @property                                                   def remitente(self):                       
@property                                                   def destinatario(self):                                           return self.__destinatario

 -Esto permite acceder al valor como si fuera un atributo, pero en realidad es un método que lo devuelve de forma segura.                                 
La interfaz en este caso son los métodos públicos que permiten usar el sistema. Está definido en la clase Usuario , el cual interactúa con los mensajes.

ENVIAR MENSAJE
Este método:
• Crea un mensaje
• Lo guarda en la carpeta de enviados
• Le pide al servidor que lo entregue al destinatario

RECIBIR MENSAJE 
Este método:
• Guarda el mensaje en la bandeja de entrada del usuario

LISTAR MENSAJES 
Estos métodos:
• Devuelven una lista de mensajes en formato legible      

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

