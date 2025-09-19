                                                    Servicio de Correo Electrónico
              CORREO EXPRESS
                           
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
