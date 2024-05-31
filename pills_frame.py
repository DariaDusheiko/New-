# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pills_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QToolBar,
    QVBoxLayout, QWidget)
import res_main_rc

class Ui_MainWindow_5(object):
    def setupUi(self, MainWindow, w, h):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(w, h)
        icon = QIcon()
        icon.addFile(u":/newPrefix/picture/home_doctor_care_treatment_support_medical_hehcare_icon_261646.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(228, 114, 150);")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_exit.setIcon(icon)
        self.action_action = QAction(MainWindow)
        self.action_action.setObjectName(u"action_action")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/picture/pill.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_action.setIcon(icon1)
        self.my_pill = QAction(MainWindow)
        self.my_pill.setObjectName(u"my_pill")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/picture/doctor_heh_analysis_hehcare_analytics_monitoring_patient_icon_261616.png", QSize(), QIcon.Normal, QIcon.Off)
        self.my_pill.setIcon(icon2)
        self.action_add_pill = QAction(MainWindow)
        self.action_add_pill.setObjectName(u"action_add_pill")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/picture/ui_app_application_computer_program_software_legacy_icon_261654.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_add_pill.setIcon(icon3)
        self.action_change_akk = QAction(MainWindow)
        self.action_change_akk.setObjectName(u"action_change_akk")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/picture/clipboard_checklist_check_document_list_record_patient_icon_261627.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_change_akk.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(228, 114, 150);")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(420, 550))
        font = QFont()
        font.setPointSize(15)
        self.verticalFrame.setFont(font)
        self.verticalFrame.setStyleSheet(u"border-radius: 35px;\n"
"background-color:rgb(255, 230, 245);\n"
"border: 2px solid;\n"
"border-color: rgb(120, 213, 193);\n"
"padding-bottom: 10px;")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.verticalFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 italic 16pt \"Segoe UI\";\n"
"color: rgb(104, 199, 167);\n"
"font-size: 20px;\n"
"border: none;\n"
"margin-top: 25px;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.tableView = QTableView(self.verticalFrame)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.pushButton = QPushButton(self.verticalFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(104, 199, 167);\n"
"font-size: 13px;\n"
"border: none;\n"
"margin-top: 25px;")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.verticalFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 10))
        self.menubar.setMinimumSize(QSize(0, 10))
        self.menubar.setMaximumSize(QSize(16777215, 10))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.toolBar.setIconSize(QSize(70, 70))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        self.toolBar_2.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.toolBar_2.setIconSize(QSize(70, 70))
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar_2)

        self.toolBar.addAction(self.action_action)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_exit)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.my_pill)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.action_add_pill)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.action_change_akk)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"&exit_", None))
        self.action_action.setText(QCoreApplication.translate("MainWindow", u"&action", None))
        self.my_pill.setText(QCoreApplication.translate("MainWindow", u"&my_pill", None))
        self.action_add_pill.setText(QCoreApplication.translate("MainWindow", u"&add_pill", None))
        self.action_change_akk.setText(QCoreApplication.translate("MainWindow", u"&change_akk", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0415\u041a\u0410\u0420\u0421\u0422\u0412A", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

