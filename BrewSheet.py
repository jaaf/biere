# Python program to create
# a pdf file
 
 
from fpdf import FPDF
 
 
# save FPDF() class into a
# variable pdf
pdf = FPDF()
 
# Add a page
pdf.add_page()
 
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)
pdf.set_fill_color(255,255,0)
 
# create a cell
pdf.cell(200, 10, txt = "GeeksforGeeks",
         ln = 1, align = 'C')
 
# add another cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')
pdf.cell(0,70,'Salut les copains',ln=2,align="R",fill=True)
 
# save the pdf with name .pdf
print('printing')
pdf.output("GFG.pdf")  