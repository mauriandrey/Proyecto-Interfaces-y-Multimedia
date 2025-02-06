import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql
from pantallaCarga import show_loading_screen


# Función para el ingreso de usuario
def ingreso_usuario():
    """
    Crea una ventana Toplevel para que el usuario ingrese sus credenciales.
    Utiliza wait_window para esperar a que se cierre la ventana y retorna True si el login es correcto,
    False en caso contrario.
    """
    # Variable mutable para almacenar el resultado del login (True/False)
    resultado = [False]  # Usamos una lista para que sea mutable desde las funciones internas

    # Crear la ventana de ingreso (Toplevel)
    ventana_ingreso = tk.Toplevel()
    ventana_ingreso.title("Ingreso de usuario")
    ventana_ingreso.geometry("400x250")

    # Etiqueta en la parte superior
    etiqueta = tk.Label(ventana_ingreso, text="Por favor ingrese su CI y Contraseña", font=("Arial", 12))
    etiqueta.pack(pady=10)

    # Función para validar que solo se permita números en el CI
    def validar_ci_contrasena(event):
        if event.char == '\x08':  # Permitir Backspace
            return None
        if not event.char.isdigit():
            return "break"

    # Función para validar que solo se permita texto (sin restricciones para la contraseña en este ejemplo)
    def validar_contrasena(event):
        if event.char == '\x08':  # Permitir Backspace
            return None
        return None

    # Funciones para manejar el placeholder
    def on_focus_in(event, placeholder, entry_widget):
        if entry_widget.get() == placeholder:
            entry_widget.delete(0, "end")
            entry_widget.config(fg="black")

    def on_focus_out(event, placeholder, entry_widget):
        if entry_widget.get() == "":
            entry_widget.insert(0, placeholder)
            entry_widget.config(fg="gray")

    # Crear caja de texto para CI
    label_ci = tk.Label(ventana_ingreso, text="CI:")
    label_ci.pack()
    entry_ci = tk.Entry(ventana_ingreso, width=30, fg="gray")
    placeholder_ci = "CI:171000000"
    entry_ci.insert(0, placeholder_ci)
    entry_ci.bind("<FocusIn>", lambda event, ph=placeholder_ci, widget=entry_ci: on_focus_in(event, ph, widget))
    entry_ci.bind("<FocusOut>", lambda event, ph=placeholder_ci, widget=entry_ci: on_focus_out(event, ph, widget))
    entry_ci.bind("<KeyPress>", validar_ci_contrasena)
    entry_ci.pack(pady=5)

    # Crear caja de texto para Contraseña
    label_contrasena = tk.Label(ventana_ingreso, text="Contraseña:")
    label_contrasena.pack()
    entry_contrasena = tk.Entry(ventana_ingreso, width=30, show="*", fg="gray")
    placeholder_contra = "Contraseña"
    entry_contrasena.insert(0, placeholder_contra)
    entry_contrasena.bind("<FocusIn>", lambda event, ph=placeholder_contra, widget=entry_contrasena: on_focus_in(event, ph, widget))
    entry_contrasena.bind("<FocusOut>", lambda event, ph=placeholder_contra, widget=entry_contrasena: on_focus_out(event, ph, widget))
    entry_contrasena.bind("<KeyPress>", validar_contrasena)
    entry_contrasena.pack(pady=5)

    # Función para verificar campos y validar credenciales
    def verificar_campos():
        if entry_ci.get() == "" or entry_ci.get() == placeholder_ci:
            messagebox.showwarning("Error", "El campo 'CI' no puede estar vacío.")
            return
        if entry_contrasena.get() == "" or entry_contrasena.get() == placeholder_contra:
            messagebox.showwarning("Error", "El campo 'Contraseña' no puede estar vacío.")
            return

        ci = entry_ci.get()
        contrasena = entry_contrasena.get()

        if verificar_ingreso_usuario(ci, contrasena):
           # messagebox.showinfo("Ingreso Exitoso", "Has ingresado correctamente.")
            resultado[0] = True
            ventana_ingreso.destroy()  # Cierra la ventana de ingreso
        else:
            messagebox.showwarning("Error", "CI o contraseña incorrectos.")
            # No se cierra la ventana; el usuario puede intentarlo nuevamente.

    # Botón para verificar los campos y realizar el login
    boton_ingresar = tk.Button(ventana_ingreso, text="Ingresar", command=verificar_campos)
    boton_ingresar.pack(pady=10)

    # En lugar de llamar a mainloop() aquí, usamos wait_window() para esperar a que se cierre la ventana
    ventana_ingreso.wait_window()

    return resultado[0]
    

