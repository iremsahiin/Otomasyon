from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 861, 671))
        self.label.setMinimumSize(QtCore.QSize(861, 671))
        self.label.setMaximumSize(QtCore.QSize(861, 671))
        self.label.setLineWidth(2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("EARTH in 8K ULTRA HD - Tour Through the Planet Earth - Best Places and Animals Relaxing Music 8K TV - YouTube - Google Chrome 20.02.2022 18_01_05.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(46, 0, 140);")
        self.label_2.setObjectName("label_2")
        self.Ad = QtWidgets.QLabel(self.centralwidget)
        self.Ad.setGeometry(QtCore.QRect(40, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Ad.setFont(font)
        self.Ad.setObjectName("Ad")
        self.Soyad = QtWidgets.QLabel(self.centralwidget)
        self.Soyad.setGeometry(QtCore.QRect(40, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Soyad.setFont(font)
        self.Soyad.setObjectName("Soyad")
        self.TcNo = QtWidgets.QLabel(self.centralwidget)
        self.TcNo.setGeometry(QtCore.QRect(40, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TcNo.setFont(font)
        self.TcNo.setObjectName("TcNo")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 70, 133, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 130, 133, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 100, 133, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 190, 171, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bolumu = QtWidgets.QComboBox(self.frame)
        self.bolumu.setGeometry(QtCore.QRect(18, 40, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bolumu.setFont(font)
        self.bolumu.setObjectName("bolumu")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Dogumtarihi = QtWidgets.QCalendarWidget(self.centralwidget)
        self.Dogumtarihi.setGeometry(QtCore.QRect(290, 100, 311, 161))
        self.Dogumtarihi.setObjectName("Dogumtarihi")
        self.tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.tablo.setGeometry(QtCore.QRect(-5, 380, 891, 361))
        self.tablo.setRowCount(20)
        self.tablo.setColumnCount(5)
        self.tablo.setObjectName("tablo")
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablo.setHorizontalHeaderItem(4, item)
        self.tablo.horizontalHeader().setDefaultSectionSize(167)
        self.kayitekle = QtWidgets.QPushButton(self.centralwidget)
        self.kayitekle.setGeometry(QtCore.QRect(160, 330, 201, 23))
        self.kayitekle.setObjectName("kayitekle")
        self.kayitsil = QtWidgets.QPushButton(self.centralwidget)
        self.kayitsil.setGeometry(QtCore.QRect(470, 330, 201, 23))
        self.kayitsil.setObjectName("kayitsil")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hoşgeldiniz"))
        self.label_2.setText(_translate("MainWindow", "   ÖĞRENCİ KAYIT SİSTEMİ"))
        self.Ad.setText(_translate("MainWindow", "Ad:"))
        self.Soyad.setText(_translate("MainWindow", "Soyad:"))
        self.TcNo.setText(_translate("MainWindow", "Tc No:"))
        self.label_3.setText(_translate("MainWindow", "Bölümü:"))
        self.label_4.setText(_translate("MainWindow", "Doğum Tarihi:"))
        item = self.tablo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ad"))
        item = self.tablo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Soyad"))
        item = self.tablo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tc No"))
        item = self.tablo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bölümü"))
        item = self.tablo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Doğum Tarihi"))
        self.kayitekle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.kayitsil.setText(_translate("MainWindow", "Kayıt Sil"))

