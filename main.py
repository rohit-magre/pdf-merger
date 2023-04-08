from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["1.pdf", "2.pdf", "3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()