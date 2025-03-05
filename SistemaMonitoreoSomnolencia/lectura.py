import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ZoomImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zoom y Desplazamiento de Imagen")

        # Crear el Canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Crear las barras de desplazamiento
        self.scrollbar_y = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y.grid(row=0, column=1, sticky="ns")

        self.scrollbar_x = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.grid(row=1, column=0, sticky="ew")

        self.canvas.config(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Cargar la imagen
        self.img = Image.open("lectura.png")
        self.img_tk = ImageTk.PhotoImage(self.img)

        # Crear el objeto de imagen en el canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, image=self.img_tk, anchor="nw")

        # Factor de zoom inicial (1.0 significa 100%)
        self.zoom_factor = 1.0

        # Añadir botones para hacer zoom
        self.zoom_in_btn = tk.Button(self.root, text="Zoom In", command=lambda: self.zoom(1.2))  # Aumentar tamaño
        self.zoom_in_btn.grid(row=2, column=0)

        self.zoom_out_btn = tk.Button(self.root, text="Zoom Out", command=lambda: self.zoom(0.8))  # Reducir tamaño
        self.zoom_out_btn.grid(row=2, column=1)

    def zoom(self, factor):
        # Actualizar el factor de zoom acumulado
        self.zoom_factor *= factor

        # Calcular el nuevo tamaño basado en el factor de zoom acumulado
        new_width = int(self.img.width * self.zoom_factor)
        new_height = int(self.img.height * self.zoom_factor)
        
        # Redimensionar la imagen
        img_resized = self.img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_resized)
        
        # Actualizar la imagen en el canvas
        self.canvas.itemconfig(self.image_on_canvas, image=img_tk)
        
        # Ajustar las dimensiones del canvas según el tamaño de la nueva imagen
        self.canvas.config(scrollregion=(0, 0, new_width, new_height))

        # Reajustar el tamaño de la imagen para las barras de desplazamiento
        self.canvas.config(width=self.root.winfo_width(), height=self.root.winfo_height())

        # Guardar la imagen redimensionada para evitar que se pierda en la próxima actualización
        self.img_tk = img_tk

# Crear la ventana principal
root = tk.Tk()

# Crear la aplicación
app = ZoomImageApp(root)

# Configurar las filas y columnas de la ventana principal
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciar la interfaz gráfica
root.mainloop()
