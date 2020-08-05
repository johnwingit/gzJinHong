# -*- coding: UTF-8 -*-
from pyautocad import Autocad, APoint

# 这个true表示没有文件则打开一个，CAD有弹窗时会打开或者创建失败
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

p1 = APoint(10, 10)  # 点的位置坐标
p2 = APoint(50, 45)
for i in range(50):
    text = acad.model.AddText('大好 %s!' % i, p1, 1.5)  # 添加文本
acad.model.AddLine(p1, p2)  # 添加线
acad.model.AddCircle(p1, 10)  # 添加圆
p1.y += 10

dp = APoint(10, 0)
# 打印点信息
for text in acad.iter_objects('Text'):
    print('text: %s at: %s' % (text.TextString, text.InsertionPoint))
text.InsertionPoint = APoint(text.InsertionPoint) + dp

# 打印圆，线名称
for obj in acad.iter_objects(['Circle', 'Line']):
    print(obj.ObjectName)