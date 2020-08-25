#pdf to text  converter
import PyPDF2
pdfileobg=open("1.pdf.pdf",'rb')
pdfreader=PyPDF2.PdfFileReader(pdfileobg)
x=pdfreader.numPages          #to  read number of pages
pageobj=pdfreader.getPage(x-1)  #counting starts from 0
text=pageobj.extractText()
file=open(r"C:\Users\HOME\PycharmProjects\tkint\2.txt","a")
file.writelines(text)
file.close()
