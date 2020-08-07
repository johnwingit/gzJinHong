from tkinter import Tk
from pdfviewer import PDFViewer


def main():
    #实例化Object,建立窗口
    root = Tk()

    #调用PDFView方法
    PDFViewer()

    #主窗口循环显示
    root.mainloop()


if __name__ == '__main__':
    main()
