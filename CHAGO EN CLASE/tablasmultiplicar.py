import customtkinter as ctk
from tkinter import messagebox


def mostrar_vacio():
    ctk.CTkLabel(
        resultados,
        text="Configura los rangos y presiona «Calcular» para ver las tablas.",
        text_color=("gray45", "gray70"),
        font=ctk.CTkFont(size=14),
        wraplength=560,
    ).pack(pady=36)


def calcular():
    try:
        tabla_inicial = int(entrada_tabla_inicial.get())
        tabla_final = int(entrada_tabla_final.get())
        multiplicacion_inicial = int(entrada_multiplicacion_inicial.get())
        multiplicacion_final = int(entrada_multiplicacion_final.get())
    except ValueError:
        messagebox.showerror("Datos incorrectos", "Completa las cuatro cajas con números enteros.")
        return

    if tabla_inicial > tabla_final or multiplicacion_inicial > multiplicacion_final:
        messagebox.showerror(
            "Rango incorrecto",
            "Cada valor inicial debe ser menor o igual que su valor final.",
        )
        return

    for elemento in resultados.winfo_children():
        elemento.destroy()

    titulo_resultado.configure(text=f"Tablas del {tabla_inicial} al {tabla_final}")
    for numero_tabla in range(tabla_inicial, tabla_final + 1):
        grupo = ctk.CTkFrame(resultados, corner_radius=12, fg_color=("gray94", "gray20"))
        grupo.pack(fill="x", padx=8, pady=6)

        ctk.CTkLabel(
            grupo,
            text=f"Tabla del {numero_tabla}",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w",
        ).pack(fill="x", padx=16, pady=(12, 6))

        for multiplicador in range(multiplicacion_inicial, multiplicacion_final + 1):
            fila = ctk.CTkFrame(grupo, fg_color="transparent")
            fila.pack(fill="x", padx=16, pady=3)
            ctk.CTkLabel(
                fila,
                text=f"{numero_tabla} × {multiplicador}",
                font=ctk.CTkFont(size=14),
                anchor="w",
            ).pack(side="left", fill="x", expand=True)
            ctk.CTkLabel(
                fila,
                text=str(numero_tabla * multiplicador),
                text_color=("#2563EB", "#60A5FA"),
                font=ctk.CTkFont(size=14, weight="bold"),
                anchor="e",
            ).pack(side="right")

        ctk.CTkFrame(grupo, height=8, fg_color="transparent").pack()


def limpiar():
    for entrada in (
        entrada_tabla_inicial,
        entrada_tabla_final,
        entrada_multiplicacion_inicial,
        entrada_multiplicacion_final,
    ):
        entrada.delete(0, "end")

    for elemento in resultados.winfo_children():
        elemento.destroy()
    titulo_resultado.configure(text="Tus resultados")
    mostrar_vacio()


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Tablas de multiplicar")
ventana.geometry("760x780")
ventana.minsize(650, 680)

contenedor = ctk.CTkFrame(ventana, fg_color="transparent")
contenedor.pack(fill="both", expand=True, padx=28, pady=24)
contenedor.grid_columnconfigure((0, 1), weight=1)
contenedor.grid_rowconfigure(4, weight=1)

ctk.CTkLabel(
    contenedor,
    text="Tablas de multiplicar",
    font=ctk.CTkFont(size=28, weight="bold"),
).grid(row=0, column=0, columnspan=2, sticky="w")
ctk.CTkLabel(
    contenedor,
    text="Elige tus rangos y genera las tablas en segundos.",
    text_color=("gray45", "gray70"),
    font=ctk.CTkFont(size=14),
).grid(row=1, column=0, columnspan=2, sticky="w", pady=(2, 18))

marco_entradas = ctk.CTkFrame(contenedor, corner_radius=16)
marco_entradas.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 16))
marco_entradas.grid_columnconfigure((0, 1), weight=1)


def crear_campo(texto, fila, columna):
    campo = ctk.CTkFrame(marco_entradas, fg_color="transparent")
    campo.grid(row=fila, column=columna, sticky="ew", padx=16, pady=10)
    ctk.CTkLabel(
        campo,
        text=texto,
        font=ctk.CTkFont(size=13, weight="bold"),
        anchor="w",
    ).pack(fill="x", pady=(0, 6))
    entrada = ctk.CTkEntry(campo, height=38, corner_radius=10)
    entrada.pack(fill="x")
    return entrada


entrada_tabla_inicial = crear_campo("Tabla inicial", 0, 0)
entrada_tabla_final = crear_campo("Tabla final", 0, 1)
entrada_multiplicacion_inicial = crear_campo("Multiplicador inicial", 1, 0)
entrada_multiplicacion_final = crear_campo("Multiplicador final", 1, 1)

marco_botones = ctk.CTkFrame(contenedor, fg_color="transparent")
marco_botones.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 16))
ctk.CTkButton(
    marco_botones,
    text="Calcular",
    command=calcular,
    height=40,
    corner_radius=10,
    font=ctk.CTkFont(size=14, weight="bold"),
).pack(side="left", padx=(0, 8))
ctk.CTkButton(
    marco_botones,
    text="Limpiar",
    command=limpiar,
    height=40,
    corner_radius=10,
    fg_color="#16A34A",
    hover_color="#15803D",
    font=ctk.CTkFont(size=14, weight="bold"),
).pack(side="left", padx=8)
ctk.CTkButton(
    marco_botones,
    text="Salir",
    command=ventana.destroy,
    height=40,
    corner_radius=10,
    fg_color="#DC2626",
    hover_color="#B91C1C",
    font=ctk.CTkFont(size=14, weight="bold"),
).pack(side="right")

marco_resultados = ctk.CTkFrame(contenedor, corner_radius=16)
marco_resultados.grid(row=4, column=0, columnspan=2, sticky="nsew")
marco_resultados.grid_rowconfigure(1, weight=1)
marco_resultados.grid_columnconfigure(0, weight=1)

titulo_resultado = ctk.CTkLabel(
    marco_resultados,
    text="Tus resultados",
    font=ctk.CTkFont(size=18, weight="bold"),
    anchor="w",
)
titulo_resultado.grid(row=0, column=0, sticky="ew", padx=18, pady=(16, 8))
resultados = ctk.CTkScrollableFrame(
    marco_resultados,
    fg_color="transparent",
    corner_radius=0,
)
resultados.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 8))
mostrar_vacio()

ventana.mainloop()
