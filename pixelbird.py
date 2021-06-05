import countbird
import skimage.io as io
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tkinter as tk
from tkinter import filedialog
import numpy as np

win_width = 500
win_height = 500

class MyMainWindow(QMainWindow):    
    src_path = ""
    dest_path = ""
    bird_cnt = 0
    savepath = ""
    color_thres = 100
    size_thres = 2

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(win_width,win_height)
        self.setWindowTitle('像素鸟计数器')
        self.setStyleSheet("background-color:#DAEAFF")

        self.select_btn=QPushButton('选择要数鸟的图片',self)
        self.select_btn.clicked.connect(self.select_pic)
        self.select_btn.setGeometry(20,20,200,30)
        
        self.output_btn=QPushButton('选择输出目录',self)
        self.output_btn.clicked.connect(self.select_output)
        self.output_btn.setGeometry(20,60,200,30)

        self.count_btn=QPushButton('数鸟！',self)
        self.count_btn.clicked.connect(self.count_birds)
        self.count_btn.setGeometry(150,100,200,30)

        self.label_src_path=QLabel(self)
        self.label_src_path.setText(self.src_path)
        self.label_src_path.setGeometry(230,20,250,30)

        self.label_output_path=QLabel(self)
        self.label_output_path.setText(self.dest_path)
        self.label_output_path.setGeometry(230,60,250,30)

        self.display_pic = QLabel(self)
        self.display_pic.setGeometry(100,140,300,300)
        self.display_pic.setScaledContents(True)

        self.count_num=QLabel(self)
        self.count_num.setText(str(self.bird_cnt)+" 只像素鸟！")
        self.count_num.setAlignment(Qt.AlignCenter)
        self.count_num.setGeometry(50,410,400,30)

    def select_pic(self):
        root = tk.Tk()
        root.withdraw()
        Folderpath = filedialog.askopenfilename()
        self.src_path = Folderpath ###
        self.label_src_path.setText(self.src_path)

    def select_output(self):
        root = tk.Tk()
        root.withdraw()
        Folderpath = filedialog.askdirectory()
        self.dest_path = Folderpath ###
        self.label_output_path.setText(self.dest_path)
    
    def count_birds(self):
        im, self.bird_cnt = countbird.run_output(self.src_path)
        pic_name = ((self.src_path.split("/")[-1]).split("."))[-2]
        self.savepath = self.dest_path + "/" +pic_name + "_" + str(self.bird_cnt) + "_pixelbirds.jpg"
        io.imsave(self.savepath,im)
        piximg = QPixmap(self.savepath)
        self.display_pic.setPixmap(piximg)
        self.count_num.setText(str(self.bird_cnt)+" 只像素鸟！")


test_path = "input/onlybird.jpg"
test_output_path = "input/"
#im,cnt = countbird.run_output(test_path)
#plt.imshow(im)
#plt.show()

app=QApplication(sys.argv)
win = MyMainWindow()
win.show()
sys.exit(app.exec_())

a=0
