from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def crear_pdf_con_imagen():
    archivo_pdf = "mi_documento_con_imagen.pdf"
    c = canvas.Canvas(archivo_pdf, pagesize=letter)

    # Escribir texto
    c.drawString(100, 750, "Este es un PDF con una imagen")

    # Agregar una imagen
    c.drawImage("lectura.png", 100, 500, width=400, height=300)

    # Finalizar y guardar el archivo PDF
    c.save()

# Llamar a la función para generar el PDF con imagen
crear_pdf_con_imagen()
