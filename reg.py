# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow, weight_window, hight_window):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(weight_window, hight_window)
        MainWindow.setStyleSheet(u"background-color: rgba(255, 114, 150, 150);\n"
"background-size: Auto Auto;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(341, 531))
        self.verticalFrame.setStyleSheet(u"border-radius: 35px;\n"
"background-color: rgb(255, 226, 237);\n"
"border: 2px solid;\n"
"border-color: rgb(255, 185, 219);")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.REGlabel = QLabel(self.verticalFrame)
        self.REGlabel.setObjectName(u"REGlabel")
        self.REGlabel.setMinimumSize(QSize(120, 70))
        self.REGlabel.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.REGlabel.setFont(font)
        self.REGlabel.setStyleSheet(u"color: rgb(195, 122, 161);\n"
"font-size: 20px;\n"
"border: none;\n"
"margin-top: 25px;")

        self.verticalLayout.addWidget(self.REGlabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.log_label_2 = QLabel(self.verticalFrame)
        self.log_label_2.setObjectName(u"log_label_2")
        self.log_label_2.setStyleSheet(u"color: rgb(95, 50, 70);\n"
"margin-bottom: 7px;\n"
"border: none;")

        self.verticalLayout.addWidget(self.log_label_2, 0, Qt.AlignHCenter)

        self.login_lineEdit = QLineEdit(self.verticalFrame)
        self.login_lineEdit.setObjectName(u"login_lineEdit")
        self.login_lineEdit.setMinimumSize(QSize(250, 35))
        self.login_lineEdit.setStyleSheet(u"\n"
"background-color: rgb(255, 247, 255);\n"
"border-radius: 10px;\n"
"border: 1px rgb(255, 255, 255);\n"
"padding: 4px;\n"
"color: #878787;\n"
"border: 2px dotted;\n"
"border-color: rgb(255, 185, 219);")

        self.verticalLayout.addWidget(self.login_lineEdit, 0, Qt.AlignHCenter)

        self.pas_label_3 = QLabel(self.verticalFrame)
        self.pas_label_3.setObjectName(u"pas_label_3")
        self.pas_label_3.setStyleSheet(u"margin-top: 10px;\n"
"margin-bottom: 7px;\n"
"color: rgb(95, 50, 70);\n"
"border: none;")

        self.verticalLayout.addWidget(self.pas_label_3, 0, Qt.AlignHCenter)

        self.password_lineEdit_2 = QLineEdit(self.verticalFrame)
        self.password_lineEdit_2.setObjectName(u"password_lineEdit_2")
        self.password_lineEdit_2.setMinimumSize(QSize(250, 35))
        self.password_lineEdit_2.setMaximumSize(QSize(188, 16777215))
        self.password_lineEdit_2.setStyleSheet(u"background-color: rgb(255, 247, 255);\n"
"border-radius: 10px;\n"
"border: 1px rgb(255, 255, 255);\n"
"padding: 4px;\n"
"color: #878787;\n"
"border: 2px dotted;\n"
"border-color: rgb(255, 185, 219);")
        self.password_lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_lineEdit_2, 0, Qt.AlignHCenter)

        self.repeatpass_label_4 = QLabel(self.verticalFrame)
        self.repeatpass_label_4.setObjectName(u"repeatpass_label_4")
        self.repeatpass_label_4.setStyleSheet(u"margin-top: 10px;\n"
"margin-bottom: 7px;\n"
"color: rgb(95, 50, 70);\n"
"border: none;")

        self.verticalLayout.addWidget(self.repeatpass_label_4, 0, Qt.AlignHCenter)

        self.repeatpassword_lineEdit_3 = QLineEdit(self.verticalFrame)
        self.repeatpassword_lineEdit_3.setObjectName(u"repeatpassword_lineEdit_3")
        self.repeatpassword_lineEdit_3.setMinimumSize(QSize(250, 35))
        self.repeatpassword_lineEdit_3.setStyleSheet(u"background-color: rgb(255, 247, 255);\n"
"border-radius: 10px;\n"
"border: 1px rgb(255, 255, 255);\n"
"padding: 4px;\n"
"color: #878787;\n"
"border: 2px dotted;\n"
"border-color: rgb(255, 185, 219);")
        self.repeatpassword_lineEdit_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.repeatpassword_lineEdit_3, 0, Qt.AlignHCenter)

        self.gender_label_5 = QLabel(self.verticalFrame)
        self.gender_label_5.setObjectName(u"gender_label_5")
        self.gender_label_5.setStyleSheet(u"margin-top: 10px;\n"
"margin-bottom: 7px;\n"
"color: rgb(95, 50, 70);\n"
"border: none;")

        self.verticalLayout.addWidget(self.gender_label_5, 0, Qt.AlignHCenter)

        self.lineEdit = QLineEdit(self.verticalFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(250, 35))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 247, 255);\n"
"border-radius: 10px;\n"
"border: 1px rgb(255, 255, 255);\n"
"padding: 4px;\n"
"color: #878787;\n"
"border: 2px dotted;\n"
"border-color: rgb(255, 185, 219);")

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignHCenter)

        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 226, 237);\n"
"border: none;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.verticalFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(180, 70))
        self.pushButton.setMaximumSize(QSize(160, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"		background-color: rgba(255, 114, 150, 20);\n"
"		border-radius: 10px;\n"
"		font-weight: bold;\n"
"		color: rgb(195, 122, 161);\n"
"		margin: 17px;\n"
"		border: 1px solid;\n"
"		border-color: rgb(255, 169, 203);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"		color: rgb(255, 185, 219);\n"
"		background-color: rgb(255, 247, 255);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.verticalFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WIPILLs", None))
        self.REGlabel.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0413\u0418\u0421\u0422\u0420\u0410\u0426\u0418\u042f", None))
        self.log_label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pas_label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.repeatpass_label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.gender_label_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u043f\u043e\u0447\u0442\u0443 \u0434\u043b\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u0432\u0432\u043e\u0434 \u043f\u0430\u0440\u043e\u043b\u044f.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

