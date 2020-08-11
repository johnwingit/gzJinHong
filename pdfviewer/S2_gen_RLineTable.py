import fitz
from pdfviewer.Jinhong_tools import *
from pdfviewer.Parse_strtonum import *
#ls = Parse_strtonum.Parse_strtonum("ertew345555634sdfg45345645645664")
#将"x坐标", "y坐标", "材料型号编号","本公司编号","材料名称"写入文本
# to load database
# it the text Extracted from pdf file
def S2_RLineTable(path):
    filepath = "database/Db.txt"  # 读取数据库文本（本公司线号、原公司线号、型号）对应表
    jinl = Jinhong_tools(filepath)
    DBltable = jinl.loadlinetableDB()  # 线号型号对应表
    print(DBltable)
    dictDB_ltableNO = jinl.loadlinetableNODB()  # 本公司线号和原公司线号对应表
    print(dictDB_ltableNO)

    # To find the exact position of String 查找字符串的确切位置
    doc = fitz.open(path)
    page = doc[0]  # 打开pdf文档

    # Open a data txt file. 打开读取pdf的txt数据文件
    fileForR = open("pdffile/data.txt", "r")
    fileForW = open("LineTable/ReadLineTable.txt", "w")
    fileForW.write("%6s, %6s, %8s, %10s , %25s \n" % ("x坐标", "y坐标", "材料型号编号", "本公司编号", "材料名称"))
    line = fileForR.readline()  # 读每一行数据
    while line:
        # 后面跟 ',' 将忽略换行符
        count = 0
        text = ""
        ls = strtonum(line)  # 判断是否是材料型号编号
        for i in range(len(ls)):
            print(ls[i])
            text = ls[i]
            lineno = text.strip()
            text_instances = page.searchFor(text)
            # print(text_instances)
            x = text_instances[0][0]  # 读横坐标
            y = text_instances[0][1]  # 读纵坐标
            s4 = dictDB_ltableNO[lineno]  # 本公司线号和原公司线号对应表
            s5 = DBltable[lineno]  # 线号型号对应表
            print(x, y, s4, s5)
            fileForW.write("%6d, %8d, %14s,%16s,%26s \n" % (x, y, lineno, s4, s5))

        line = fileForR.readline()

    fileForW.close()
    fileForR.close()
