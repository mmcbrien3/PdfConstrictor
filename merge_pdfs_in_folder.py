import os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

#INSERT FOLDER PATH HERE
fold = r"C:\Users\mmcbrien\Documents\Skewl\College\Skewl Terms\FALL 2019\Comm Netwoks\notes"
if os.path.isfile(os.path.join(fold, "compiled_notes.pdf")):
    os.remove(os.path.join(fold, "compiled_notes.pdf"))
outfile = os.path.join(fold, "compiled_notes.pdf")
pdfs = os.listdir(fold)
pdfs.sort()
pdfs = [os.path.join(fold, f) for f in pdfs if f.endswith((".pdf"))]
input_streams = []
for pdf in pdfs:
    input_streams.append(open(pdf, 'rb'))
writer = PdfFileWriter()

for reader in map(PdfFileReader, input_streams):
    for n in range(reader.getNumPages()):
        writer.addPage(reader.getPage(n))

fhandle = open(outfile, "wb")
writer.write(fhandle)
fhandle.close()
for f in input_streams:
    f.close()
    
