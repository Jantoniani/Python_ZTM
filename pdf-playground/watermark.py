import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('super(watermark).pdf', 'wb') as file:
        output.write(file)





# pdf_file = 'super.pdf'
# watermark = 'wtr.pdf'
# final_pdf = 'super(watermark).pdf'
#
# input_file = open(pdf_file, 'rb')
# input_pdf = PyPDF2.PdfFileReader(input_file)
#
# watermark_file = open(watermark, 'rb')
# watermark_pdf = PyPDF2.PdfFileReader(watermark)
#
# pdf_page = input_pdf.getPage(0)
#
# watermark_page = watermark_pdf.getPage(0)
#
# pdf_page.mergePage(watermark_page)
#
# output = PyPDF2.PdfFileWriter()
#
# output.addPage(pdf_page)
#
# final_pdf = open(final_pdf, 'wb')
# output.write(final_pdf)
