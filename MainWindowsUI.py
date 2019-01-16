# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowsUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import *
import sys
import BlueNoise
import GreenNoise
import PinkNoise
import PurpleNoise
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 40, 321, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NoisePoints = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.NoisePoints.setObjectName("NoisePoints")
        self.NoisePoints.setStyleSheet("QLabel{background:gray}")
        self.horizontalLayout.addWidget(self.NoisePoints)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(720, 40, 321, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NoiseSpectrum = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.NoiseSpectrum.setObjectName("NoiseSpectrum")
        self.NoiseSpectrum.setStyleSheet("QLabel{background:gray}")
        self.horizontalLayout_2.addWidget(self.NoiseSpectrum)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(290, 390, 751, 351))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.NoiseSpectrumPlot = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.NoiseSpectrumPlot.setObjectName("NoiseSpectrumPlot")
        self.NoiseSpectrumPlot.setStyleSheet("QLabel{background:gray}")
        self.horizontalLayout_4.addWidget(self.NoiseSpectrumPlot)

        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(60, 700, 161, 41))
        self.Run.setObjectName("Run")
        self.Run.clicked.connect(self.clickRun)


        self.BlurSigma = QtWidgets.QSlider(self.centralwidget)
        self.BlurSigma.setGeometry(QtCore.QRect(30, 510, 221, 22))
        self.BlurSigma.setOrientation(QtCore.Qt.Horizontal)
        self.BlurSigma.setObjectName("BlurSigma")
        self.BlurSigma.setMinimum(0.0)
        self.BlurSigma.setMaximum(maxBlurSigma * 10.0)
        self.BlurSigma.valueChanged.connect(self.changeBlurSigma)

        self.PointsNum = QtWidgets.QSlider(self.centralwidget)
        self.PointsNum.setGeometry(QtCore.QRect(30, 360, 221, 22))
        self.PointsNum.setOrientation(QtCore.Qt.Horizontal)
        self.PointsNum.setObjectName("PointsNum")
        self.PointsNum.setMinimum(1000)
        self.PointsNum.setMaximum(4000)
        self.PointsNum.valueChanged.connect(self.changePointsNum)

        self.NoiseType = QtWidgets.QComboBox(self.centralwidget)
        self.NoiseType.setGeometry(QtCore.QRect(30, 100, 221, 22))
        self.NoiseType.setObjectName("NoiseType")
        self.NoiseType.addItem("BlueNoise")
        self.NoiseType.addItem("GreenNoise")
        self.NoiseType.addItem("PinkNoise")
        self.NoiseType.addItem("PurpleNoise")
        self.NoiseType.activated.connect(self.ComboBoxActivated)


        self.ShowNoiseType = QtWidgets.QLabel(self.centralwidget)
        self.ShowNoiseType.setGeometry(QtCore.QRect(30, 50, 221, 16))
        self.ShowNoiseType.setObjectName("ShowNoiseType")
        self.ShowPointsNum = QtWidgets.QLabel(self.centralwidget)
        self.ShowPointsNum.setGeometry(QtCore.QRect(30, 320, 221, 16))
        self.ShowPointsNum.setObjectName("ShowPointsNum")
        self.ShowSigmaValue = QtWidgets.QLabel(self.centralwidget)
        self.ShowSigmaValue.setGeometry(QtCore.QRect(30, 470, 211, 16))
        self.ShowSigmaValue.setObjectName("ShowSigmaValue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 用于生成噪声的数据值
        self.NoiseTypeIndex = 0
        self.BlurSigmaValue = 0.0
        self.PointsNumValue = 1000

    def changeBlurSigma(self, value):
        self.ShowSigmaValue.setText("BlurSigma:" + str(float(value / 10.0)))
        self.BlurSigmaValue = value / 10.0

    def changePointsNum(self,value):
        self.ShowPointsNum.setText("噪声点数量:"+str(value))
        self.PointsNumValue=value

    def ComboBoxActivated(self,text):
        self.ShowNoiseType.setText("选择噪声:"+self.NoiseType.currentText())
        self.NoiseTypeIndex = self.NoiseType.currentIndex()
        print(self.NoiseType.currentIndex())

    def CreateThreePic(self):
        try:
            if self.NoiseTypeIndex == 0:
                BlueNoise.BlueNoise(blursigma=self.BlurSigmaValue,width=250,height=250,num=self.PointsNumValue,scale=0.05)
                points_path = os.getcwd()+'/BlueNoise.jpg'
                spectrum_path =os.getcwd()+ '/BlueNoiseSpectrum.jpg'
                spectrumplot_path = os.getcwd()+'/BlueNoiseSpectrumPlot.jpg'
                points_jpg = QtGui.QPixmap(points_path)
                spectrum_jpg = QtGui.QPixmap(spectrum_path)
                spectrumplot_jpg = QtGui.QPixmap(spectrumplot_path)
                self.NoisePoints.setPixmap(points_jpg)
                self.NoisePoints.setScaledContents(True)
                self.NoisePoints.repaint()
                self.NoiseSpectrum.setPixmap(spectrum_jpg)
                self.NoiseSpectrum.setScaledContents(True)
                self.NoiseSpectrum.repaint()
                self.NoiseSpectrumPlot.setPixmap(spectrumplot_jpg)
                self.NoiseSpectrumPlot.setScaledContents(True)
                self.NoiseSpectrumPlot.repaint()
            elif self.NoiseTypeIndex == 1:
                GreenNoise.GreenNoise(blursigma_weak=self.BlurSigmaValue,width=250,height=250,num=self.PointsNumValue)
                points_path = os.getcwd()+'/GreenNoise.jpg'
                spectrum_path = os.getcwd()+'/GreenNoiseSpectrum.jpg'
                spectrumplot_path = os.getcwd()+'/GreenNoiseSpectrumPlot.jpg'
                points_jpg = QtGui.QPixmap(points_path)
                spectrum_jpg = QtGui.QPixmap(spectrum_path)
                spectrumplot_jpg = QtGui.QPixmap(spectrumplot_path)
                self.NoisePoints.setPixmap(points_jpg)
                self.NoisePoints.setScaledContents(True)
                self.NoisePoints.repaint()
                self.NoiseSpectrum.setPixmap(spectrum_jpg)
                self.NoiseSpectrum.setScaledContents(True)
                self.NoiseSpectrum.repaint()
                self.NoiseSpectrumPlot.setPixmap(spectrumplot_jpg)
                self.NoiseSpectrumPlot.setScaledContents(True)
                self.NoiseSpectrumPlot.repaint()
            elif self.NoiseTypeIndex == 2:
                PinkNoise.PinkNoise(blursigma=self.BlurSigmaValue,width=250,height=250,num=self.PointsNumValue)
                points_path = os.getcwd()+'/PinkNoise.jpg'
                spectrum_path = os.getcwd()+'/PinkNoiseSpectrum.jpg'
                spectrumplot_path = os.getcwd()+'/PinkNoiseSpectrumPlot.jpg'
                points_jpg = QtGui.QPixmap(points_path)
                spectrum_jpg = QtGui.QPixmap(spectrum_path)
                spectrumplot_jpg = QtGui.QPixmap(spectrumplot_path)
                self.NoisePoints.setPixmap(points_jpg)
                self.NoisePoints.setScaledContents(True)
                self.NoisePoints.repaint()
                self.NoiseSpectrum.setPixmap(spectrum_jpg)
                self.NoiseSpectrum.setScaledContents(True)
                self.NoiseSpectrum.repaint()
                self.NoiseSpectrumPlot.setPixmap(spectrumplot_jpg)
                self.NoiseSpectrumPlot.setScaledContents(True)
                self.NoiseSpectrumPlot.repaint()
            elif self.NoiseTypeIndex == 3:
                PurpleNoise.PurpleNoise(blursigma_weak=self.BlurSigmaValue,width=250,height=250,num=self.PointsNumValue)
                points_path = os.getcwd()+'/PurpleNoise.jpg'
                spectrum_path = os.getcwd()+'/PurpleNoiseSpectrum.jpg'
                spectrumplot_path = os.getcwd()+'/PurpleNoiseSpectrumPlot.jpg'
                points_jpg = QtGui.QPixmap(points_path)
                spectrum_jpg = QtGui.QPixmap(spectrum_path)
                spectrumplot_jpg = QtGui.QPixmap(spectrumplot_path)
                self.NoisePoints.setPixmap(points_jpg)
                self.NoisePoints.setScaledContents(True)
                self.NoisePoints.repaint()
                self.NoiseSpectrum.setPixmap(spectrum_jpg)
                self.NoiseSpectrum.setScaledContents(True)
                self.NoiseSpectrum.repaint()
                self.NoiseSpectrumPlot.setPixmap(spectrumplot_jpg)
                self.NoiseSpectrumPlot.setScaledContents(True)
                self.NoiseSpectrumPlot.repaint()
        except:
            pass
    def clickRun(self):
        print("Run...")
        self.CreateThreePic()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "噪声生成器"))
        self.NoisePoints.setText(_translate("MainWindow", "NoisePoints"))
        self.NoiseSpectrum.setText(_translate("MainWindow", "NoiseSpectrum"))
        self.NoiseSpectrumPlot.setText(_translate("MainWindow", "NoiseSpectrumPlot"))
        self.Run.setText(_translate("MainWindow", "运行"))
        self.ShowNoiseType.setText(_translate("MainWindow", "选择噪声:"))
        self.ShowPointsNum.setText(_translate("MainWindow", "噪声点数量:"))
        self.ShowSigmaValue.setText(_translate("MainWindow", "BlurSigma:"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())