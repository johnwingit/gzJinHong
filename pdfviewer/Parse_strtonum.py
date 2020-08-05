# coding=utf-8
import sys

def Parse_strtonum(pastr):  #判断是否是材料型号编号
    str = pastr+"a"
    count = 0
    length = 7 #定义字符串中>=7个数字的序列输出
    temp = []
    dig = []
    for i in range(str.__len__()):
        if (str[i] >= '0' and str[i] <= '9'):
            # 数字加一
            count += 1
            temp.append(str[i])  #append在列表末尾添加新的对象
        else:
            if count >= length:
                # 数字串大于之前的
                length = count
                count = 0
                str1 = ''.join(temp)
                dig.append(str1)
                temp = []
            else:
                # 数字串较短则清空
                temp = []
                count = 0
        # 结果输出
    return dig

