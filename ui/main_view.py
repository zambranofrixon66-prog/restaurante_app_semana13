import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):
    def __init__(self, parent, *args):
        super().__init__(parent)
        self.parent = parent
        
        # Si le pasaron (controlador, servicio, usuario) o (servicio, usuario)
        if len(args) == 3:
            self.controlador = args[0]
            self.servicio = args[1]
            self.usuario_activo = args[2]
        elif len(args) == 2:
            self.controlador = None
            self.servicio = args[0]
            self.usuario_activo = args[1]
        else:
            self.controlador = None
            self.servicio = None
            self.usuario_activo = None

        self._iniciar_interfaz()

    def _iniciar_interfaz(self):
        header = ttk.Frame(self, padding=(15, 10))
        header.pack(fill=tk.X)
        rol = getattr(self.usuario_activo, 'rol', 'Personal')
        ttk.Label(
            header,
            text=f"Sesión activa: {self.usuario_activo.nombre} ({rol})",
            font=("Segoe UI", 11, "bold")
        ).pack(side=tk.LEFT)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=(5, 15))

        self.tab_productos = ttk.Frame(self.notebook, padding=10)
        self.tab_usuarios = ttk.Frame(self.notebook, padding=10)

        self.notebook.add(self.tab_productos, text="  Gestión de Productos  ")
        self.notebook.add(self.tab_usuarios, text="  Consulta de Usuarios  ")

        self._construir_pestana_productos()
        self._construir_pestana_usuarios()

    def _construir_pestana_productos(self):
        panel_izq = ttk.Frame(self.tab_productos)
        panel_izq.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        frame_form = ttk.LabelFrame(panel_izq, text=" Formulario de Producto ", padding=10)
        frame_form.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(frame_form, text="ID Producto:").grid(row=0, column=0, sticky=tk.W, pady=4)
        self.txt_id = ttk.Entry(frame_form, width=22)
        self.txt_id.grid(row=0, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky=tk.W, pady=4)
        self.txt_nombre = ttk.Entry(frame_form, width=22)
        self.txt_nombre.grid(row=1, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Categoría:").grid(row=2, column=0, sticky=tk.W, pady=4)
        self.cmb_cat = ttk.Combobox(
            frame_form,
            values=["Platos Fuertes", "Bebidas", "Postres", "Entradas", "Guarniciones"],
            state="readonly",
            width=20
        )
        self.cmb_cat.current(0)
        self.cmb_cat.grid(row=2, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=3, column=0, sticky=tk.W, pady=4)
        self.txt_precio = ttk.Entry(frame_form, width=22)
        self.txt_precio.grid(row=3, column=1, pady=4, padx=5)

        ttk.Label(frame_form, text="Stock:").grid(row=4, column=0, sticky=tk.W, pady=4)
        self.txt_stock = ttk.Entry(frame_form, width=22)
        self.txt_stock.grid(row=4, column=1, pady=4, padx=5)

        frame_btn = ttk.LabelFrame(panel_izq, text=" Acciones ", padding=10)
        frame_btn.pack(fill=tk.X)

        ttk.Button(frame_btn, text="Registrar", command=self._accion_registrar).grid(row=0, column=0, sticky=tk.EW, padx=3, pady=3)
        ttk.Button(frame_btn, text="Cargar / Consultar", command=self._accion_consultar).grid(row=0, column=1, sticky=tk.EW, padx=3, pady=3)
        ttk.Button(frame_btn, text="Actualizar", command=self._accion_actualizar).grid(row=1, column=0, sticky=tk.EW, padx=3, pady=3)
        ttk.Button(frame_btn, text="Eliminar", command=self._accion_eliminar).grid(row=1, column=1, sticky=tk.EW, padx=3, pady=3)
        ttk.Button(frame_btn, text="Limpiar Campos", command=self._limpiar).grid(row=2, column=0, columnspan=2, sticky=tk.EW, padx=3, pady=(6, 3))

        frame_btn.columnconfigure(0, weight=1)
        frame_btn.columnconfigure(1, weight=1)

        panel_der = ttk.LabelFrame(self.tab_productos, text=" Catálogo Actual ", padding=10)
        panel_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        columnas = ("id", "nombre", "cat", "precio", "stock")
        self.tabla_prod = ttk.Treeview(panel_der, columns=columnas, show="headings", selectmode="browse")
        self.tabla_prod.heading("id", text="ID")
        self.tabla_prod.heading("nombre", text="Nombre")
        self.tabla_prod.heading("cat", text="Categoría")
        self.tabla_prod.heading("precio", text="Precio ($)")
        self.tabla_prod.heading("stock", text="Stock")

        self.tabla_prod.column("id", width=60, anchor=tk.CENTER)
        self.tabla_prod.column("nombre", width=170)
        self.tabla_prod.column("cat", width=110)
        self.tabla_prod.column("precio", width=75, anchor=tk.E)
        self.tabla_prod.column("stock", width=60, anchor=tk.CENTER)

        barra_y = ttk.Scrollbar(panel_der, orient=tk.VERTICAL, command=self.tabla_prod.yview)
        self.tabla_prod.configure(yscrollcommand=barra_y.set)

        self.tabla_prod.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        barra_y.pack(side=tk.RIGHT, fill=tk.Y)

        self._refrescar_tabla_productos()

    def _construir_pestana_usuarios(self):
        frame_usr = ttk.LabelFrame(self.tab_usuarios, text=" Directorio de Usuarios ", padding=10)
        frame_usr.pack(fill=tk.BOTH, expand=True)

        cols = ("usuario", "nombre", "rol")
        self.tabla_usr = ttk.Treeview(frame_usr, columns=cols, show="headings")
        self.tabla_usr.heading("usuario", text="Nombre de Usuario")
        self.tabla_usr.heading("nombre", text="Nombre Completo")
        self.tabla_usr.heading("rol", text="Rol Asignado")

        self.tabla_usr.pack(fill=tk.BOTH, expand=True)
        self._cargar_tabla_usuarios()

    def _refrescar_tabla_productos(self):
        for row in self.tabla_prod.get_children():
            self.tabla_prod.delete(row)
        for p in self.servicio.obtener_productos():
            self.tabla_prod.insert("", tk.END, values=(
                p.id_producto, p.nombre, p.categoria, f"{p.precio:.2f}", p.stock
            ))

    def _cargar_tabla_usuarios(self):
        for row in self.tabla_usr.get_children():
            self.tabla_usr.delete(row)
        for u in self.servicio.obtener_usuarios():
            self.tabla_usr.insert("", tk.END, values=(u.username, u.nombre, getattr(u, 'rol', 'Personal')))

    def _limpiar(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.cmb_cat.current(0)
        self.txt_precio.delete(0, tk.END)
        self.txt_stock.delete(0, tk.END)
        self.txt_id.focus()

    def _parse_numeros(self):
        try:
            precio = float(self.txt_precio.get().strip())
            stock = int(self.txt_stock.get().strip())
            return precio, stock
        except ValueError:
            messagebox.showwarning("Formato inválido", "El precio debe ser un número decimal y el stock un número entero.")
            return None, None

    def _accion_registrar(self):
        id_p = self.txt_id.get().strip()
        nom = self.txt_nombre.get().strip()
        cat = self.cmb_cat.get()
        precio, stock = self._parse_numeros()
        if precio is None:
            return

        exito, msg = self.servicio.registrar_producto(id_p, nom, cat, precio, stock)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_productos()
            self._limpiar()
        else:
            messagebox.showerror("Error", msg)

    def _accion_consultar(self):
        id_p = self.txt_id.get().strip()
        if not id_p:
            messagebox.showwarning("Atención", "Ingrese el ID del producto que desea cargar en el formulario.")
            return

        prod = self.servicio.buscar_producto_por_id(id_p)
        if prod:
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, prod.nombre)
            self.cmb_cat.set(prod.categoria)
            self.txt_precio.delete(0, tk.END)
            self.txt_precio.insert(0, str(prod.precio))
            self.txt_stock.delete(0, tk.END)
            self.txt_stock.insert(0, str(prod.stock))
            messagebox.showinfo("Información", f"Producto '{prod.nombre}' cargado en el formulario.")
        else:
            messagebox.showwarning("No encontrado", f"No se encontró ningún producto con ID '{id_p}'.")

    def _accion_actualizar(self):
        id_p = self.txt_id.get().strip()
        nom = self.txt_nombre.get().strip()
        cat = self.cmb_cat.get()
        precio, stock = self._parse_numeros()
        if precio is None:
            return

        exito, msg = self.servicio.actualizar_producto(id_p, nom, cat, precio, stock)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_productos()
            self._limpiar()
        else:
            messagebox.showerror("Error", msg)

    def _accion_eliminar(self):
        id_p = self.txt_id.get().strip()
        if not id_p:
            messagebox.showwarning("Atención", "Ingrese el ID del producto que desea eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto con ID '{id_p}'?")
        if not confirmar:
            return

        exito, msg = self.servicio.eliminar_producto(id_p)
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_productos()
            self._limpiar()
        else:
            messagebox.showerror("Error", msg)