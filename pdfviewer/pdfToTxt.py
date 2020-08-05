from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer
import fitz

# Open a PDF file.
fp = open('../pdffile/YT4856.pdf', 'rb')

# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.
# Password for initialization as 2nd parameter
document = PDFDocument(parser)

# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Create a PDF device object.
device = PDFDevice(rsrcmgr)

# BEGIN LAYOUT ANALYSIS
# Set parameters for analysis.f有
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)

def parse_obj(lt_objs,f):

    # loop over the object list
    for obj in lt_objs:

        # if it's a textbox, print text and location
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            print ("%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text()))
            f.write("%6d, %6d, %s \n" % (obj.bbox[0], obj.bbox[1], obj.get_text()))
        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs,f)

# loop over all pages in the document
for page in PDFPage.create_pages(document):

    # read the page into a layout object
    interpreter.process_page(page)
    layout = device.get_result()
    f = open("../pdffile/data.txt", "w")
    #f.write("Woops! I have deleted the content!")

    # extract text from this object
    parse_obj(layout._objs,f)
    f.close()


    ### READ IN PDF

    doc = fitz.open("../pdffile/YT4856.pdf")
    page = doc[0]

    text = "713060044"
    text_instances = page.searchFor(text)
    print(text_instances)
    ### HIGHLIGHT

    for inst in text_instances:
        highlight = page.addHighlightAnnot(inst)

    ### OUTPUT

    doc.save("../pdffile/YT4856output0601.pdf", garbage=4, deflate=True, clean=True)