# Función para agregar un nuevo usuario
def nuevo_usuario():
    # Crear una nueva ventana para el registro
    ventana_registro = tk.Toplevel()  # Nueva ventana secundaria
    ventana_registro.title("Registro de nuevo usuario")
    ventana_registro.geometry("400x300")

    # Etiqueta en la parte superior
    etiqueta = tk.Label(ventana_registro, text="Por favor ingrese los siguientes datos para su registro", font=("Arial", 12))
    etiqueta.pack(pady=10)

    # Función para validar que solo se permita texto (sin números, sin espacio ni caracteres especiales)
    def validar_nombre(event):
        # Permitir la tecla Backspace (clave 8)
        if event.char == '\x08':  # '\x08' es el código de Backspace
            return None  # No bloqueamos Backspace
        if not event.char.isalpha():  # Solo permite letras
            return "break"  # Bloquear la tecla si no es una letra
        if event.char == " ":
            return "break"  # Bloquear la tecla de espacio

    # Función para validar que solo se permita números
    def validar_ci_contrasena(event):
        # Permitir la tecla Backspace (clave 8)
        if event.char == '\x08':  # '\x08' es el código de Backspace
            return None  # No bloqueamos Backspace
        if not event.char.isdigit():  # Solo permite números
            return "break"  # Bloquear la tecla si no es un número

    # Función para manejar el placeholder (texto por defecto en la caja de texto)
    def on_focus_in(event, placeholder, entry_widget):
        if entry_widget.get() == placeholder:
            entry_widget.delete(0, "end")
            entry_widget.config(fg="black")  # Texto negro al escribir

    def on_focus_out(event, placeholder, entry_widget):
        if entry_widget.get() == "":
            entry_widget.insert(0, placeholder)
            entry_widget.config(fg="gray")  # Texto gris como placeholder

    # Crear la caja de texto para el Nombre (con placeholder)
    label_nombre = tk.Label(ventana_registro, text="Nombre:")
    label_nombre.pack()
    entry_nombre = tk.Entry(ventana_registro, width=30, fg="gray")
    entry_nombre.insert(0, "Nombre")  # Texto de referencia inicial
    entry_nombre.bind("<FocusIn>", lambda event, placeholder="Nombre", entry_widget=entry_nombre: on_focus_in(event, placeholder, entry_widget))
    entry_nombre.bind("<FocusOut>", lambda event, placeholder="Nombre", entry_widget=entry_nombre: on_focus_out(event, placeholder, entry_widget))
    entry_nombre.bind("<KeyPress>", validar_nombre)  # Solo texto permitido
    entry_nombre.pack(pady=5)

    # Crear la caja de texto para CI (con placeholder)
    label_ci = tk.Label(ventana_registro, text="CI:")
    label_ci.pack()
    entry_ci = tk.Entry(ventana_registro, width=30, fg="gray")
    entry_ci.insert(0, "CI:171000000")  # Texto de referencia inicial
    entry_ci.bind("<FocusIn>", lambda event, placeholder="CI:171000000", entry_widget=entry_ci: on_focus_in(event, placeholder, entry_widget))
    entry_ci.bind("<FocusOut>", lambda event, placeholder="CI:171000000", entry_widget=entry_ci: on_focus_out(event, placeholder, entry_widget))
    entry_ci.bind("<KeyPress>", validar_ci_contrasena)  # Solo números permitidos
    entry_ci.pack(pady=5)

    # Crear la caja de texto para Contraseña (con placeholder)
    label_contrasena = tk.Label(ventana_registro, text="Contraseña:")
    label_contrasena.pack()
    entry_contrasena = tk.Entry(ventana_registro, width=30, show="*", fg="gray")
    entry_contrasena.insert(0, "Contraseña")  # Texto de referencia inicial
    entry_contrasena.bind("<FocusIn>", lambda event, placeholder="Contraseña", entry_widget=entry_contrasena: on_focus_in(event, placeholder, entry_widget))
    entry_contrasena.bind("<FocusOut>", lambda event, placeholder="Contraseña", entry_widget=entry_contrasena: on_focus_out(event, placeholder, entry_widget))
    entry_contrasena.bind("<KeyPress>", validar_ci_contrasena)  # Solo números permitidos
    entry_contrasena.pack(pady=5)

    # Función para verificar si las cajas no están vacías
    def verificar_campos():
        if entry_nombre.get() == "" or entry_nombre.get() == "Nombre":
            messagebox.showwarning("Error", "El campo 'Nombre' no puede estar vacío.")
            return
        if entry_ci.get() == "" or entry_ci.get() == "CI:171000000":
            messagebox.showwarning("Error", "El campo 'CI' no puede estar vacío.")
            return
        if entry_contrasena.get() == "" or entry_contrasena.get() == "Contraseña":
            messagebox.showwarning("Error", "El campo 'Contraseña' no puede estar vacío.")
            return

        # Aquí puedes agregar la función de guardar los usuarios en la base de datos o archivo
        # Por ejemplo, puedes agregar una llamada a tu función para guardar en PostgreSQL
        
        # Guardar el usuario en la base de datos
        nombre = entry_nombre.get()
        ci = entry_ci.get()
        contrasena = entry_contrasena.get()
        
        # Verificar si el CI ya existe en la base de datos
        if verificar_ci_existente(ci):
            messagebox.showwarning("Error", "El CI ya está registrado.")
            return
        
        # Llamar a la función para guardar el usuario
        guardar_usuario(nombre, ci, contrasena)

        # Mostrar el mensaje de registro exitoso
        messagebox.showinfo("Registro Exitoso", "El usuario ha sido registrado correctamente.")
        ventana_registro.destroy()  # Cerrar la ventana de registro

    # Botón para verificar los campos
    boton_guardar = tk.Button(ventana_registro, text="Registrar", command=verificar_campos)
    boton_guardar.pack(pady=10)

    # Ejecutar la ventana de registro
    ventana_registro.mainloop()

