

import PyPDF2

def compress_pdf(input_file, output_file):
    input_stream = open(input_file, 'rb')
    pdf_reader = PyPDF2.PdfReader(input_stream)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])
    
    output_stream = open(output_file, 'wb')
    pdf_writer.write(output_stream)
    
    input_stream.close()
    output_stream.close()

compress_pdf('my-CV.pdf', 'Cv-c.pdf')
