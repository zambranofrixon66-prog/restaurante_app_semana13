from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    RUTA_PRODUCTOS = "datos/productos.json"
    RUTA_USUARIOS = "datos/usuarios.json"

    def __init__(self):
        self.archivo_servicio = ArchivoServicio()

    def autenticar(self, username, password):
        usuarios = self.archivo_servicio.leer_json(self.RUTA_USUARIOS)
        for u in usuarios:
            if u.get("username") == username and u.get("password") == password:
                return Usuario.from_dict(u)
        return None

    def autenticar_usuario(self, username, password):
        return self.autenticar(username, password)

    def obtener_usuarios(self) -> list:
        data = self.archivo_servicio.leer_json(self.RUTA_USUARIOS)
        return [Usuario.from_dict(u) for u in data]

    def obtener_productos(self) -> list:
        data = self.archivo_servicio.leer_json(self.RUTA_PRODUCTOS)
        return [Producto.from_dict(p) for p in data]

    def buscar_producto_por_id(self, id_prod: str):
        id_prod = str(id_prod).strip()
        for prod in self.obtener_productos():
            if str(prod.id_producto).strip() == id_prod:
                return prod
        return None

    def registrar_producto(self, id_prod, nombre, categoria, precio, stock):
        id_prod = str(id_prod).strip()
        nombre = str(nombre).strip()

        if not id_prod or not nombre:
            return False, "El ID y el Nombre son obligatorios."
        if precio < 0 or stock < 0:
            return False, "El precio y el stock no pueden ser negativos."
        if self.buscar_producto_por_id(id_prod):
            return False, f"El producto con ID '{id_prod}' ya existe."

        productos = self.obtener_productos()
        nuevo = Producto(id_prod, nombre, categoria, precio, stock)
        productos.append(nuevo)

        self._guardar_productos(productos)
        return True, "Producto registrado correctamente."

    def actualizar_producto(self, id_prod, nombre, categoria, precio, stock):
        id_prod = str(id_prod).strip()
        nombre = str(nombre).strip()

        if not id_prod or not nombre:
            return False, "El ID y el Nombre son obligatorios."
        if precio < 0 or stock < 0:
            return False, "El precio y el stock deben ser válidos."

        productos = self.obtener_productos()
        encontrado = False

        for i, p in enumerate(productos):
            if str(p.id_producto).strip() == id_prod:
                productos[i] = Producto(id_prod, nombre, categoria, precio, stock)
                encontrado = True
                break

        if not encontrado:
            return False, f"No se encontró el producto con ID '{id_prod}'."

        self._guardar_productos(productos)
        return True, "Producto actualizado con éxito."

    def eliminar_producto(self, id_prod: str):
        id_prod = str(id_prod).strip()
        productos = self.obtener_productos()
        nuevos = [p for p in productos if str(p.id_producto).strip() != id_prod]

        if len(productos) == len(nuevos):
            return False, f"No se encontró el producto con ID '{id_prod}'."

        self._guardar_productos(nuevos)
        return True, "Producto eliminado correctamente."

    def _guardar_productos(self, lista):
        data = [p.to_dict() for p in lista]
        self.archivo_servicio.guardar_json(self.RUTA_PRODUCTOS, data)