from docx import Document
from docx.shared import Inches
from datetime import date

titulo=input("Introduce el título del documento: ")
guardar=input("¿Con qué nombre lo quieres guardar? ")
document = Document()
document.add_heading(titulo, 0)
document.add_paragraph("Ruiz Tovar Edgar")
document.add_paragraph("248926")
document.add_paragraph(str(date.today()))
document.save('C://Users//Edgar//Documents//Edgar//Matemáticas Aplicadas//Sexto Semestre//Economia//%s.docx'%(guardar))  