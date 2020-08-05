# coding=utf-8
import sys

class Jinhong_tools(object):

    def __init__(self,file):
        self.file = file
        self.dictdb ={}
        self.dictdbNO ={}

    #线号型号对应表
    def loadlinetableDB(self):
        f = open(self.file, "r",encoding='UTF-8')
        line = f.readline()
        while line:
            ls_str = line.split(',', 2);
            #print(line)
            #print( ls_str)
            self.dictdb[ls_str[0].strip()] = ls_str[2].strip()
            line = f.readline()
        f.close()
        return self.dictdb

    #本公司线号和原公司线号对应表
    def loadlinetableNODB(self):
        f = open(self.file, "r",encoding='UTF-8')
        line = f.readline()
        while line:
            ls_str = line.split(',', 2);
            self.dictdbNO[ls_str[0].strip()] = ls_str[1].strip()
            line = f.readline()
        f.close()
        return self.dictdbNO


# 主程序
def Main():
    # 创建
    filepath = "../database/Db.txt"
    jinl = Jinhong_tools(filepath)
    dictDB_ltable = jinl.loadlinetableDB()
    print(dictDB_ltable)
    dictDB_ltable = jinl.loadlinetableNODB()
    print(dictDB_ltable)


if __name__ == '__main__':
    Main()
