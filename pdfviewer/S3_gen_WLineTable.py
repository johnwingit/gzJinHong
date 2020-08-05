import fitz

#记录需要标记的本公司线号坐标及内容
# Open a data txt file.
def S3_gen_WLineTable():
    fileForR = open("LineTable/ReadLineTable.txt", "r")  # 打开步骤二提取的（x坐标", "y坐标", "材料型号编号","本公司编号","材料名称"）文件
    fileForW = open("LineTable/WriteLineTable.txt", "w")
    fileForW.write("%6s, %6s, %s\n" % ("新x坐标", "新y坐标", "本公司编号"))
    line = fileForR.readline()  # abandon the first line. 忽略第一行
    line = fileForR.readline()  # 调用文件的 readline()方法
    while line:
        # 后面跟 ',' 将忽略换行符
        ls_str = line.split(',', 5);  # the string all string.
        nx_str = str(int(ls_str[0]) - 90)
        fileForW.write("%6s," % (nx_str))
        ny_str = ls_str[1]
        fileForW.write("%6s," % (ny_str))
        nno = ls_str[3]  # 本公司编号
        fileForW.write("%6s" % (nno))
        fileForW.write("\n")
        line = fileForR.readline()

    fileForW.close()
    fileForR.close()
