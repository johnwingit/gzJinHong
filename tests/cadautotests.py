# -*- coding: UTF-8 -*-
from pyautocad import Autocad, APoint

# 这个true表示没有文件则打开一个，CAD有弹窗时会打开或者创建失败
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)


for text in acad.iter_objects('Text'):
    if text.TextString.find("YT4")>=0:
        print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
#text.InsertionPoint = APoint(text.InsertionPoint) + dp