def obtener_conexion():
    # Establece la conexión a la base de datos
    conn = psycopg2.connect(
        host="localhost",  # o la dirección de tu servidor
        dbname="Interfaces",  # Nombre de la base de datos
        user="postgres",  # Usuario
        password="admin123"  # Contraseña Version Stalin: 1234
    )
    return conn

def verificar_ci_existente(ci):
    try:
        # Obtener la conexión
        conn = obtener_conexion()
        cursor = conn.cursor()

        # Consulta SQL para verificar si el CI existe
        query = sql.SQL("SELECT 1 FROM usuarios WHERE ci = %s")
        cursor.execute(query, (ci,))

        # Comprobar si se encontró algún registro
        existe = cursor.fetchone()  # Devuelve None si no encuentra ningún registro

        # Cerrar la conexión
        cursor.close()
        conn.close()

        if existe:
            return True  # El CI ya existe
        else:
            return False  # El CI no existe
    except Exception as e:
        print(f"Error al verificar el CI: {e}")
        return False  # Asumimos que no existe en caso de error

def guardar_usuario(nombre, ci, contrasena):
    try:
        # Obtener la conexión
        conn = obtener_conexion()
        cursor = conn.cursor()

        # Consulta SQL para insertar los datos
        query = sql.SQL("INSERT INTO usuarios (nombre, ci, contrasena) VALUES (%s, %s, %s)")

        # Ejecutar la consulta
        cursor.execute(query, (nombre, ci, contrasena))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        cursor.close()
        conn.close()

        print("Usuario registrado correctamente en la base de datos.")
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")
      
        
def verificar_ingreso_usuario(ci, contrasena):
    try:
        # Obtener la conexión
        conn = obtener_conexion()
        cursor = conn.cursor()

        # Consulta SQL para verificar si el CI y la contraseña son correctos
        query = sql.SQL("SELECT 1 FROM usuarios WHERE ci = %s AND contrasena = %s")
        cursor.execute(query, (ci, contrasena))

        # Comprobar si se encontró algún registro
        existe = cursor.fetchone()  # Devuelve None si no encuentra ningún registro

        # Cerrar la conexión
        cursor.close()
        conn.close()

        if existe:
            return True  # El usuario existe y la contraseña es correcta
        else:
            return False  # CI o contraseña incorrectos
    except Exception as e:
        print(f"Error al verificar el ingreso del usuario: {e}")
        return False  # Asumimos que el ingreso es incorrecto en caso de error