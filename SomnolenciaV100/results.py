import tkinter as tk
from tkinter import font
import psycopg2

class ResultsWindow:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("Resultados")
        self.top.geometry("700x650")
        self.top.configure(bg="#e0f7fa")

        # Fuentes
        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.label_font = font.Font(family="Arial", size=12)

        # Frame para el Resultado Monitoreo de Actividades
        self.frame1 = tk.Frame(self.top, bg="#ffffff", padx=20, pady=10, relief="raised", bd=3)
        self.frame1.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.35)

        tk.Label(self.frame1, text="Resultado Monitoreo de Actividades", font=self.title_font, bg="#ffffff", fg="#009688").pack(pady=5)

        self.resultados_frame1 = tk.Frame(self.frame1, bg="#64b5f6", padx=10, pady=10, relief="raised", bd=2)
        self.resultados_frame1.pack(pady=10, fill="x")

        self.tiempo_ojos_label = tk.Label(self.resultados_frame1, text="Tiempo de ojo cerrado (s): --", font=self.label_font, bg="#64b5f6")
        self.tiempo_ojos_label.pack(pady=5)
        self.parpadeos_label = tk.Label(self.resultados_frame1, text="Parpadeos detectados: --", font=self.label_font, bg="#64b5f6")
        self.parpadeos_label.pack(pady=5)
        self.porcentaje_label = tk.Label(self.resultados_frame1, text="Porcentaje de ojo cerrado (%): --", font=self.label_font, bg="#64b5f6")
        self.porcentaje_label.pack(pady=5)

        # Conclusión actividades
        self.conclusion_actividades_label = tk.Label(self.resultados_frame1, text="Conclusión actividades: --", font=self.label_font, bg="#64b5f6")
        self.conclusion_actividades_label.pack(pady=5)

        # Frame para el Resultado Test de CPT
        self.frame2 = tk.Frame(self.top, bg="#ffffff", padx=20, pady=10, relief="raised", bd=3)
        self.frame2.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.35)

        tk.Label(self.frame2, text="Resultado Test de CPT", font=self.title_font, bg="#ffffff", fg="#009688").pack(pady=5)

        self.resultados_frame2 = tk.Frame(self.frame2, bg="#81c784", padx=10, pady=10, relief="raised", bd=2)
        self.resultados_frame2.pack(pady=10, fill="x")

        self.aciertos_label = tk.Label(self.resultados_frame2, text="Total de aciertos: --", font=self.label_font, bg="#81c784")
        self.aciertos_label.pack(pady=5)
        self.errores_label = tk.Label(self.resultados_frame2, text="Total de Erróneos: --", font=self.label_font, bg="#81c784")
        self.errores_label.pack(pady=5)
        self.promedio_label = tk.Label(self.resultados_frame2, text="Total de Promedio: -- segundos", font=self.label_font, bg="#81c784")
        self.promedio_label.pack(pady=5)

        # Conclusión test
        self.conclusion_test_label = tk.Label(self.resultados_frame2, text="Conclusión test: --", font=self.label_font, bg="#81c784")
        self.conclusion_test_label.pack(pady=5)

        # Frame para la Conclusión Final
        self.frame3 = tk.Frame(self.top, bg="#ffffff", padx=20, pady=10, relief="raised", bd=3)
        self.frame3.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.1)

        self.conclusion_final_label = tk.Label(self.frame3, text="", font=self.title_font, bg="#ffeb3b")
        self.conclusion_final_label.pack(pady=10, fill="x")

        # Botón de Cerrar centrado
        # Establecemos el fondo del botón igual que el de la ventana
        self.boton_cerrar = tk.Button(self.top, text="Cerrar", command=self.top.destroy, width=20, font=("Helvetica", 12), bg="white", fg="black", relief="solid", bd=2)
        self.boton_cerrar.place(relx=0.5, rely=0.9, anchor="center")

        self.actualizar_interfaz()

    def obtener_datos(self):
        try:
            conn = psycopg2.connect(
                host="localhost",  # o la dirección de tu servidor
                dbname="Interfaces",  # Nombre de la base de datos
                user="postgres",  # Usuario
                password="1234"  # Contraseña
            )
            cur = conn.cursor()
            cur.execute("SELECT Tiempo_total_ojos_cerrados, Parpadeos_totales, Porcentaje_ojos_cerrados FROM Ractividades ORDER BY CI DESC LIMIT 1;")
            datos = cur.fetchone()
            conn.close()
            return datos if datos else (0, 0, 0.0)
        except Exception as e:
            print("Error en la base de datos:", e)
            return (0, 0, 0.0)

    def actualizar_interfaz(self):
        datos = self.obtener_datos()
        
        self.tiempo_ojos_label.config(text=f"Tiempo de ojo cerrado (s): {datos[0]}")
        self.parpadeos_label.config(text=f"Parpadeos detectados: {datos[1]}")
        self.porcentaje_label.config(text=f"Porcentaje de ojo cerrado (%): {datos[2]}")
        
        # Conclusión actividades
        if datos[2] < 80:
            self.conclusion_actividades_label.config(text="No se detecta somnolencia", bg="lightgreen")
        else:
            self.conclusion_actividades_label.config(text="Se detecta somnolencia", bg="red", fg="white")

        # Resultado Test de CPT
        self.aciertos_label.config(text="Total de aciertos: --")
        self.errores_label.config(text="Total de Erróneos: --")
        self.promedio_label.config(text="Total de Promedio: -- segundos")
        
        # Conclusión test
        if datos[2] < 80:
            self.conclusion_test_label.config(text="No se detecta somnolencia", bg="lightgreen")
        else:
            self.conclusion_test_label.config(text="Se detecta somnolencia", bg="red", fg="white")
        
        # Conclusión final
        if datos[2] < 80:
            self.conclusion_final_label.config(text="No se detecta somnolencia en los resultados generales", bg="lightgreen")
        else:
            self.conclusion_final_label.config(text="Se detecta somnolencia en los resultados generales", bg="red", fg="white")
