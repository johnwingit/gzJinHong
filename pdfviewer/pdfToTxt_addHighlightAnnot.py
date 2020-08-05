import fitz
doc = fitz.open("../pdffile/YT4856.pdf")
page = doc[0]

text = "713060044"
text_instances = page.searchFor(text)
print(text_instances)
    ### HIGHLIGHT

for inst in text_instances:
    highlight = page.addHighlightAnnot(inst)


doc.save("../pdffile/test01.pdf", garbage=4, deflate=True, clean=True)