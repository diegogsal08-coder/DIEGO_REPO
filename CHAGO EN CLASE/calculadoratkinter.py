import tkinter as tk
from tkinter import messagebox


# Creamos la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Calculadora básica")
ventana.geometry("420x350")
ventana.resizable(False, False)

# Variable para guardar la operación elegida por el usuario
operacion = tk.StringVar()


# Función para validar que el contenido ingresado sea un número
# Acepta solo números enteros o decimales, evitando textos vacíos
# que puedan provocar errores al hacer cálculos.
def validar_numero(texto):
    if texto == "":
        return True
    try:
        float(texto)
        return True
    except ValueError:
        return False


# Función principal para realizar el cálculo
# Se valida que se hayan ingresado dos números y que haya una operación seleccionada.
def calcular():
    # Leemos lo escrito en los campos de entrada
    numero1 = entrada1.get()
    numero2 = entrada2.get()
    opcion = operacion.get()

    # Verificamos que ambos campos no estén vacíos
    if numero1 == "" or numero2 == "":
        messagebox.showerror("Error", "Debes ingresar los dos números.")
        return

    # Verificamos que la operación haya sido seleccionada
    if opcion == "":
        messagebox.showerror("Error", "Debes seleccionar una operación.")
        return

    # Convertimos los textos a números reales para poder operar
    try:
        n1 = float(numero1)
        n2 = float(numero2)
    except ValueError:
        messagebox.showerror("Error", "Solo se permiten números.")
        return

    # Validamos la división por cero antes de ejecutar la operación
    if opcion == "/" and n2 == 0:
        messagebox.showerror("Error", "No se puede dividir entre 0.")
        return

    # Realizamos el cálculo según la operación escogida
    if opcion == "+":
        resultado = n1 + n2
    elif opcion == "-":
        resultado = n1 - n2
    elif opcion == "*":
        resultado = n1 * n2
    elif opcion == "/":
        resultado = n1 / n2
    else:
        messagebox.showerror("Error", "Operación no válida.")
        return

    # Mostramos el resultado en la etiqueta correspondiente
    resultado_label.config(text=f"Resultado: {resultado}")


# Función para limpiar todos los campos y resetear la interfaz
# Se deja listo para una nueva operación.
def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    operacion.set("")
    resultado_label.config(text="Resultado: ")


# Función para cerrar la aplicación
# Se usa para salir de la ventana principal.
def salir():
    ventana.destroy()


# Etiqueta para indicar qué es cada caja de entrada
label1 = tk.Label(ventana, text="Número 1:")
label1.pack(pady=(20, 5))

entrada1 = tk.Entry(ventana, width=25)
entrada1.pack()

label2 = tk.Label(ventana, text="Número 2:")
label2.pack(pady=(15, 5))

entrada2 = tk.Entry(ventana, width=25)
entrada2.pack()

# Configuramos validación para que solo se permitan números en los campos
# validate="key" ejecuta la validación cada vez que el usuario escribe
# validatecommand recibe una función con la entrada que se está escribiendo.
# %P representa el texto que resultará del ingreso actual.
validar_cmd = (ventana.register(validar_numero), "%P")
entrada1.config(validate="key", validatecommand=validar_cmd)
entrada2.config(validate="key", validatecommand=validar_cmd)

# Radio buttons para elegir la operación
frame_operaciones = tk.Frame(ventana)
frame_operaciones.pack(pady=15)

radio_suma = tk.Radiobutton(frame_operaciones, text="+", variable=operacion, value="+")
radio_resta = tk.Radiobutton(frame_operaciones, text="-", variable=operacion, value="-")
radio_multi = tk.Radiobutton(frame_operaciones, text="*", variable=operacion, value="*")
radio_div = tk.Radiobutton(frame_operaciones, text="/", variable=operacion, value="/")

radio_suma.grid(row=0, column=0, padx=10)
radio_resta.grid(row=0, column=1, padx=10)
radio_multi.grid(row=0, column=2, padx=10)
radio_div.grid(row=0, column=3, padx=10)

# Botones principales de la calculadora
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=(5, 5))

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack()

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=(5, 5))

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado: ", font=("Arial", 12))
resultado_label.pack(pady=15)

# Iniciamos el bucle principal de la ventana
ventana.mainloop()
