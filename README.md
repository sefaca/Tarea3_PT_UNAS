# Gestión de Inventario de Productos - Python

Este proyecto implementa un sistema simple de gestión de inventario de productos. Permite ordenar una lista de productos por precio y calcular el stock restante en base a entradas y salidas. El proyecto fue creado como parte de una prueba técnica.

## Índice

- [Introducción](#introducción)
- [Primeros pasos](#primeros-pasos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Tecnologías y herramientas utilizadas](#tecnologías-y-herramientas-utilizadas)
- [Aprendizaje y desarrollo](#aprendizaje-y-desarrollo)

## Introducción

El objetivo de este proyecto es demostrar cómo gestionar un inventario de productos en un almacén. La funcionalidad principal incluye:

1. **Ordenar productos por precio** (de menor a mayor).
2. **Calcular el stock restante** a partir de una lista de movimientos (entradas y salidas de inventario).

Este proyecto está desarrollado en Python y es ideal para probar conceptos de lógica, algoritmos y manejo de estructuras de datos.

## Primeros pasos

Sigue los siguientes pasos para ejecutar el proyecto en tu máquina local.

### Paso 1: Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/gestion-inventario-python.git
```

### Paso 2: Ejecutar el código

Asegúrate de tener Python 3.x instalado en tu sistema. Si no lo tienes, descárgalo desde aquí.

Luego, desde la carpeta del proyecto, ejecuta el script en la terminal:

```bash
python gestion_inventario.py
```

### Paso 3: Resultado esperado

Al ejecutar el script, verás dos operaciones principales:

- Productos ordenados por precio: La lista de productos se muestra de menor a mayor precio.
- Stock actualizado: El stock de cada producto se ajusta según los movimientos dados (entradas y salidas de inventario).

Ejemplo de salida:

```bash
Productos ordenados por precio:
{'nombre': 'Producto A', 'precio': 10, 'stock': 50}
{'nombre': 'Producto C', 'precio': 15, 'stock': 40}
{'nombre': 'Producto B', 'precio': 20, 'stock': 30}

Stock actualizado:
{'nombre': 'Producto A', 'precio': 10, 'stock': 150}
{'nombre': 'Producto B', 'precio': 20, 'stock': 25}
{'nombre': 'Producto C', 'precio': 15, 'stock': 60}
```

## Estructura del proyecto

El proyecto tiene la siguiente estructura de archivos:

```bash
├── gestion_inventario.py  # Archivo principal con las funciones de gestión de productos e inventario
├── README.md              # Documentación del proyecto
```

- gestion_inventario.py: Contiene el código principal que implementa la lógica para ordenar productos por precio y calcular el stock basado en los movimientos.
- README.md: Este archivo, que documenta cómo instalar, usar y entender el proyecto.

## Tecnologías y herramientas utilizadas

Este proyecto ha sido desarrollado con:

Lenguaje de programación:
Python 3.x: El lenguaje utilizado para implementar la lógica de gestión de inventario. Python ofrece una sintaxis limpia y sencilla para trabajar con listas y diccionarios, lo que facilita la implementación de las funcionalidades solicitadas.

## Aprendizaje y desarrollo

A través del desarrollo de este proyecto se han puesto en práctica los siguientes conceptos:

- Lógica y algoritmos en Python: Uso de funciones para ordenar y manipular listas de diccionarios.
- Manejo de estructuras de datos: Manipulación de listas y diccionarios para representar productos, precios y movimientos de stock.
- Procesamiento de datos en inventarios: Actualización dinámica del stock en función de entradas y salidas en el almacén.
- Buenas prácticas de desarrollo: Estructuración clara del código con funciones separadas para cada tarea, lo que facilita su mantenimiento y escalabilidad.

Este proyecto refuerza conceptos básicos pero importantes para el desarrollo de software, como el manejo eficiente de estructuras de datos y la separación de lógica en funciones.
