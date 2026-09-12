````markdown
# Restaurante App - Semana 13

**Estudiante:** Frixon Jeancarlos Zambrano Ortiz  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 13  

## Propósito

En esta semana se realizó la transición de la aplicación del restaurante desde una interacción por consola hacia una interfaz gráfica desarrollada con `Tkinter`.

El objetivo principal fue mejorar la forma en que el usuario interactúa con el sistema, manteniendo la lógica y la estructura desarrollada anteriormente. Además, se continúa utilizando archivos `JSON` para almacenar la información de productos y usuarios.

## Estructura del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
````

## Descripción de la Estructura

* `datos/`: contiene los archivos `JSON` con la información de productos y usuarios.
* `modelos/`: contiene las clases principales del sistema, como `Producto` y `Usuario`.
* `servicios/`: contiene la lógica para leer los datos, realizar validaciones y gestionar las operaciones del sistema.
* `ui/`: contiene las ventanas creadas con `Tkinter`.
* `main.py`: inicia la aplicación y controla el cambio entre las diferentes vistas.
* `README.md`: contiene la información general y el funcionamiento del proyecto.

## Funcionamiento de la Aplicación

1. Al ejecutar el programa se muestra la pantalla de inicio de sesión.
2. El usuario ingresa su nombre de usuario y contraseña.
3. Las credenciales son validadas mediante `RestauranteServicio`.
4. Si los datos son correctos, se muestra la ventana principal.
5. Desde la ventana principal se pueden consultar los productos y usuarios registrados.
6. La opción de ventas muestra una notificación para una futura implementación.
7. El usuario puede cerrar sesión y regresar a la pantalla de acceso.

## Interfaz Gráfica

La interfaz gráfica fue desarrollada con `Tkinter` utilizando componentes como `Label`, `Entry`, `Button` y `Frame`.

Las vistas se encuentran separadas dentro de la carpeta `ui`, lo que permite mantener una mejor organización del código y evitar mezclar la interfaz gráfica con la lógica del sistema.

## Separación de Responsabilidades

El proyecto mantiene una estructura organizada donde cada parte cumple una función específica.

Los modelos representan las entidades principales, los servicios realizan las validaciones y gestionan la información, mientras que la interfaz gráfica se encarga de mostrar los datos y recibir las acciones del usuario.

## Ejecución

Para ejecutar la aplicación se debe abrir una terminal dentro de la carpeta principal del proyecto y escribir:

```bash
python main.py
```

## Tecnologías Utilizadas

* `Python`
* `Tkinter`
* `JSON`
* `Programación Orientada a Objetos`

## Conclusión

Con esta actividad se logró incorporar una interfaz gráfica al sistema del restaurante, haciendo que la aplicación sea más sencilla y visual para el usuario.

Además, se mantuvo la organización del proyecto mediante la separación de modelos, servicios e interfaz gráfica, facilitando futuras mejoras y nuevas funcionalidades.

```

Las palabras que más conviene resaltar son: `Tkinter`, `JSON`, `Producto`, `Usuario`, `RestauranteServicio`, `Label`, `Entry`, `Button`, `Frame`, `Python` y los nombres de archivos/carpetas.
```
