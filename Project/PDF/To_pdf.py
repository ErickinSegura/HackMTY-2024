import pdfkit


html_file = 'ruta/a/tu/archivo.html'


path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'  # En Linux/Mac

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


pdf_output = 'ruta/de/salida/archivo_salida.pdf'
pdfkit.from_file(html_file, pdf_output, configuration=config)

print(f"PDF generado en: {pdf_output}")
