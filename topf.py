# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topf2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Topf(object):
    def setupUi(self, Topf):
        Topf.setObjectName("Topf")
        Topf.setWindowModality(QtCore.Qt.ApplicationModal)
        Topf.setEnabled(True)
        Topf.resize(880, 580)
        Topf.setMinimumSize(QtCore.QSize(880, 580))
        Topf.setMaximumSize(QtCore.QSize(880, 580))
        Topf.setWindowOpacity(0.0)
        Topf.setWhatsThis("")
        Topf.setAutoFillBackground(False)
        Topf.setStyleSheet("background-color: #cccccc")
        Topf.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(Topf)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(560, 320, 221, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMinimumSize(QtCore.QSize(111, 111))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"    border: 2px solid rgb(255, 219, 15) ;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: rgb(255, 219, 15) ;\n"
"    color: white;\n"
"}\n"
"\n"
"QToolButton:checked::hover {\n"
"    border: 6px solid white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 4px solid rgb(255, 219, 15) ;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #CDD0D2;\n"
"    color: #69737A;\n"
"    border-radius: 20%;\n"
"    border: 2px solid #69737A;\n"
"}")
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(560, 20, 221, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(111, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"    border: 2px solid #A64AC9 ;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #A64AC9 ;\n"
"    color: white;\n"
"}\n"
"\n"
"QToolButton:checked::hover {\n"
"    border: 5px solid white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 4px solid #A64AC9;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #CCCCCC;\n"
"    color: #69737A;\n"
"    border-radius: 20px;\n"
"    border: none;\n"
"}")
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(560, 160, 221, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setMinimumSize(QtCore.QSize(111, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(20)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("QToolButton {\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"    border: 2px solid #A64AC9 ;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #A64AC9 ;\n"
"    color: white;\n"
"}\n"
"\n"
"QToolButton:checked::hover {\n"
"    border: 5px solid white;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 4px solid #A64AC9;\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #CCCCCC;\n"
"    color: #69737A;\n"
"    border-radius: 20px;\n"
"    border: none;\n"
"}")
        self.toolButton_4.setCheckable(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 301, 131))
        self.label_3.setMinimumSize(QtCore.QSize(150, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;\n"
"background-color: #FCCD04;\n"
"border-radius: 20px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(330, 20, 201, 61))
        self.label_15.setMinimumSize(QtCore.QSize(150, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: white;\n"
"background-color: #17E9E0;\n"
"border-radius: 20px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(550, 10, 241, 291))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(550, 310, 241, 261))
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 531, 291))
        self.label_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(330, 90, 201, 61))
        self.label_18.setMinimumSize(QtCore.QSize(181, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #FF652F;\n"
"border-radius: 20px;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(260, 160, 271, 131))
        self.label_12.setMinimumSize(QtCore.QSize(181, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #86C232;\n"
"border-radius: 20px;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 231, 61))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #86C232;\n"
"border-radius: 20px;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 230, 231, 61))
        self.label_13.setMinimumSize(QtCore.QSize(181, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #FE9F08 ;\n"
"border-radius: 20px;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(19, 323, 511, 241))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 301, 241))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #86C232;\n"
"color: white;\n"
"border-radius: 20px;\n"
"\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(310, 0, 201, 171))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #35B1CF;\n"
"color: white;\n"
"border-radius: 20px;\n"
"\n"
"")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 180, 71, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: #86C232;\n"
"    border-radius: 20px;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #2F4454;\n"
"    border: 4px solid #86C232;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 4px solid white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 190, 231, 51))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #FF652F;\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #2F4454;\n"
"    border: 4px solid #86C232;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 123, 35);\n"
"    border: 2px solid rgb(255, 123, 35);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #FF652F;\n"
"border-top-left-radius: 20px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(180, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #FF652F;\n"
"border-radius: 0px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(180, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 123, 35);\n"
"border-radius: 0px;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(90, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 123, 35);\n"
"border-radius: 0px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(255, 136, 17);")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(360, 0, 151, 91))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: #FF652F;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(0, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 123, 35);\n"
"border-bottom-left-radius: 20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(255, 136, 17);")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(270, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 123, 35);\n"
"border-radius: 0px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(255, 136, 17);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(255, 136, 17);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(False)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 2px solid rgb(255, 136, 17);")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 51, 51))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #FF652F;\n"
"    border-radius: 25px;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #2F4454;\n"
"    border: 4px solid #86C232;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 4px solid white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 531, 261))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(800, 10, 71, 561))
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(";\n"
"background-color: rgb(255, 255, 255);\n"
"color: white;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.label_14.setText("")
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setIndent(-1)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setEnabled(True)
        self.label_16.setGeometry(QtCore.QRect(810, 20, 51, 51))
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel {\n"
"    background-color: #35B1CF;\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"\n"
"    \n"
"}\n"
"\n"
"QLabel:hover {\n"
"    Width: 10px;\n"
"}\n"
"\n"
"")
        self.label_16.setText("")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_9.raise_()
        self.label_21.raise_()
        self.label_17.raise_()
        self.label_25.raise_()
        self.toolButton_3.raise_()
        self.toolButton_2.raise_()
        self.toolButton_4.raise_()
        self.label_3.raise_()
        self.label_15.raise_()
        self.label_18.raise_()
        self.label_12.raise_()
        self.label_4.raise_()
        self.label_13.raise_()
        self.stackedWidget.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        Topf.setCentralWidget(self.centralwidget)

        self.retranslateUi(Topf)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Topf)
        Topf.setTabOrder(self.toolButton_3, self.lineEdit)
        Topf.setTabOrder(self.lineEdit, self.pushButton_2)

    def retranslateUi(self, Topf):
        _translate = QtCore.QCoreApplication.translate
        Topf.setWindowTitle(_translate("Topf", "Горшок"))
        self.toolButton_3.setText(_translate("Topf", "Авто"))
        self.toolButton_2.setText(_translate("Topf", "Свет"))
        self.toolButton_4.setText(_translate("Topf", "Насос"))
        self.label_3.setText(_translate("Topf", "TextLabel"))
        self.label_15.setText(_translate("Topf", "TextLabel"))
        self.label_18.setText(_translate("Topf", "TextLabel"))
        self.label_12.setText(_translate("Topf", "TextLabel"))
        self.label_4.setText(_translate("Topf", "TextLabel"))
        self.label_13.setText(_translate("Topf", "TextLabel"))
        self.label_2.setText(_translate("Topf", "10"))
        self.label.setText(_translate("Topf", "20"))
        self.pushButton_3.setText(_translate("Topf", ">"))
        self.pushButton_2.setText(_translate("Topf", "Сохранить"))
        self.label_7.setText(_translate("Topf", "Освещение"))
        self.label_8.setText(_translate("Topf", "Аэрация"))
        self.label_10.setText(_translate("Topf", "Кол-во"))
        self.label_6.setText(_translate("Topf", "Конец"))
        self.lineEdit_4.setText(_translate("Topf", "10"))
        self.label_19.setText(_translate("Topf", "Дни"))
        self.label_5.setText(_translate("Topf", "Начало"))
        self.lineEdit_3.setText(_translate("Topf", "5-2"))
        self.label_11.setText(_translate("Topf", "Время"))
        self.lineEdit.setText(_translate("Topf", "10:00"))
        self.lineEdit_2.setText(_translate("Topf", "20:00"))
        self.lineEdit_5.setText(_translate("Topf", "0"))
        self.pushButton.setText(_translate("Topf", "<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Topf = QtWidgets.QMainWindow()
    ui = Ui_Topf()
    ui.setupUi(Topf)
    Topf.show()
    sys.exit(app.exec_())

