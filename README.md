# Proyecto 2
Este es un proyecto que simula el funcionamiento de una heladería utilizando **Flask** como framework para la creación de la API y una serie de clases en Python que modelan los productos, ingredientes y ventas. La aplicación permite realizar ventas de productos como copas, malteadas, y otros complementos, gestionando el inventario de los ingredientes y verificando la disponibilidad antes de cada venta.

## Descripción

La aplicación permite:
- Verificar el inventario de los ingredientes (como bases y complementos).
- Realizar ventas de productos.
- Ver la rentabilidad de los productos.
- Manejar los errores en caso de que falte algún ingrediente para la venta.

## Características

- **Gestión de Inventarios**: Se gestionan los inventarios de diferentes tipos de ingredientes.
- **Venta de Productos**: Permite la venta de productos (copas, malteadas) siempre y cuando todos los ingredientes estén disponibles.
- **Manejo de Errores**: Lanza errores con mensajes específicos cuando falta un ingrediente, con un mensaje personalizado.
- **Flask API**: Implementación de una API para interactuar con el sistema y realizar ventas.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- **Python 3.x**
- **Flask** (Para crear la API y manejar las solicitudes HTTP)
- **Pip** (Para gestionar las dependencias)

## Instalación

Sigue los siguientes pasos para instalar y ejecutar el proyecto:

1. Clona el repositorio en tu máquina local:
   ```
   git clone https://github.com/tu-usuario/heladeria-flask.git
   ```
