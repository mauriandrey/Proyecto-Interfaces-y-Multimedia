# results.py
import tkinter as tk

class ResultsWindow:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("Resultados")
        self.top.geometry("400x300")

        tk.Label(self.top, text="Resultados del monitoreo y test de somnolencia", font=("Arial", 14)).pack(pady=10)
        # Ejemplo de resultados (se deben reemplazar con los datos reales)
        tk.Label(self.top, text="Tiempo de monitoreo: 00:10:25").pack(pady=5)
        tk.Label(self.top, text="Eventos de somnolencia detectados: 3").pack(pady=5)

        tk.Button(self.top, text="Cerrar", command=self.top.destroy, width=20).pack(pady=20)
