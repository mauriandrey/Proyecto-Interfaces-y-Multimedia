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

# Crear ventana principal con un diseño mejorado
root = tk.Tk()
root.title("Consulta de Análisis")
root.geometry("1000x500")  # Tamaño de la ventana ajustado
root.config(bg="#f0f0f0")  # Fondo gris claro para la ventana

# Mensajes de bienvenida con fuente personalizada
mensaje1 = tk.Label(root, text="¡Felicidades por completar nuestro monitoreo!", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#2c3e50")
mensaje1.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

mensaje2 = tk.Label(root, text="Puedes buscar tus análisis en base a tu usuario.", font=("Helvetica", 12), bg="#f0f0f0", fg="#7f8c8d")
mensaje2.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

# Campo de texto para el número de usuario con un estilo más atractivo
label_usuario = tk.Label(root, text="Ingresa tu número de usuario:", font=("Arial", 10), bg="#f0f0f0", fg="#34495e")
label_usuario.grid(row=2, column=0, padx=20, pady=10)
entrada_usuario = tk.Entry(root, width=25, font=("Arial", 10), bd=2, relief="solid")
entrada_usuario.grid(row=2, column=1, padx=10, pady=10)

# Botón para consultar con un estilo atractivo
boton_consultar = tk.Button(root, text="Consultar", command=consultar, width=15, font=("Arial", 12), bg="#3498db", fg="white", bd=0, relief="flat")
boton_consultar.grid(row=3, column=0, columnspan=2, padx=20, pady=15)

# Tabla para mostrar los resultados con el fondo blanco y bordes
treeview = ttk.Treeview(root, columns=("ci", "nombre", "tiempo ojos cerrados", "parpadeos totales", "PERCLOS", "Omisiones", "Comisiones", "tiempo promedio", "Conclusión"), show="headings")

# Ajustar el ancho de las columnas
treeview.column("ci", width=90)
treeview.column("nombre", width=120)
treeview.column("tiempo ojos cerrados", width=120)
treeview.column("parpadeos totales", width=120)
treeview.column("PERCLOS", width=90)
treeview.column("Omisiones", width=90)
treeview.column("Comisiones", width=110)
treeview.column("tiempo promedio", width=130)
treeview.column("Conclusión", width=130)

# Encabezados de las columnas con fondo y color de texto
treeview.heading("ci", text="ci", anchor="center")
treeview.heading("nombre", text="nombre", anchor="center")
treeview.heading("tiempo ojos cerrados", text="tiempo ojos cerrados", anchor="center")
treeview.heading("parpadeos totales", text="parpadeos totales", anchor="center")
treeview.heading("PERCLOS", text="PERCLOS", anchor="center")
treeview.heading("Omisiones", text="Omisiones", anchor="center")
treeview.heading("Comisiones", text="Comisiones", anchor="center")
treeview.heading("tiempo promedio", text="tiempo promedio", anchor="center")
treeview.heading("Conclusión", text="Conclusión", anchor="center")

# Establecer el color de fondo de las filas
treeview.tag_configure("evenrow", background="#ecf0f1")  # Fila par
treeview.tag_configure("oddrow", background="white")  # Fila impar

# Usamos pack para que la tabla se ajuste al tamaño de la ventana
treeview.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

# Configurar el comportamiento de los rows y columns para que se expandan
root.grid_rowconfigure(4, weight=1)  # Esto permite que la fila 4 (donde está la tabla) se expanda
root.grid_columnconfigure(0, weight=1)  # Esto permite que la columna 0 se expanda
root.grid_columnconfigure(1, weight=1)  # Esto permite que la columna 1 se expanda

# Botón de exportar a PDF con estilo
boton_exportar = tk.Button(root, text="Exportar PDF", width=15, font=("Arial", 12), bg="#2ecc71", fg="white", bd=0, relief="flat")
boton_exportar.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

# Botón de volver con estilo
boton_volver = tk.Button(root, text="Volver", width=15, font=("Arial", 12), bg="#e74c3c", fg="white", bd=0, relief="flat")
boton_volver.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

# Ejecutar la interfaz
root.mainloop()
