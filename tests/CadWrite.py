#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyautocad import Autocad, APoint


acad = Autocad()
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

p1 = APoint(0, 0)
p2 = APoint(50, 25)
#for i in range(5):
    #text = acad.model.AddText('Hikjjkk %s!' % i, p1, 2.5)

for text in acad.iter_objects('Text'):
    if text.TextString.find("YT4")>=0:
        print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
        rec=text.InsertionPoint
        x = float(rec[0])+float(100.0)
        p = APoint(x, float(rec[1]))
        str = "Jin hong 56824556"
        text = acad.model.AddText('%s!' % str, p, 2.5)
        clr = acad.Application.GetInterfaceObject("AutoCAD.AcCmColor.19")
        clr.SetRGB(255, 0, 0)  # 创建红色
        text.TrueColor = clr  # 指定颜色
