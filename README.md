This code gets a file name and two words from user modify it and turns it to a PDF file. It is for a specific use but can be modified for different purposes.
1- It will search firstWordArgument in the document and replace all with the secondWordArgument.
2- It will creates a PDF file with the name of secondWordArgument.pdf

Requirements

Python 3

python-docx (pip3 install python-docx) github.com/AlJohri/docx2pdf

docx2pdf (pip3 install docx2pdf) python-docx.readthedocs.org/en/latest/


Instructions

python3 documentTransformer.py nameOfDocument.docx firstWordArgument secondWordArgument
