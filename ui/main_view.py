import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, parent, controlador, restaurante_servicio, usuario_actual=None):
        super().__init__(parent, padx=20, pady=20)
        self.controlador = controlador
        self.servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.crear_widgets()

    def crear_widgets(self):
        nombre = self.usuario_actual.nombre if self.usuario_actual else "Usuario"
        lbl_bienvenida = ttk.Label(self, text=f"Bienvenido/a, {nombre}", font=("Arial", 14, "bold"))
        lbl_bienvenida.pack(pady=(0, 15))

        nav = ttk.Frame(self)
        nav.pack(fill="x", pady=(0, 10))

        ttk.Button(nav, text="Productos registrados", command=self.listar_productos).pack(side="left", padx=5)
        ttk.Button(nav, text="Usuarios registrados", command=self.listar_usuarios).pack(side="left", padx=5)
        ttk.Button(nav, text="Ventas", command=self.mostrar_alerta_ventas).pack(side="left", padx=5)
        ttk.Button(nav, text="Cerrar sesión", command=self.controlador.mostrar_login_view).pack(side="right", padx=5)

        self.tree = ttk.Treeview(self, show="headings", height=8)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.lbl_status = ttk.Label(self, text="Seleccione una opción para consultar datos.", relief="sunken", anchor="w")
        self.lbl_status.pack(fill="x", pady=(5, 0))

    def limpiar_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def listar_productos(self):
        self.limpiar_treeview()
        self.tree["columns"] = ("ID", "Nombre", "Precio", "Categoría")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        for p in self.servicio.obtener_productos():
            self.tree.insert("", tk.END, values=(p.id, p.nombre, f"${p.precio:.2f}", p.categoria))

        self.lbl_status.config(text=f"Total de productos: {self.servicio.contar_productos()}")

    def listar_usuarios(self):
        self.limpiar_treeview()
        self.tree["columns"] = ("Usuario", "Nombre", "Rol")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        for u in self.servicio.obtener_usuarios():
            self.tree.insert("", tk.END, values=(u.username, u.nombre, u.rol))

        self.lbl_status.config(text=f"Total de usuarios: {self.servicio.contar_usuarios()}")

    def mostrar_alerta_ventas(self):
        messagebox.showinfo("Ventas", "Módulo de ventas identificado como funcionalidad futura (pendiente de desarrollo).")