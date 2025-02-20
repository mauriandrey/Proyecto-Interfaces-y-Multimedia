import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

cap = None
camara_encendida = False

# Crear la ventana principal primero
root = tk.Tk()
root.title("Interfaz Gráfica")
root.geometry("800x500")
root.minsize(600, 400)
root.configure(bg="#2E4053")  # Fondo oscuro para reducir fatiga visual

# Cargar imágenes después de crear la ventana principal
img_camara_on = tk.PhotoImage(file="imagenes/camara-encendida.png")
img_camara_off = tk.PhotoImage(file="imagenes/camara-apagada.png")

def toggle_camara():
    """ Alterna entre encender y apagar la cámara. """
    global camara_encendida
    if camara_encendida:
        apagar_camara()
    else:
        iniciar_camara()

def iniciar_camara():
    """ Inicia la cámara y actualiza el feed en el marco de la interfaz. """
    global cap, camara_encendida
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "No se pudo abrir la cámara")
        return
    
    camara_encendida = True
    btn_camara.config(text="Apagar cámara", image=img_camara_on, compound=tk.LEFT, padx=10)
    
    def actualizar_frame():
        if camara_encendida:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = img.resize((marco_camara.winfo_width(), marco_camara.winfo_height()))
                imgtk = ImageTk.PhotoImage(image=img)
                camara_label.imgtk = imgtk
                camara_label.configure(image=imgtk)
                camara_label.after(10, actualizar_frame)
            else:
                apagar_camara()
    
    camara_label = tk.Label(marco_camara, bg="#1C2833")
    camara_label.pack(fill=tk.BOTH, expand=True)
    actualizar_frame()

def apagar_camara():
    """ Apaga la cámara y limpia el frame de la interfaz. """
    global cap, camara_encendida
    if cap and cap.isOpened():
        cap.release()
    
    camara_encendida = False
    btn_camara.config(text="Iniciar cámara", image=img_camara_off, compound=tk.LEFT)

    # Limpiar la imagen mostrada en el widget de la cámara
    for widget in marco_camara.winfo_children():
        widget.destroy()

def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Aquí irá la información de ayuda")

def on_enter(event):
    event.widget.config(bg="#1F618D", fg="#F7DC6F")  # Cambio de color al pasar el cursor

def on_leave(event):
    event.widget.config(bg="#283747", fg="#F7DC6F")  # Restauración del color

def on_press(event):
    event.widget.config(relief=tk.SUNKEN)  # Cambio de relieve al presionar

def on_release(event):
    event.widget.config(relief=tk.RAISED)  # Restauración del relieve

# Frame superior principal con estilo
frame_superior = tk.Frame(root, bg="#34495E", padx=10, pady=10, relief=tk.RIDGE, bd=5)
frame_superior.pack(side=tk.TOP, fill=tk.X)

# Mensaje de bienvenida estilizado
bienvenida = tk.Label(frame_superior, text="¡Bienvenido!, siempre es un gusto tener aquí <usuario>", font=("Arial", 14, "bold"), fg="#F7DC6F", bg="#34495E", anchor="w")
bienvenida.pack(side=tk.LEFT, padx=10, pady=20)

# Frame que contiene el menú lateral y el contenido
frame_principal = tk.Frame(root, bg="#2E4053")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Menú lateral con diseño
frame_menu = tk.Frame(frame_principal, width=300, height=500, bg="#1C2833", padx=30, pady=10, relief=tk.RIDGE, bd=5)
frame_menu.pack(side=tk.LEFT, fill=tk.Y)

# Estilos de botones
btn_style = {"font": ("Arial", 12, "bold"), "fg": "#F7DC6F", "bg": "#283747", "relief": tk.RAISED, "bd": 3, "activebackground": "#566573", "activeforeground": "#F7DC6F"}

botones = []
actividad_img = tk.PhotoImage(file="imagenes/actividad.png").subsample(8, 8)
btn_actividades = tk.Button(frame_menu, text="Actividades", image=actividad_img, compound=tk.LEFT, width=20, height=100, **btn_style)
btn_actividades.pack(pady=10, fill=tk.X)
botones.append(btn_actividades)

test_img = tk.PhotoImage(file="imagenes/test.png").subsample(9, 9)
btn_test = tk.Button(frame_menu, text="Test", image=test_img, compound=tk.LEFT, width=15, height=100, padx=25,  **btn_style)
btn_test.pack(pady=10, fill=tk.X)
botones.append(btn_test)

resultado_img = tk.PhotoImage(file="imagenes/resultado.png").subsample(8, 8)
btn_resultados = tk.Button(frame_menu, text="Resultados", image=resultado_img, compound=tk.LEFT, width=25, height=100, **btn_style)
btn_resultados.pack(pady=10, fill=tk.X)
botones.append(btn_resultados)

btn_salir = tk.Button(frame_menu, text="Salir", width=25, height=100, **btn_style)
btn_salir.pack(pady=100, fill=tk.X)
botones.append(btn_salir)

# Agregar eventos a los botones
for btn in botones:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<ButtonPress-1>", on_press)
    btn.bind("<ButtonRelease-1>", on_release)

# Área de contenido principal dentro de frame_principal
frame_contenido = tk.Frame(frame_principal, bg="#2E4053")
frame_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Nuevo frame para la cámara
frame_camara = tk.Frame(frame_contenido, width=1500, height=600, bg="#1C2833", relief=tk.SUNKEN, bd=5)
frame_camara.pack(fill=tk.NONE, expand=True, padx=20, pady=20)

# Marco para mostrar contenido (widget para la cámara)
marco_camara = tk.LabelFrame(frame_camara, text="Vista de cámara", font=("Arial", 12, "bold"), fg="#F7DC6F", bg="#1C2833", width=1000, height=500, relief=tk.GROOVE, bd=4)
marco_camara.pack(fill=tk.NONE, expand=True, padx=10, pady=10)
marco_camara.pack_propagate(False)

# Botón para iniciar la cámara, debajo del frame de la cámara
btn_camara = tk.Button(frame_camara, text="Iniciar cámara", image=img_camara_off, command=toggle_camara, **btn_style)
btn_camara.pack(pady=10)
btn_camara.bind("<Enter>", on_enter)
btn_camara.bind("<Leave>", on_leave)
btn_camara.bind("<ButtonPress-1>", on_press)
btn_camara.bind("<ButtonRelease-1>", on_release)

# Botón de ayuda en la parte inferior derecha
frame_ayuda = tk.Frame(root, bg="#2E4053")
frame_ayuda.place(relx=0.98, rely=0.98, anchor=tk.SE)

btn_ayuda = tk.Button(frame_ayuda, text="Ayuda", command=mostrar_ayuda, **btn_style)
btn_ayuda.pack()
btn_ayuda.bind("<Enter>", on_enter)
btn_ayuda.bind("<Leave>", on_leave)
btn_ayuda.bind("<ButtonPress-1>", on_press)
btn_ayuda.bind("<ButtonRelease-1>", on_release)

# Iniciar el bucle de la aplicación
root.mainloop()
