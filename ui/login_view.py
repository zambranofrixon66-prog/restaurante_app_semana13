import tkinter as tk
from tkinter import ttk

class LoginView(tk.Frame):
    def __init__(self, parent, controlador, restaurante_servicio):
        super().__init__(parent, padx=25, pady=25)
        self.controlador = controlador
        self.servicio = restaurante_servicio
        self.crear_widgets()

    def crear_widgets(self):
        titulo = ttk.Label(self, text="Restaurante App", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 10))

        subtitulo = ttk.Label(self, text="Acceso al Sistema", font=("Arial", 11))
        subtitulo.pack(pady=(0, 15))

        lbl_usuario = ttk.Label(self, text="Usuario:")
        lbl_usuario.pack(anchor="w", pady=(5, 0))
        self.entry_usuario = ttk.Entry(self, width=30)
        self.entry_usuario.pack(pady=(0, 10))

        lbl_pass = ttk.Label(self, text="Contraseña:")
        lbl_pass.pack(anchor="w", pady=(5, 0))
        self.entry_pass = ttk.Entry(self, show="*", width=30)
        self.entry_pass.pack(pady=(0, 15))

        self.lbl_mensaje = ttk.Label(self, text="", foreground="red")
        self.lbl_mensaje.pack(pady=(0, 10))

        btn_ingresar = ttk.Button(self, text="Iniciar sesión", command=self.procesar_login)
        btn_ingresar.pack(fill="x", pady=5)

    def procesar_login(self):
        usuario_txt = self.entry_usuario.get().strip()
        pass_txt = self.entry_pass.get().strip()

        if not usuario_txt or not pass_txt:
            self.lbl_mensaje.config(text="Por favor, complete todos los campos.", foreground="red")
            return

        usuario_valido = self.servicio.autenticar_usuario(usuario_txt, pass_txt)
        if usuario_valido:
            self.lbl_mensaje.config(text="")
            self.entry_usuario.delete(0, tk.END)
            self.entry_pass.delete(0, tk.END)
            self.controlador.mostrar_main_view(usuario_valido)
        else:
            self.lbl_mensaje.config(text="Usuario o contraseña incorrectos.", foreground="red")