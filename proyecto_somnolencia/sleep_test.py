import tkinter as tk
import time
import random
from threading import Thread
import psycopg2

def obtener_conexion():
    conn = psycopg2.connect(
        host="localhost",  # o la dirección de tu servidor
        dbname="Interfaces",  # Nombre de la base de datos
        user="postgres",  # Usuario
        password="admin123"  # Contraseña Version Stalin: 1234
    )
    return conn

class CPTTestWindow:
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Continuous Performance Test (CPT)")
        self.top.attributes("-fullscreen", True)
        self.top.configure(bg="black")
        
        self.container = tk.Frame(self.top, bg="black")
        self.container.pack(expand=True)
        
        self.label = tk.Label(self.container, text="Presiona la barra espaciadora cuando veas la letra 'X'", font=("Arial", 16), fg="white", bg="black")
        self.label.pack(pady=20)
        
        self.stimulus_label = tk.Label(self.container, text="", font=("Arial", 100), fg="white", bg="black")
        self.stimulus_label.pack(pady=20)
        
        self.start_button = tk.Button(self.container, text="Iniciar Test", command=self.start_test, font=("Arial", 14), bg="green", fg="white", activebackground="white", activeforeground="black")
        self.start_button.pack(pady=20)
        
        self.end_button = tk.Button(self.container, text="Finalizar Test", command=self.close_window, font=("Arial", 14), bg="#80DAEB", fg="black")
        self.end_button.pack(pady=20)
        self.end_button.pack_forget()  # Ocultar el botón al inicio
        
        self.top.bind("<space>", self.record_response)
        
        self.running = False
        self.responses = []
        self.stimulus_time = None

    def start_test(self):
        self.start_button.pack_forget()  # Ocultar el botón al iniciar el test
        self.running = True
        self.responses.clear()
        
        self.test_thread = Thread(target=self.run_test)
        self.test_thread.start()
    
    def run_test(self):
        start_time = time.time()
        duration = 3  # 3 minutos 180
        
        while time.time() - start_time < duration:
            letter = random.choice(["X", "A", "B", "C", "D"])
            self.stimulus_time = time.time()
            self.stimulus_label.config(text=letter)
            time.sleep(random.uniform(1, 3))  # Intervalo variable entre estímulos
        
        self.running = False
        self.stimulus_label.config(text="Fin del test")
        self.show_results()
    
    def record_response(self, event):
        if self.running and self.stimulus_label.cget("text") == "X":
            reaction_time = time.time() - self.stimulus_time
            self.responses.append(reaction_time)
    
    def show_results(self):
        avg_reaction_time = sum(self.responses) / len(self.responses) if self.responses else 0
        result_text = f"Tiempo de reacción promedio: {avg_reaction_time:.3f} s"
        tk.Label(self.container, text=result_text, font=("Arial", 14), fg="white", bg="black").pack(pady=10)
        self.save_results(avg_reaction_time)
        self.end_button.pack(pady=20)  # Mostrar el botón al finalizar el test
    
    def save_results(self, avg_reaction_time):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS tiempo_reaccion FLOAT;")
        cursor.execute("UPDATE usuarios SET tiempo_reaccion = %s WHERE ci = %s;", (avg_reaction_time, "12345678"))  # Ajustar con CI real
        conn.commit()
        cursor.close()
        conn.close()
    
    def close_window(self):
        self.top.destroy()

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    CPTTestWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
