# coding=utf-8
import sys
import fitz

def S4_linetableToPdf(path):
    doc = fitz.open(path)  # 打开PDF源文件
    page = doc[0]

    # 颜色
    red = (1, 0, 0)
    MediumBlue = (0, 0, 205)
    Lavender = (230, 230, 250)
    gold = (1, 1, 0)
    green = (0, 1, 0)

    # Open a data txt file.
    fileForR = open("LineTable/WriteLineTable.txt", "r")  # 打开("%6s, %6s, %s\n" % ("新x坐标", "新y坐标", "本公司编号"))文本
    line = fileForR.readline()  # abandon the first line. 忽略第一行
    line = fileForR.readline()  # 调用文件的 readline()方法

    while line:
        # 后面跟 ',' 将忽略换行符
        ls_str = line.split(',', 3);  # the string all string.

        x0 = int(ls_str[0])
        y0 = int(ls_str[1])
        txt = ls_str[2]
        ra = fitz.Rect(x0, y0 + 3, x0 + 60, y0 + 10)  # 绘制一个矩形
        anno = page.addFreetextAnnot(ra, txt, fontsize=6, text_color=red, fill_color=Lavender)  # 在PDF上增加注释
        line = fileForR.readline()

    fileForR.close()
    doc.save("pdffile/YT4_produce01.pdf", garbage=4, deflate=True, clean=True)
