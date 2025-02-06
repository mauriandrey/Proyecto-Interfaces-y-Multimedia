import tkinter as tk
from tkinter import messagebox
import cv2
import mediapipe as mp
from PIL import Image, ImageTk

from activities import ActivitiesWindow
from sleep_test import CPTTestWindow
from results import ResultsWindow
from drowsiness_monitor import DrowsinessMonitor

class MainInterface:
    def __init__(self, root=None):
        # Si se pasa un root, lo usamos; de lo contrario, creamos uno nuevo (aunque lo ideal es pasarlo)
        self.root = root if root is not None else tk.Tk()
        self.root.title("Sistema de Monitoreo de Somnolencia")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")

        self.drowsiness_monitor = DrowsinessMonitor(ear_threshold=0.25)

        # Panel Izquierdo - Menú
        self.left_frame = tk.Frame(self.root, width=300, bg="#2c2c2c")
        self.left_frame.grid(row=0, column=0, sticky="ns")

        button_style = {"width": 20, "height": 2, "bg": "#4caf50", "fg": "white", "bd": 0,
                        "font": ("Arial", 12, "bold")}
        tk.Button(self.left_frame, text="Actividades", command=self.open_activities, **button_style).pack(pady=10, padx=10)
        tk.Button(self.left_frame, text="Test de Somnolencia", command=self.open_sleep_test, **button_style).pack(pady=10, padx=10)
        tk.Button(self.left_frame, text="Resultados", command=self.open_results, **button_style).pack(pady=10, padx=10)
        tk.Button(self.left_frame, text="Salir", command=self.root.quit, **button_style).pack(pady=10, padx=10)

        # Panel Derecho - Video y Control
        self.right_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.video_container = tk.Frame(self.right_frame, bg="black", highlightthickness=5, highlightbackground="red")
        self.video_container.pack(expand=True, fill="both", padx=20, pady=20)

        self.video_label = tk.Label(self.video_container, bg="black")
        self.video_label.pack(expand=True, fill="both", padx=5, pady=5)

        self.control_frame = tk.Frame(self.right_frame, bg="#1e1e1e")
        self.control_frame.pack(side="bottom", pady=10)

        self.cam_button = tk.Button(self.control_frame, text="Iniciar Cámara", command=self.toggle_camera, **button_style)
        self.cam_button.pack()

        self.cap = None
        self.running = False
        self.after_id = None  # Para almacenar el id del callback
        self.imgtk = None  # Referencia a la imagen

        self.mp_face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        self.mp_drawing = mp.solutions.drawing_utils

    def open_activities(self):
        ActivitiesWindow(self.root)

    def open_sleep_test(self):
        CPTTestWindow(self.root)

    def open_results(self):
        ResultsWindow(self.root)

    def toggle_camera(self):
        if self.running:
            # Apagar la cámara
            self.running = False
            self.cam_button.config(text="Iniciar Cámara", bg="#4caf50")
            self.video_container.config(highlightbackground="red")
            if self.after_id is not None:
                try:
                    self.video_label.after_cancel(self.after_id)
                except Exception as e:
                    print("Error cancelando callback:", e)
                self.after_id = None
            if self.cap and self.cap.isOpened():
                self.cap.release()
                self.cap = None
            if self.video_label.winfo_exists():
                self.video_label.config(image="")  # Limpiar la imagen
            self.imgtk = None
        else:
            # Encender la cámara
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "No se pudo abrir la cámara")
                return
            self.running = True
            self.cam_button.config(text="Apagar Cámara", bg="#d32f2f")
            self.video_container.config(highlightbackground="green")
            self.process_video()  # Inicia el loop de procesamiento

    def process_video(self):
        # Verificar que la cámara esté activa y el widget exista
        if not self.running or self.cap is None or not self.video_label.winfo_exists():
            return

        ret, frame = self.cap.read()
        if ret:
            # Procesar la imagen para mostrarla
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.mp_face_mesh.process(frame_rgb)
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    frame, ear, perclos = self.drowsiness_monitor.update(
                        frame, face_landmarks, frame.shape[1], frame.shape[0]
                    )
                    self.mp_drawing.draw_landmarks(
                        frame_rgb,
                        face_landmarks,
                        mp.solutions.face_mesh.FACEMESH_CONTOURS
                    )
            # Convertir nuevamente la imagen para mostrarla
            frame_final = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_final)
            self.imgtk = ImageTk.PhotoImage(image=img)
            try:
                if self.video_label.winfo_exists():
                    self.video_label.configure(image=self.imgtk)
                    # Almacenar la imagen en el widget para mantener la referencia
                    self.video_label.image = self.imgtk
            except tk.TclError as e:
                print("Error actualizando la imagen:", e)

        # Programar la siguiente actualización solo si la cámara sigue encendida
        if self.running and self.video_label.winfo_exists():
            self.after_id = self.video_label.after(10, self.process_video)
        else:
            if self.cap:
                self.cap.release()
                self.cap = None

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    interface = MainInterface()
    interface.run()
