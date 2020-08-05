import fitz


# Open a data txt file.
fileForR = open("../LineTable/ReadLineTable.txt", "r")
fileForW = open("../LineTable/WriteLineTable0601.txt", "w")#"x坐标", "y坐标", "材料型号编号","本公司编号","材料名称"
fileForW.write("%6s, %6s, %s, %s , %s , %s, %s  \n" % ("新x坐标", "新y坐标", "本公司编号", "x坐标", "y坐标", "材料型号编号", "材料名称"))
line = fileForR.readline()               # abandon the first line.
line = fileForR.readline()               # 调用文件的 readline()方法
while line:
    # 后面跟 ',' 将忽略换行符
    ls_str = line.split(',', 5); # the string all string.
    nx_str = str(int(ls_str[0]) - 20)
    fileForW.write("%6s," % (nx_str))
    ny_str = ls_str[1]
    fileForW.write("%6s," % (ny_str))
    nno = ls_str[3] #本公司编号
    fileForW.write("%6s" % (nno))
    fileForW.write("\n")
    line = fileForR.readline()

fileForW.close()
fileForR.close()