from pdf2docx import Converter

pdf_file = 'output.pdf'
docx_file = '123.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()