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
#读取PDF文件的内容及位置
# Open a PDF file.
fp = open('../pdffile/YT4856.pdf', 'rb')

# Create a PDF parser object associated with the file object.创建一个PDF分析程序与文件对象关联
parser = PDFParser(fp)

# Create a PDF document object that stores the document structure.创建一个存储文档结构的PDF文档对象
# Password for initialization as 2nd parameter 初始化密码作为第二个参数
document = PDFDocument(parser)

# Check if the document allows text extraction. If not, abort.检查文档是否允许文字提取，如果不，退出
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.创建一个存储共享资源的PDF资源管理器对象
rsrcmgr = PDFResourceManager()

# Create a PDF device object.创建一个PDF设备对象
device = PDFDevice(rsrcmgr)

# BEGIN LAYOUT ANALYSIS 开始布局分析
# Set parameters for analysis.f 设置分析参数
laparams = LAParams()

# Create a PDF page aggregator object. 创建PDF页面聚合器对象
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object. 创建一个PDF解释器对象
interpreter = PDFPageInterpreter(rsrcmgr, device)

def parse_obj(lt_objs,f):

    # loop over the object list 遍历对象列表
    for obj in lt_objs:

        # if it's a textbox, print text and location 如果是文本框，打印文字和位置
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            print ("%6d, %6d, %s" % (obj.bbox[0], obj.bbox[1], obj.get_text()))
            f.write("%6d, %6d, %s \n" % (obj.bbox[0], obj.bbox[1], obj.get_text()))
        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs,f)

# loop over all pages in the document 遍历文档中的所有页面
for page in PDFPage.create_pages(document):

    # read the page into a layout object 将页面读入布局对象
    interpreter.process_page(page)
    layout = device.get_result()
    # store all text in a file 将所有内容存入文件
    f = open("../pdffile/data1.txt", "w")
    #f.write("Woops! I have deleted the content!")

    # extract text from this object 从该对象中提取文本
    parse_obj(layout._objs,f)
    f.close()