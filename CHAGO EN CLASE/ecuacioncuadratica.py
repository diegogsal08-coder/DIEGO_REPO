import tkinter as tk
from tkinter import messagebox
import cmath


FONDO = "#eef2ff"
TARJETA = "#ffffff"
TEXTO = "#252b48"
ACENTO = "#5b5bd6"


def calcular():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        if a == 0:
            raise ValueError("El coeficiente a no puede ser cero.")

        discriminante = b ** 2 - 4 * a * c
        x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
        if discriminante >= 0:
            resultado = (
                "La ecuación tiene raíces reales:\n\n"
                f"x₁ = {x1.real:.6g}\n"
                f"x₂ = {x2.real:.6g}"
            )
        else:
            resultado = (
                "La ecuación tiene raíces complejas:\n\n"
                f"x₁ = {x1.real:.6g} + {abs(x1.imag):.6g}i\n"
                f"x₂ = {x2.real:.6g} - {abs(x2.imag):.6g}i"
            )

        caja_resultados.configure(state="normal")
        caja_resultados.delete("1.0", tk.END)
        caja_resultados.insert(tk.END, resultado)
        caja_resultados.configure(state="disabled")
    except ValueError as error:
        messagebox.showerror(
            "Datos no válidos",
            str(error) or "Escribe valores numéricos válidos para a, b y c.",
        )


def limpiar():
    entrada_a.delete(0, tk.END)
    entrada_b.delete(0, tk.END)
    entrada_c.delete(0, tk.END)
    caja_resultados.configure(state="normal")
    caja_resultados.delete("1.0", tk.END)
    caja_resultados.configure(state="disabled")
    entrada_a.focus_set()


ventana = tk.Tk()
ventana.title("Solucionar ecuación cuadrática")
ventana.geometry("480x570")
ventana.resizable(False, False)
ventana.configure(bg=FONDO)

tarjeta = tk.Frame(ventana, bg=TARJETA, padx=32, pady=28)
tarjeta.pack(padx=28, pady=28, fill="both", expand=True)

tk.Label(
    tarjeta,
    text="Ecuación cuadrática",
    font=("Segoe UI", 21, "bold"),
    fg=TEXTO,
    bg=TARJETA,
).pack(anchor="w")
tk.Label(
    tarjeta,
    text="Escribe los coeficientes de ax² + bx + c = 0",
    font=("Segoe UI", 10),
    fg="#68708c",
    bg=TARJETA,
).pack(anchor="w", pady=(4, 22))

entradas = []
for nombre, color in (("a", "#e9e8ff"), ("b", "#e5f5f2"), ("c", "#fff1df")):
    fila = tk.Frame(tarjeta, bg=TARJETA)
    fila.pack(fill="x", pady=6)
    tk.Label(
        fila,
        text=f"Coeficiente {nombre}",
        width=16,
        anchor="w",
        font=("Segoe UI", 11, "bold"),
        fg=TEXTO,
        bg=TARJETA,
    ).pack(side="left")
    campo = tk.Entry(
        fila,
        font=("Segoe UI", 12),
        relief="flat",
        bg=color,
        fg=TEXTO,
        insertbackground=TEXTO,
    )
    campo.pack(side="right", fill="x", expand=True, ipady=8, padx=(8, 0))
    entradas.append(campo)

entrada_a, entrada_b, entrada_c = entradas

tk.Label(
    tarjeta,
    text="Resultados",
    font=("Segoe UI", 11, "bold"),
    fg=TEXTO,
    bg=TARJETA,
).pack(anchor="w", pady=(22, 8))
caja_resultados = tk.Text(
    tarjeta,
    height=5,
    font=("Segoe UI", 11),
    bg="#f5f6fb",
    fg=TEXTO,
    relief="flat",
    padx=12,
    pady=10,
    wrap="word",
)
caja_resultados.pack(fill="x")
caja_resultados.configure(state="disabled")

botones = tk.Frame(tarjeta, bg=TARJETA)
botones.pack(fill="x", pady=(22, 0))
tk.Button(
    botones,
    text="Calcular",
    command=calcular,
    bg=ACENTO,
    fg="white",
    activebackground="#4848b5",
    activeforeground="white",
    relief="flat",
    font=("Segoe UI", 12, "bold"),
    padx=12,
    pady=14,
    cursor="hand2",
).pack(side="left", expand=True, fill="x", padx=(0, 4))
tk.Button(
    botones,
    text="Limpiar",
    command=limpiar,
    bg="#e7e9f2",
    fg=TEXTO,
    activebackground="#d7daea",
    relief="flat",
    font=("Segoe UI", 12, "bold"),
    padx=12,
    pady=14,
    cursor="hand2",
).pack(side="left", expand=True, fill="x", padx=4)
tk.Button(
    botones,
    text="Salir",
    command=ventana.destroy,
    bg="#ffe7e7",
    fg="#a33b45",
    activebackground="#ffd5d5",
    relief="flat",
    font=("Segoe UI", 12, "bold"),
    padx=12,
    pady=14,
    cursor="hand2",
).pack(side="left", expand=True, fill="x", padx=(4, 0))

ventana.bind("<Return>", lambda _evento: calcular())
entrada_a.focus_set()
ventana.mainloop()
