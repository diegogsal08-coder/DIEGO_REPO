
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# CONEXION A LA BASE DE DATOS
conexion = sqlite3.connect("oxxo.db")
cursor = conexion.cursor()

# CREAR TABLAS
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    total REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venta_id INTEGER,
    producto TEXT,
    cantidad INTEGER,
    precio REAL,
    subtotal REAL
)
""")

# AGREGAR PRODUCTOS INICIALES
cursor.execute("SELECT COUNT(*) FROM productos")
cantidad_productos = cursor.fetchone()[0]

if cantidad_productos == 0:
    productos_iniciales = [
        ("Coca Cola", 20, 30),
        ("Sabritas", 18, 25),
        ("Agua", 15, 40),
        ("Galletas", 16, 20),
        ("Chocolate", 22, 15),
        ("Jugo", 18, 25),
        ("Leche", 28, 15),
        ("Pan", 25, 20)
    ]

    cursor.executemany(
        "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
        productos_iniciales
    )

conexion.commit()

# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Punto de Venta - Tienda de Conveniencia")
ventana.geometry("900x650")
ventana.configure(bg="#eeeeee")

carrito = []

# TITULO
titulo = tk.Label(
    ventana,
    text="PUNTO DE VENTA",
    font=("Arial", 22, "bold"),
    bg="#cc0000",
    fg="white",
    pady=15
)
titulo.pack(fill="x")

subtitulo = tk.Label(
    ventana,
    text="Sistema de ventas estilo OXXO",
    font=("Arial", 12),
    bg="#eeeeee"
)
subtitulo.pack(pady=10)

# FUNCION PARA MOSTRAR PRODUCTOS
def cargar_productos():
    for fila in tabla_productos.get_children():
        tabla_productos.delete(fila)

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    for producto in productos:
        tabla_productos.insert("", "end", values=producto)


# FUNCION PARA AGREGAR AL CARRITO
def agregar_producto():
    seleccion = tabla_productos.selection()

    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un producto.")
        return

    try:
        cantidad = int(entrada_cantidad.get())

        if cantidad <= 0:
            messagebox.showwarning("Aviso", "Ingresa una cantidad mayor a cero.")
            return

    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un numero.")
        return

    datos = tabla_productos.item(seleccion[0], "values")

    id_producto = int(datos[0])
    nombre = datos[1]
    precio = float(datos[2])
    stock = int(datos[3])

    if cantidad > stock:
        messagebox.showwarning(
            "Inventario",
            "No hay suficientes productos disponibles."
        )
        return

    # BUSCAR SI EL PRODUCTO YA ESTA EN EL CARRITO
    encontrado = False

    for producto in carrito:
        if producto[0] == id_producto:
            nueva_cantidad = producto[3] + cantidad

            if nueva_cantidad > stock:
                messagebox.showwarning(
                    "Inventario",
                    "No hay suficientes productos disponibles."
                )
                return

            producto[3] = nueva_cantidad
            encontrado = True
            break

    if not encontrado:
        carrito.append([id_producto, nombre, precio, cantidad])

    entrada_cantidad.delete(0, tk.END)
    entrada_cantidad.insert(0, "1")

    mostrar_carrito()


# FUNCION PARA MOSTRAR EL CARRITO
def mostrar_carrito():
    for fila in tabla_carrito.get_children():
        tabla_carrito.delete(fila)

    total = 0

    for producto in carrito:
        subtotal = producto[2] * producto[3]
        total += subtotal

        tabla_carrito.insert(
            "",
            "end",
            values=(
                producto[1],
                producto[3],
                f"${producto[2]:.2f}",
                f"${subtotal:.2f}"
            )
        )

    etiqueta_total.config(text=f"TOTAL: ${total:.2f}")


# FUNCION PARA ELIMINAR UN PRODUCTO DEL CARRITO
def eliminar_producto():
    seleccion = tabla_carrito.selection()

    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un producto del carrito.")
        return

    indice = tabla_carrito.index(seleccion[0])
    carrito.pop(indice)

    mostrar_carrito()


# FUNCION PARA REALIZAR LA VENTA
def realizar_venta():
    if len(carrito) == 0:
        messagebox.showwarning("Aviso", "El carrito esta vacio.")
        return

    total = 0

    # COMPROBAR NUEVAMENTE LAS EXISTENCIAS
    for producto in carrito:
        cursor.execute(
            "SELECT stock FROM productos WHERE id = ?",
            (producto[0],)
        )

        resultado = cursor.fetchone()

        if resultado is None or producto[3] > resultado[0]:
            messagebox.showerror(
                "Error",
                "El inventario cambio. Revisa los productos."
            )
            cargar_productos()
            return

        total += producto[2] * producto[3]

    # GUARDAR LA VENTA
    from datetime import datetime

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute(
            "INSERT INTO ventas (fecha, total) VALUES (?, ?)",
            (fecha, total)
        )

        venta_id = cursor.lastrowid

        for producto in carrito:
            id_producto = producto[0]
            nombre = producto[1]
            precio = producto[2]
            cantidad = producto[3]
            subtotal = precio * cantidad

            cursor.execute("""
                INSERT INTO detalle_ventas
                (venta_id, producto, cantidad, precio, subtotal)
                VALUES (?, ?, ?, ?, ?)
            """, (venta_id, nombre, cantidad, precio, subtotal))

            cursor.execute("""
                UPDATE productos
                SET stock = stock - ?
                WHERE id = ?
            """, (cantidad, id_producto))

        conexion.commit()

        messagebox.showinfo(
            "Venta realizada",
            f"Venta registrada correctamente.\n\n"
            f"Numero de venta: {venta_id}\n"
            f"Total a pagar: ${total:.2f}"
        )

        carrito.clear()
        mostrar_carrito()
        cargar_productos()

    except sqlite3.Error as error:
        conexion.rollback()
        messagebox.showerror("Error", f"No se pudo registrar la venta:\n{error}")


# FUNCION PARA CONSULTAR LAS VENTAS
def consultar_ventas():
    ventana_ventas = tk.Toplevel(ventana)
    ventana_ventas.title("Historial de ventas")
    ventana_ventas.geometry("600x400")

    tk.Label(
        ventana_ventas,
        text="HISTORIAL DE VENTAS",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tabla_ventas = ttk.Treeview(
        ventana_ventas,
        columns=("ID", "Fecha", "Total"),
        show="headings"
    )

    tabla_ventas.heading("ID", text="Venta")
    tabla_ventas.heading("Fecha", text="Fecha")
    tabla_ventas.heading("Total", text="Total")

    tabla_ventas.pack(fill="both", expand=True, padx=10, pady=10)

    cursor.execute("SELECT * FROM ventas ORDER BY id DESC")
    registros = cursor.fetchall()

    for venta in registros:
        tabla_ventas.insert(
            "",
            "end",
            values=(venta[0], venta[1], f"${venta[2]:.2f}")
        )


# SECCION DE PRODUCTOS
marco_productos = tk.LabelFrame(
    ventana,
    text="Productos disponibles",
    font=("Arial", 11, "bold"),
    bg="#eeeeee",
    padx=10,
    pady=10
)
marco_productos.pack(fill="x", padx=15, pady=10)

tabla_productos = ttk.Treeview(
    marco_productos,
    columns=("ID", "Nombre", "Precio", "Stock"),
    show="headings",
    height=7
)

tabla_productos.heading("ID", text="ID")
tabla_productos.heading("Nombre", text="Producto")
tabla_productos.heading("Precio", text="Precio")
tabla_productos.heading("Stock", text="Existencias")

tabla_productos.column("ID", width=50)
tabla_productos.column("Nombre", width=250)
tabla_productos.column("Precio", width=100)
tabla_productos.column("Stock", width=100)

tabla_productos.pack(fill="x")

# SECCION PARA AGREGAR PRODUCTOS
marco_compra = tk.Frame(ventana, bg="#eeeeee")
marco_compra.pack(pady=10)

tk.Label(
    marco_compra,
    text="Cantidad:",
    font=("Arial", 11),
    bg="#eeeeee"
).grid(row=0, column=0, padx=5)

entrada_cantidad = tk.Entry(marco_compra, width=10)
entrada_cantidad.grid(row=0, column=1, padx=5)
entrada_cantidad.insert(0, "1")

tk.Button(
    marco_compra,
    text="Agregar al carrito",
    bg="#ffcc00",
    font=("Arial", 10, "bold"),
    command=agregar_producto
).grid(row=0, column=2, padx=10)

# SECCION DEL CARRITO
marco_carrito = tk.LabelFrame(
    ventana,
    text="Carrito de compras",
    font=("Arial", 11, "bold"),
    bg="#eeeeee",
    padx=10,
    pady=10
)
marco_carrito.pack(fill="both", expand=True, padx=15, pady=5)

tabla_carrito = ttk.Treeview(
    marco_carrito,
    columns=("Producto", "Cantidad", "Precio", "Subtotal"),
    show="headings",
    height=5
)

for columna in ("Producto", "Cantidad", "Precio", "Subtotal"):
    tabla_carrito.heading(columna, text=columna)

tabla_carrito.pack(fill="both", expand=True)

# TOTAL DE LA COMPRA
etiqueta_total = tk.Label(
    ventana,
    text="TOTAL: $0.00",
    font=("Arial", 18, "bold"),
    bg="#eeeeee",
    fg="#cc0000"
)
etiqueta_total.pack(pady=10)

# BOTONES PRINCIPALES
marco_botones = tk.Frame(ventana, bg="#eeeeee")
marco_botones.pack(pady=10)

tk.Button(
    marco_botones,
    text="Eliminar producto",
    bg="#dddddd",
    command=eliminar_producto
).grid(row=0, column=0, padx=5)

tk.Button(
    marco_botones,
    text="Cobrar",
    bg="#28a745",
    fg="white",
    font=("Arial", 11, "bold"),
    command=realizar_venta
).grid(row=0, column=1, padx=5)

tk.Button(
    marco_botones,
    text="Historial de ventas",
    bg="#007bff",
    fg="white",
    command=consultar_ventas
).grid(row=0, column=2, padx=5)

# CARGAR LOS PRODUCTOS AL INICIAR
cargar_productos()

# EJECUTAR EL PROGRAMA
ventana.mainloop()

# CERRAR LA BASE DE DATOS AL FINALIZAR
conexion.close()
