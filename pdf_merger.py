from PyPDF2 import PdfMerger

pdfs = [r'RELEVE NIVEAU 1.pdf', r'RELEVE NIVEAU 2.pdf', r'RELEVE NIVEAU 3.pdf', r'RELEVE NIVEAU 4.pdf', r'RELEVE NIVEAU 5.pdf']
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("RELEVE_1-5.pdf")
merger.close()