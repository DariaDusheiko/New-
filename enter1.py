# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enter.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, w, h):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(w, h)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(102,225,205,150), stop:1 rgba(255, 114, 150, 150));\n"
"font-family: Candara;\n"
"justify-content: center;\n"
"align-items: center;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"justify-content: center;\n"
"align-items: center;")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.enter_frame = QFrame(self.centralwidget)
        self.enter_frame.setObjectName(u"enter_frame")
        self.enter_frame.setMinimumSize(QSize(270, 300))
        self.enter_frame.setMaximumSize(QSize(270, 310))
        self.enter_frame.setStyleSheet(u"\n"
"border-radius: 45px;\n"
"background-color: rgb(250, 250, 250);")
        self.verticalLayout = QVBoxLayout(self.enter_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vhod = QLabel(self.enter_frame)
        self.vhod.setObjectName(u"vhod")
        self.vhod.setMinimumSize(QSize(0, 50))
        self.vhod.setMaximumSize(QSize(16777215, 16777215))
        self.vhod.setStyleSheet(u"background-color: none;")

        self.verticalLayout.addWidget(self.vhod, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.login_label = QLabel(self.enter_frame)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setMinimumSize(QSize(0, 30))
        self.login_label.setStyleSheet(u"background-color: none;")

        self.verticalLayout.addWidget(self.login_label, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.login = QLineEdit(self.enter_frame)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(185, 30))
        self.login.setMaximumSize(QSize(185, 16777215))
        self.login.setStyleSheet(u"background-color: #d4d4d4;\n"
"background-color: #f5f5f5;\n"
"border-radius: 10px;\n"
"border: 1px rgb(255, 255, 255);\n"
"padding: 4px;\n"
"color: #878787;")

        self.verticalLayout.addWidget(self.login, 0, Qt.AlignHCenter)

        self.password_label = QLabel(self.enter_frame)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(0, 30))
        self.password_label.setStyleSheet(u"background-color: none;")

        self.verticalLayout.addWidget(self.password_label, 0, Qt.AlignHCenter)

        self.password = QLineEdit(self.enter_frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(185, 30))
        self.password.setMaximumSize(QSize(185, 16777215))
        self.password.setStyleSheet(u"background-color: #d4d4d4;\n"
"background-color: #f5f5f5;\n"
"border-radius: 10px;\n"
"border: 1px rgb(255, 255, 255);\n"
"padding: 4px;\n"
"color: #878787;")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password, 0, Qt.AlignHCenter)

        self.label = QLabel(self.enter_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"font-size: 9px;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.enter_pushButton = QPushButton(self.enter_frame)
        self.enter_pushButton.setObjectName(u"enter_pushButton")
        self.enter_pushButton.setMinimumSize(QSize(60, 25))
        self.enter_pushButton.setMaximumSize(QSize(60, 16777215))
        self.enter_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enter_pushButton.setStyleSheet(u"QPushButton{\n"
"		background-color: rgba(255, 114, 150, 50);\n"
"		border-radius: 7px;\n"
"		font-weight: bold;\n"
"		color: rgb(135, 135, 135);\n"
"		margin_bottom: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"		color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.enter_pushButton, 0, Qt.AlignHCenter)

        self.reg_pushButton = QPushButton(self.enter_frame)
        self.reg_pushButton.setObjectName(u"reg_pushButton")
        self.reg_pushButton.setMinimumSize(QSize(0, 40))
        self.reg_pushButton.setMaximumSize(QSize(16777215, 40))
        self.reg_pushButton.setSizeIncrement(QSize(0, 40))
        self.reg_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg_pushButton.setStyleSheet(u"QPushButton{\n"
"		background-color: none;\n"
"		color: rgb(135, 135, 135);\n"
"		font-size: 14px;\n"
"		margin-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"		color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.reg_pushButton, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.enter_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"		background-color: none;\n"
"		color: rgb(135, 135, 135);\n"
"		font-size: 12px;\n"
"		margin-bottom: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"		color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.enter_frame, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WIPILLs", None))
        self.vhod.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#878787;\">\u0412\u0425\u041e\u0414</span></p></body></html>", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:#4f9d8f;\">\u041b\u043e\u0433\u0438\u043d</span></p></body></html>", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#4f9d8f;\">\u041f\u0430\u0440\u043e\u043b\u044c</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043b\u043e\u0433\u0438\u043d \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c.", None))
        self.enter_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.reg_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

