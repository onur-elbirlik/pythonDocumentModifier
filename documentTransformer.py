from docx import Document
from docx2pdf import convert
import sys
doc=Document('./'+sys.argv[1])
Dictionary = {sys.argv[2]: sys.argv[3]}
for i in Dictionary:
    for p in doc.paragraphs:
        if p.text.find(i)>=0:
            p.text=p.text.replace(i,Dictionary[i])
doc.save('./'+sys.argv[1])
convert(sys.argv[1], sys.argv[3] +'.pdf')
