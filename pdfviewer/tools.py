def loadlinetableDB(file):
    dictdb = {}
    f = open(file, "r",encoding='UTF-8')
    line = f.readline()
    while line:
        ls_str = line.split(',', 2);
        #print(line)
        #print( ls_str)
        dictdb[ls_str[0].strip()] = ls_str[1].strip()
        line = f.readline()
    f.close()
    return dictdb

def loadlinetableNODB(file):
    dictdb = {}
    f = open(file, "r",encoding='UTF-8')
    line = f.readline()
    while line:
        ls_str = line.split(',', 2);
        dictdb[ls_str[0].strip()] = ls_str[2].strip()
        line = f.readline()
    f.close()
    return dictdb



filepath = "../database/Db.txt"
dictDB = loadlinetableDB(filepath)
print(dictDB)
dictDB = loadlinetableNODB(filepath)
print(dictDB)