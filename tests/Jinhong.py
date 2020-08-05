

class Jinhong(object):

    def __init__(self,file):
        self.file = file
        self.dictdb ={}

    #@staticmethod
    def loadlinetableDB(self):
        f = open(self.file, "r",encoding='UTF-8')
        line = f.readline()
        while line:
            ls_str = line.split(',', 2);
            #print(line)
            #print( ls_str)
            self.dictdb[ls_str[0].strip()] = ls_str[1].strip()
            line = f.readline()
        f.close()
        return self.dictdb

    #@staticmethod
    def loadlinetableNODB(self):
        f = open(self.file, "r",encoding='UTF-8')
        line = f.readline()
        while line:
            ls_str = line.split(',', 2);
            self.dictdb[ls_str[0].strip()] = ls_str[2].strip()
            line = f.readline()
        f.close()
        return self.dictdb


# 主程序
def Main():
    # 创建士兵
    filepath = "../database/Db.txt"
    jinl = Jinhong(filepath)
    dictDB = jinl.loadlinetableDB()
    print(dictDB)
    dictDB = jinl.loadlinetableNODB()
    print(dictDB)


if __name__ == '__main__':
    Main()
