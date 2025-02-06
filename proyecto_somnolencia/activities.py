# activities.py
import tkinter as tk

class ActivitiesWindow:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("Actividades")
        self.top.geometry("1920x1080")

        tk.Label(self.top, text="Selecciona una actividad:", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.top, text="Actividad 1", command=self.actividad1, width=20).pack(pady=5)
        tk.Button(self.top, text="Actividad 2", command=self.actividad2, width=20).pack(pady=5)
        tk.Button(self.top, text="Cerrar", command=self.top.destroy, width=20).pack(pady=20)

    def actividad1(self):
        # Placeholder para la actividad 1
        tk.Label(self.top, text="Actividad 1 seleccionada").pack()

    def actividad2(self):
        # Placeholder para la actividad 2
        tk.Label(self.top, text="Actividad 2 seleccionada").pack()
