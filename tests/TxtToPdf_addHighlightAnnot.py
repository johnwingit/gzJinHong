import fitz
doc = fitz.open("../pdffile/YT4.pdf")
page = doc[0]

red = (1, 0, 0)
Lavender = (230,230,250)
gold = (1, 1, 0)
green = (0, 1, 0)

text = "713060057"
text_instances = page.searchFor(text)
print(text_instances)
    ### HIGHLIGHT



# text for annotation
x0 =500
y0 = 360

ta = "we here"
ra = fitz.Rect(x0, y0, x0+20, y0+20)
anno = page.addFreetextAnnot(ra, ta, fontsize=7, text_color=red, fill_color=Lavender)


doc.save("../pdffile/test01.pdf", garbage=4, deflate=True, clean=True)