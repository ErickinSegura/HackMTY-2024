# wkhtmltopdf
import pdfkit

# Ruta al archivo HTML que quieres convertir
html_file = '/workspaces/HackMTY-2024/Project/WEB/index.html'

# Configuración para wkhtmltopdf (especifica la ruta correcta en tu sistema)
path_wkhtmltopdf = '/usr/local/python/3.12.1/lib/python3.12/site-packages (0.2)'  # En Linux/Mac
# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # En Windows
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Generar PDF a partir del archivo HTML
pdf_output = '/workspaces/HackMTY-2024/Project/PDF/archivo_salida.pdf'
pdfkit.from_file(html_file, pdf_output, configuration=config)

print(f"PDF generado en: {pdf_output}")
