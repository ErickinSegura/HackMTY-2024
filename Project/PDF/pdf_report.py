from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crear el archivo PDF
nombre_pdf = "mi_documento.pdf"
c = canvas.Canvas(nombre_pdf, pagesize=letter)

# Escribir texto en el PDF
c.drawString(100, 750, "Hola, este es mi primer PDF generado en Python!")

# Guardar el PDF
c.save()

print(f"PDF guardado como {nombre_pdf}")
