import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Restaurante - Semana 13")
        self.root.geometry("620x420")
        self.root.resizable(False, False)

        self.servicio = RestauranteServicio()

        self.contenedor = tk.Frame(self.root)
        self.contenedor.pack(fill="both", expand=True)

        self.vista_actual = None
        self.mostrar_login_view()

    def cambiar_vista(self, nueva_vista):
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_login_view(self):
        self.cambiar_vista(LoginView(self.contenedor, self, self.servicio))

    def mostrar_main_view(self, usuario):
        self.cambiar_vista(MainView(self.contenedor, self, self.servicio, usuario))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()