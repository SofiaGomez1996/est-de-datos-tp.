              Servicio de Correo Electrónico:Cliente_Correo

              
# 📧 Cliente de Correo – Proyecto en Python

**Proyecto final de la cátedra Estructuras de Datos – UNaB (2025)**
Implementación completa de un **cliente de correo electrónico** en Python, cumpliendo todos los requisitos del Trabajo Práctico: orientación a objetos, recursividad, estructuras de datos avanzadas, filtros, cola de prioridades y simulación de red mediante grafos.

## Integrantes del grupo
**Soto,Lucia**_
**Lepin,Ian**_
**Gomez,Sofia**_email: marianosofia54@gmail.com

##  Objetivo del Proyecto

Modelar un sistema de correo electrónico que permita:

* Crear usuarios.
* Enviar y recibir mensajes.
* Organizar mensajes en carpetas y subcarpetas (árbol general recursivo).
* Implementar filtros automáticos.
* Manejar mensajes urgentes con una **cola de prioridades (heap)**.
* Simular una red de servidores mediante un **grafo** con BFS y DFS.
* Exponer todas las funcionalidades mediante una **interfaz CLI simple**.

El enfoque del proyecto está en el **uso correcto de estructuras de datos**, **encapsulamiento**, **recursividad**, **colecciones eficientes** y **algoritmos de recorrida de grafos**.


##  Funcionalidades Implementadas

## Sistema completo de usuarios

Cada usuario posee:

* Bandeja de entrada
* Spam
* Enviados
* Estructura jerárquica de carpetas
* Cola de prioridades para urgentes

## Clase *Carpeta* como árbol recursivo

Permite:
* Subcarpetas ilimitadas
* Búsqueda recursiva por asunto o remitente
* Mover mensajes entre carpetas

## Filtros automáticos

El servidor permite crear reglas como:
> Si el asunto contiene "tp", mover a la carpeta "Trabajo".

##Cola de mensajes urgentes (heap)
 Mensajes con prioridad 1 se encolan automáticamente.

## Grafo de servidores

Permite modelar una red realista con:
* BFS (ruta más corta)
* DFS (cualquier ruta válida)

## CLI (Interfaz de Línea de Comandos)

Desde *main.py* el usuario puede:
* Ver bandeja de entrada
* Ver subcarpetas
* Enviar mensajes
* Ver todos los mensajes recibidos

## Estructura del Proyecto

cliente_correo/
│
├── codigo_cliente_correo.py   # Clases principales: Usuario, Carpeta, Servidor, Mensaje...
├── main.py                    # Interfaz CLI
└── README.md                  # Este archivo


##  Tecnologías y Librerías Usadas

Este proyecto está desarrollado **100% en Python**, utilizando únicamente librerías estándar:

## Librerías usadas

* `heapq` → implementación de cola de prioridades.
* `collections.deque` → soporte eficiente para BFS.
* `typing` → anotaciones de tipo para claridad del código.
* `abc` → definición de interfaces (clases abstractas).

No requiere instalaciones adicionales ni dependencias externas.

## Versión utilizada de Python

Python 3.12

## Cómo Ejecutar el Proyecto

1. Clonar o descargar el repositorio.
2. Ejecutar en consola:
   https://github.com/SofiaGomez1996/cliente_correo.git
3. Seguir las opciones del menú.



##  Notas

Este proyecto cumple con todos los puntos requeridos:

* Modelado OOP completo.
* Encapsulamiento y uso de interfaces.
* Árbol recursivo para carpetas.
* Filtros automáticos.
* Cola de prioridades.
* Grafo con recorridos BFS/DFS.
* CLI integrada.
* Código documentado y organizado.


      

