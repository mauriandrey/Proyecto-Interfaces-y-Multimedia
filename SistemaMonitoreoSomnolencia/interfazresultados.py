import tkinter as tk
from tkinter import ttk

def consultar():
    # Aquí iría la lógica para conectar con PostgreSQL y obtener los datos
    # Por ahora se simula un resultado de ejemplo
    resultado = [
        ("174322525", "Stalin", "10 segundos", "1500", "12%", "5", "3", "30 segundos", "Aprobado")
    ]
    
    # Limpiar la tabla antes de insertar los nuevos resultados
    for row in treeview.get_children():
        treeview.delete(row)
    
    # Insertar los resultados en la tabla
    for r in resultado:
        treeview.insert("", tk.END, values=r)

# Crear ventana principal con tonos azules
root = tk.Tk()
root.title("Consulta de Análisis")
root.geometry("1200x600")  # Ventana más grande
root.config(bg="#A9CFE7")  # Fondo azul claro para la ventana

# Mensajes de bienvenida con colores suaves y mayor tamaño
mensaje1 = tk.Label(root, text="¡Felicidades por completar nuestro monitoreo!", font=("Helvetica", 16, "bold"), bg="#A9CFE7", fg="#1F3A6E")
mensaje1.grid(row=0, column=0, columnspan=2, padx=30, pady=15)

mensaje2 = tk.Label(root, text="Puedes buscar tus análisis en base a tu usuario.", font=("Helvetica", 14), bg="#A9CFE7", fg="#2A56A3")
mensaje2.grid(row=1, column=0, columnspan=2, padx=30, pady=10)

# Campo de texto para el número de usuario con borde suave y mayor tamaño
label_usuario = tk.Label(root, text="Ingresa tu número de usuario:", font=("Arial", 12), bg="#A9CFE7", fg="#1F3A6E")
label_usuario.grid(row=2, column=0, padx=30, pady=15)
entrada_usuario = tk.Entry(root, width=30, font=("Arial", 12), bd=2, relief="solid", highlightbackground="#4C8DFF", highlightcolor="#4C8DFF")
entrada_usuario.grid(row=2, column=1, padx=20, pady=15)

# Estilo para los botones con cambio de color al pasar el cursor
def on_enter(boton, color):
    boton.config(bg=color)

def on_leave(boton, color):
    boton.config(bg=color)

# Botón para consultar con colores suaves y efecto hover
boton_consultar = tk.Button(root, text="Consultar", command=consultar, width=20, font=("Arial", 14), bg="#4C8DFF", fg="white", bd=2, relief="raised")
boton_consultar.grid(row=3, column=0, columnspan=2, padx=30, pady=20)
boton_consultar.bind("<Enter>", lambda e: on_enter(boton_consultar, "#3575E5"))  # Hover color
boton_consultar.bind("<Leave>", lambda e: on_leave(boton_consultar, "#4C8DFF"))  # Color normal

# Crear un frame para contener la tabla y centrarla
frame = tk.Frame(root, bg="#A9CFE7")
frame.grid(row=4, column=0, columnspan=2, padx=50, pady=20, sticky="nsew")

# Tabla para mostrar los resultados con el fondo blanco y bordes
treeview = ttk.Treeview(frame, columns=("ci", "nombre", "tiempo ojos cerrados", "parpadeos totales", "PERCLOS", "Omisiones", "Comisiones", "tiempo promedio", "Conclusión"), show="headings")

# Ajustar el ancho de las columnas (más grandes)
treeview.column("ci", width=120, anchor="center", stretch=False)
treeview.column("nombre", width=160, anchor="center", stretch=False)
treeview.column("tiempo ojos cerrados", width=160, anchor="center", stretch=False)
treeview.column("parpadeos totales", width=160, anchor="center", stretch=False)
treeview.column("PERCLOS", width=120, anchor="center", stretch=False)
treeview.column("Omisiones", width=120, anchor="center", stretch=False)
treeview.column("Comisiones", width=140, anchor="center", stretch=False)
treeview.column("tiempo promedio", width=160, anchor="center", stretch=False)
treeview.column("Conclusión", width=160, anchor="center", stretch=False)

# Encabezados de las columnas con fondo azul y color blanco
treeview.heading("ci", text="ci", anchor="center")
treeview.heading("nombre", text="nombre", anchor="center")
treeview.heading("tiempo ojos cerrados", text="tiempo ojos cerrados", anchor="center")
treeview.heading("parpadeos totales", text="parpadeos totales", anchor="center")
treeview.heading("PERCLOS", text="PERCLOS", anchor="center")
treeview.heading("Omisiones", text="Omisiones", anchor="center")
treeview.heading("Comisiones", text="Comisiones", anchor="center")
treeview.heading("tiempo promedio", text="tiempo promedio", anchor="center")
treeview.heading("Conclusión", text="Conclusión", anchor="center")

# Establecer el color de fondo de las filas con bordes
treeview.tag_configure("evenrow", background="#E3F2FD")  # Fila par con color azul muy claro
treeview.tag_configure("oddrow", background="white")  # Fila impar blanca

# Usamos grid para que la tabla se ajuste al tamaño de la ventana dentro del frame
treeview.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

# Configurar el comportamiento de los rows y columns para que se expandan dentro del frame
frame.grid_rowconfigure(0, weight=1)  # Esto permite que la fila 0 (donde está la tabla) se expanda
frame.grid_columnconfigure(0, weight=1)  # Esto permite que la columna 0 se expanda

# Botón de exportar a PDF con colores suaves y efecto hover
boton_exportar = tk.Button(root, text="Exportar PDF", width=20, font=("Arial", 14), bg="#64B5F6", fg="white", bd=2, relief="raised")
boton_exportar.grid(row=5, column=0, columnspan=2, padx=30, pady=20)
boton_exportar.bind("<Enter>", lambda e: on_enter(boton_exportar, "#42A5F5"))  # Hover color
boton_exportar.bind("<Leave>", lambda e: on_leave(boton_exportar, "#64B5F6"))  # Color normal

# Botón de volver con colores suaves y efecto hover
boton_volver = tk.Button(root, text="Volver", width=20, font=("Arial", 14), bg="#FF7043", fg="white", bd=2, relief="raised")
boton_volver.grid(row=6, column=0, columnspan=2, padx=30, pady=20)
boton_volver.bind("<Enter>", lambda e: on_enter(boton_volver, "#FF5722"))  # Hover color
boton_volver.bind("<Leave>", lambda e: on_leave(boton_volver, "#FF7043"))  # Color normal

# Ejecutar la interfaz
root.mainloop()
