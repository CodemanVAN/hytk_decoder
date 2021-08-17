# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mian_wd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_windows(object):
    def setupUi(self, main_windows):
        main_windows.setObjectName("main_windows")
        main_windows.resize(292, 123)
        self.start = QtWidgets.QPushButton(main_windows)
        self.start.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(main_windows)
        self.label.setGeometry(QtCore.QRect(10, 100, 191, 20))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(main_windows)
        self.spinBox.setGeometry(QtCore.QRect(240, 20, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(main_windows)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 241, 16))
        self.label_2.setObjectName("label_2")
        self.single = QtWidgets.QCheckBox(main_windows)
        self.single.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.single.setObjectName("single")
        self.label_3 = QtWidgets.QLabel(main_windows)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 211, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(main_windows)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(main_windows)
        self.label_5.setGeometry(QtCore.QRect(50, 86, 211, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(main_windows)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 291, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(main_windows)
        self.label_7.setGeometry(QtCore.QRect(170, 80, 131, 20))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(main_windows)
        QtCore.QMetaObject.connectSlotsByName(main_windows)

    def retranslateUi(self, main_windows):
        _translate = QtCore.QCoreApplication.translate
        main_windows.setWindowTitle(_translate("main_windows", "一键爬取幻影坦克并解码"))
        self.start.setText(_translate("main_windows", "开冲"))
        self.label.setText(_translate("main_windows", "软件完全开源，为了安全不留信息了"))
        self.label_2.setText(_translate("main_windows", "要爬取的页数（50的整数倍，0就是吧内首页"))
        self.single.setText(_translate("main_windows", "边下载边解码"))
        self.label_3.setText(_translate("main_windows", "不勾选就是爬完所有图片才会开始解码"))
        self.label_4.setText(_translate("main_windows", "状态："))
        self.label_5.setText(_translate("main_windows", "请点击开冲"))
        self.label_6.setText(_translate("main_windows", "解码后的图片在decode文件夹，download是下载的图片"))
        self.label_7.setText(_translate("main_windows", "有能力的还请赞助一下"))
