"""
Mini editor de texto con Tkinter
--------------------------------
Universidad Autónoma de Zacatecas (UAZ) - UAIE
Materia: Programación Básica
Equipo: Jerezanos Tostaderos
Integrantes: Diego Guijarro Saldaña, Carlos Andre Castañon Davila,
             Hector Daniel Roman Cornejo

Descripción:
    Programa con interfaz gráfica que abre, edita y guarda archivos .txt.
    Usa tres componentes de Tkinter:
      - Menu       : barra superior con los menús Archivo y Ayuda.
      - Filedialog : ventanas para elegir el archivo a abrir o guardar.
      - Messagebox : avisos, errores y confirmación para salir.
"""

import tkinter as tk
from tkinter import messagebox, filedialog

# Tipos de archivo que mostrarán los cuadros de diálogo
TIPOS = [("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]


# ---------------------------------------------------------------- funciones
def abrir(evento=None):
    """Pide un archivo y muestra su contenido en el cuadro de texto."""
    ruta = filedialog.askopenfilename(title="Abrir archivo", filetypes=TIPOS)
    if ruta:                                  # ruta == "" si el usuario cancela
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            texto.delete("1.0", tk.END)       # borra el texto anterior
            texto.insert("1.0", contenido)    # escribe el nuevo contenido
            messagebox.showinfo("Aviso", "Archivo abierto")
        except (OSError, UnicodeDecodeError):
            messagebox.showerror("Error", "No se pudo abrir el archivo")
    return "break"    # evita que Tk ejecute su atajo predeterminado


def guardar(evento=None):
    """Pide un nombre y guarda en él el contenido del cuadro de texto."""
    ruta = filedialog.asksaveasfilename(title="Guardar como",
                                        defaultextension=".txt",
                                        filetypes=TIPOS)
    if ruta:
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(texto.get("1.0", "end-1c"))   # sin el salto final
            messagebox.showinfo("Aviso", "Archivo guardado")
        except OSError:
            messagebox.showerror("Error", "No se pudo guardar el archivo")
    return "break"


def salir():
    """Pregunta al usuario si desea cerrar el programa."""
    if messagebox.askyesno("Salir", "¿Seguro que deseas salir?"):
        ventana.destroy()                     # Sí: cierra la ventana
    else:
        messagebox.showinfo("Aviso", "Seguimos trabajando")


def acerca_de():
    """Muestra la información del equipo."""
    messagebox.showinfo("Acerca de",
                        "Mini editor de texto\nEquipo: Jerezanos Tostaderos")


# ---------------------------------------------------------------- interfaz
ventana = tk.Tk()
ventana.title("Mini editor")

texto = tk.Text(ventana, width=50, height=12)
texto.pack(fill="both", expand=True)
texto.focus_set()

# Barra de menús
barra = tk.Menu(ventana)
ventana.config(menu=barra)                    # conecta la barra a la ventana

archivo = tk.Menu(barra, tearoff=0)           # tearoff=0 quita la línea punteada
archivo.add_command(label="Abrir", accelerator="Ctrl+O", command=abrir)
archivo.add_command(label="Guardar como", accelerator="Ctrl+S", command=guardar)
archivo.add_separator()
archivo.add_command(label="Salir", command=salir)
barra.add_cascade(label="Archivo", menu=archivo)

ayuda = tk.Menu(barra, tearoff=0)
ayuda.add_command(label="Acerca de", command=acerca_de)
barra.add_cascade(label="Ayuda", menu=ayuda)

# ---------------------------------------------------------------- eventos
texto.bind("<Control-o>", abrir)              # atajo de teclado Ctrl+O
texto.bind("<Control-s>", guardar)            # atajo de teclado Ctrl+S
ventana.protocol("WM_DELETE_WINDOW", salir)   # al pulsar la X de la ventana

ventana.mainloop()