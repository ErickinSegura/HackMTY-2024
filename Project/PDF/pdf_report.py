import os
import sys

# Using ReportLab to generate PDFs
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# using pillow to get image dimensions
from PIL import Image
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='noesmisaesunbot@gmail.com',
    to_emails='roccolpz04@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get(''))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    print("Correo enviado")
except Exception as e:
    print(e.message)

class Escritor:
    def __init__(self, nombre_pregunta):
        self.ref_nombre_pdf = f"Reporte--{nombre_pregunta}--.pdf"
        self.c_writer = canvas.Canvas(self.ref_nombre_pdf, pagesize=letter)

    def escribe_pregunta(self, pregunta, x, y, max_ancho=500):

    
        self.c_writer.setFont("Helvetica", 12)
        self.c_writer.setFillColorRGB(0, 0, 0)
        
        
        lineas = self.divide_texto(pregunta, max_ancho)
        
        
        for linea in lineas:
            self.c_writer.drawString(x, y, linea)
            y -= 15  # Espacio entre líneas
        

    def divide_texto(self, texto, max_ancho):

        """Divide el texto en líneas basadas en el ancho máximo disponible."""

        palabras = texto.split(' ')
        lineas = []
        linea_actual = ""

        for palabra in palabras:
            if self.c_writer.stringWidth(linea_actual + palabra) < max_ancho:
                linea_actual += palabra + " "
            else:
                lineas.append(linea_actual.strip())
                linea_actual = palabra + " "

        if linea_actual:
            lineas.append(linea_actual.strip())

        return lineas

    def insertar_imagen(self, ruta_imagen, x, y, ancho=None, alto=None):

        if ancho and alto:
            self.c_writer.drawImage(ruta_imagen, x, y, width=ancho, height=alto)
        else:
            self.c_writer.drawImage(ruta_imagen, x, y)

    def guarda_pdf(self):

        self.c_writer.save()
        print(f"PDF guardado como {self.ref_nombre_pdf}")
    
    def generar_pdf(self, pregunta, ruta_imagen):
        
        padding_left_text = 10
        padding_top_text = 10
        height = 792  # Altura de la página (letter)

        # Tomar las dimensiones del ancho y alto de la imagen
        with Image.open(ruta_imagen) as img:
            ancho_imagen = img.width
            alto_imagen = img.height

        # Insertar la imagen en la esquina superior izquierda
        self.insertar_imagen(ruta_imagen, 0, (height-alto_imagen), ancho=ancho_imagen, alto=alto_imagen)

        # Coordenadas para el texto, debajo de la imagen
        x_texto = ancho_imagen + padding_left_text
        y_texto = height - padding_top_text  

        # Escribir la pregunta debajo de la imagen y ajustarla a la línea si es necesario
        self.escribe_pregunta(pregunta, x_texto, y_texto)

        # Guardar el PDF
        self.guarda_pdf()

# Pregunta por el usuario y nombre del PDF
pregunta_por_usuario = "¿Cuál es la capital de Francia?"
nombre_pdf = "conimagentexto3"
try_clase = Escritor(nombre_pdf)

# Ruta de la imagen
ruta_imagen = os.path.abspath("bici.png")

# Generar el PDF con la imagen y la pregunta
try_clase.generar_pdf(pregunta_por_usuario, ruta_imagen)
