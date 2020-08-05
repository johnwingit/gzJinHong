import fitz
from Jinhong_tools import *

def isdigit(x):
    try:
        x=int(x)
        return isinstance(x,int)
    except ValueError:
        return False

# to load database
# it the text Extracted from pdf file
filepath = "../database/Db.txt"
jinl = Jinhong_tools(filepath)
DBltable = jinl.loadlinetableDB()
print(DBltable)
dictDB_ltableNO = jinl.loadlinetableNODB()
print(dictDB_ltableNO)

# To find the exact position of String
doc = fitz.open("../pdffile/YT4856.pdf")
page = doc[0]

# Open a data txt file.
fileForR = open("../pdffile/data.txt", "r")
fileForW = open("../LineTable/ReadLineTable.txt", "w")
fileForW.write("%6s, %6s, %s, %s , %s \n" % ("x坐标", "y坐标", "材料型号编号","本公司编号","材料名称"))
line = fileForR.readline()
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
        lineno=text.strip()
        text_instances = page.searchFor(text)
        #print(text_instances)
        x=text_instances[0][0]
        y=text_instances[0][1]
        s4 = dictDB_ltableNO[lineno]
        s5=  DBltable[lineno]
        print(s4+s5)
        fileForW.write("%6d, %6d, %s,%s,%s \n" % (x, y, lineno, s4, s5))
    line = fileForR.readline()

fileForW.close()
fileForR.close()