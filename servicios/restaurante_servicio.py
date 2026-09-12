from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.usuarios = []
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        raw_usuarios = ArchivoServicio.leer_json("datos/usuarios.json")
        self.usuarios = [
            Usuario(u["username"], u["password"], u["nombre"], u["rol"])
            for u in raw_usuarios
        ]

        raw_productos = ArchivoServicio.leer_json("datos/productos.json")
        self.productos = [
            Producto(p["id"], p["nombre"], p["precio"], p["categoria"])
            for p in raw_productos
        ]

    def autenticar_usuario(self, username, password):
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return u
        return None

    def obtener_productos(self):
        return self.productos

    def obtener_usuarios(self):
        return self.usuarios

    def contar_productos(self):
        return len(self.productos)

    def contar_usuarios(self):
        return len(self.usuarios)