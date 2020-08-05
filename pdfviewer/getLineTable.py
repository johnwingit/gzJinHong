import fitz
from Jinhong import *

def isdigit(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False
# 后面跟 ',' 将忽略换行符


doc = fitz.open("../pdffile/YT4856.pdf")
page = doc[0]

    ### HIGHLIGHT
# Open a PDF file.
fileForR = open("../pdffile/data.txt", "r")
fileForW = open("../LineTable/ReadLineTable.txt", "w")
fileForW.write("%6s, %6s, %s, %s , %s \n" % ("x坐标", "y坐标", "材料型号编号","本公司编号","材料"))
line = fileForR.readline()               # 调用文件的 readline()方法
while line:
    # 后面跟 ',' 将忽略换行符
    count =0
    text =""
    for ch in line:
        if isdigit(ch):
            text = text + ch
            #print(ch)
            count=count+1
        else:
            break
    if count> 7:
        print(line)
        print(text)
        text_instances = page.searchFor(text)
        #print(text_instances)
        x=text_instances[0][0]
        y=text_instances[0][1]
        fileForW.write("%6d, %6d, %s \n" % (x, y, text))
    line = fileForR.readline()

fileForW.close()
fileForR.close()