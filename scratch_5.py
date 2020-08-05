def loadlinetableDB(file):
    dictdb = {}
    f = open(file, "r")
    line = f.readline()
    while line:
        ls_str = line.split(',', 1);
        dictdb[ls_str[0]] = ls_str[1]
        line = f.readline()
    f.close()
    return dictdb



filepath = "../database/Db.txt"
dictDB = loadlinetableDB(filepath)
print(dictDB)
