class Producto:
    def __init__(self, id, nombre, precio, categoria):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria

    def __str__(self):
        return f"[{self.id}] {self.nombre} - ${self.precio:.2f} ({self.categoria})"