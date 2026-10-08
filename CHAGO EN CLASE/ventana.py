import tkinter as tk

ventana = tk.Tk()                 # 1. Crear la ventana
ventana.title("Mi ventana")       # 2. Ponerle título
ventana.geometry("400x300")       # 3. Definir tamaño (ancho x alto)

etiqueta = tk.Label(ventana, text="¡Hola, mundo!", font=("Arial", 18), bg="lightblue") #Etiqueta con texto y color de fondo 
etiqueta.pack(pady=40) #pack hace que la etiqueta se muestre en la ventana y pady agrega espacio vertical alrededor de la etiqueta
etiqueta2 = tk.Label(ventana, text="ingeniero", font=("Arial", 25), bg="lightgreen") # etiqueta con texto y color de fondo
etiqueta2.pack(pady=20)
boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
boton.pack()

ventana.mainloop()                # 4. Mantener la ventana abierta