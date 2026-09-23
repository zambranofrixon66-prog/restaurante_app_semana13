# Restaurante App - Semana 14

**Estudiante:** Frixon Jeancarlos Zambrano Ortiz  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 14  

## Propósito

En esta semana se realizó la evolución de la aplicación `restaurante_app` mediante la integración de componentes avanzados, contenedores y gestores de geometría de `Tkinter` y `ttk`.

El objetivo principal fue transformar la interfaz gráfica inicial hacia una experiencia de usuario más clara, amigable y estructurada. Se implementaron formularios, áreas de visualización tabular y paneles de control que permiten gestionar el catálogo de productos (registro, consulta, actualización y eliminación) y consultar los usuarios registrados, preservando estrictamente la separación de responsabilidades y la persistencia en archivos `JSON`.

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
```

## Descripción de la Estructura

* `datos/`: almacena los archivos `JSON` (`productos.json` y `usuarios.json`) que garantizan la persistencia de datos.
* `modelos/`: define las clases entidad del sistema, como `Producto` y `Usuario`, junto con sus métodos de serialización.
* `servicios/`: contiene la lógica del negocio (`RestauranteServicio`) y la lectura/escritura en disco (`ArchivoServicio`), evitando que la interfaz manipule archivos o aplique reglas de negocio directamente.
* `ui/`: alberga las ventanas desarrolladas con `Tkinter` (`LoginView` para autenticación y `MainView` para la gestión y consulta).
* `main.py`: punto de entrada que inicializa la aplicación y coordina el flujo de acceso.
* `README.md`: documentación completa del proyecto correspondiente a la Semana 14.

## Mejoras Incorporadas en la Interfaz (Componentes y Contenedores)

La interfaz principal (`MainView`) fue rediseñada utilizando contenedores organizados para estructurar de manera óptima las zonas de navegación, captura y presentación:

1. **`ttk.Notebook` (Pestañas de Navegación):** Permite organizar el sistema en dos áreas claramente diferenciadas:
   * **Gestión de Productos:** Área operativa para registrar, consultar, modificar y eliminar artículos.
   * **Consulta de Usuarios:** Directorio con la lista del personal y usuarios registrados.
2. **`ttk.LabelFrame` (Contenedores Agrupadores):** Se emplearon marcos con título para delimitar visualmente:
   * El formulario de entrada de datos.
   * El panel de botones y acciones.
   * El catálogo visual de productos y el directorio de usuarios.
3. **`ttk.Treeview` y `ttk.Scrollbar` (Visualización Tabular):** Permite presentar la información estructurada en columnas (ID, Nombre, Categoría, Precio y Stock) con desplazamiento vertical fluido.
4. **`ttk.Combobox` (Lista Desplegable):** Facilita la selección controlada de categorías de productos (Platos Fuertes, Bebidas, Postres, etc.).
5. **`ttk.Button` con `command=`:** Enlace de todas las acciones del usuario sin recurrir a eventos complejos (`bind()`), manteniendo la interacción sencilla y limpia.
6. **Gestores de Geometría (`pack` y `grid`):** Uso armónico de `pack()` para distribuir los paneles principales y `grid()` para alinear con precisión las etiquetas y cajas de texto del formulario.

## Operaciones Implementadas sobre Productos

Todas las operaciones se ejecutan mediante botones en la interfaz y delegan su validación a `RestauranteServicio`:

* **Registrar:** Captura los datos ingresados en el formulario, valida campos obligatorios y números válidos, y guarda el nuevo producto en `productos.json`.
* **Cargar / Consultar:** Permite ingresar un ID de producto para buscarlo en el sistema y rellenar automáticamente los campos del formulario para su revisión o modificación.
* **Actualizar:** Modifica la información del producto existente tras validar los valores numéricos y la presencia del registro.
* **Eliminar:** Remueve el producto seleccionado previa confirmación mediante un cuadro de diálogo (`messagebox.askyesno`).
* **Limpiar:** Restablece todos los controles del formulario y devuelve el foco al campo del ID.

## Separación de Responsabilidades y Persistencia

Se mantuvo rigurosamente la arquitectura modular:
* La capa **UI** (`MainView`) se limita a capturar los datos ingresados por el usuario, mostrar cuadros de diálogo informativos y actualizar la tabla visual.
* La capa de **Servicios** (`RestauranteServicio`) procesa las reglas del restaurante (verificación de duplicados, validación de stock y precios mayores o iguales a cero).
* La persistencia en `productos.json` se ejecuta inmediatamente tras cada operación exitosa mediante `ArchivoServicio`, asegurando que la información se conserve al cerrar y reiniciar la aplicación.

## Ejecución

Para iniciar la aplicación, abra una terminal en la carpeta principal del proyecto y ejecute:

```bash
python main.py
```

## Tecnologías Utilizadas

* `Python`
* `Tkinter` / `ttk` (`Notebook`, `LabelFrame`, `Treeview`, `Combobox`, `Scrollbar`, `Button`, `Entry`, `Label`)
* `JSON`
* `Programación Orientada a Objetos` (POO)
* `Git` y `GitHub`

## Conclusión

Con la evolución de la Semana 14, `restaurante_app` consolidó una interfaz gráfica estructurada, intuitiva y profesional. El uso adecuado de componentes y contenedores permitió resolver las operaciones CRUD de productos y la consulta de usuarios en un entorno limpio y coherente, respetando la arquitectura modular y la persistencia de datos establecida.