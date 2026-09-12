class Usuario:
    def __init__(self, username, password, nombre, rol):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} ({self.username}) - Rol: {self.rol}"