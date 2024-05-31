# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_pill.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)
import res_main_rc

class Ui_MainWindow_4(object):
    def setupUi(self, MainWindow, w, h):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(w, h)
        icon = QIcon()
        icon.addFile(u":/newPrefix/picture/home_doctor_care_treatment_support_medical_hehcare_icon_261646.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgba(102,225,205,150);")
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
        self.centralwidget.setStyleSheet(u"background-color: rgb(103, 226, 206);")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(345, 550))
        self.verticalFrame.setStyleSheet(u"border-radius: 35px;\n"
"background-color: rgb(201, 255, 246);\n"
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

        self.label_2 = QLabel(self.verticalFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(84, 161, 146);\n"
"font-size: 12px;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.lineEdit = QLineEdit(self.verticalFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(230, 0))
        self.lineEdit.setMaximumSize(QSize(250, 32))
        self.lineEdit.setStyleSheet(u"background-color: rgb(243, 255, 255);\n"
"border: 2px dotted;\n"
"border-color: rgb(120, 213, 193);\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignHCenter)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.verticalFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(84, 161, 146);\n"
"font-size: 12px;\n"
"border: none;\n"
"padding: none;\n"
"padding-left: 0px;\n"
"padding-right: 0px;")

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.comboBox = QComboBox(self.verticalFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(130, 25))
        self.comboBox.setStyleSheet(u"background-color: rgb(243, 255, 255);\n"
"border-radius: 10px;\n"
"padding-left: 6px;\n"
"padding-right: 2px;\n"
"border: 2px dotted;\n"
"border-color: rgb(120, 213, 193);\n"
"border-radius: 10px;")

        self.verticalLayout_3.addWidget(self.comboBox, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.frame_2 = QFrame(self.verticalFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;\n"
"padding-bottom: 10px;")
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"color: rgb(84, 161, 146);\n"
"font-size: 12px;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(230, 0))
        self.lineEdit_2.setMaximumSize(QSize(120, 32))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(243, 255, 255);\n"
"border: 2px dotted;\n"
"border-color: rgb(120, 213, 193);\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignVCenter)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(90, 0))
        self.pushButton.setMaximumSize(QSize(90, 16777215))
        self.pushButton.setStyleSheet(u"color: rgb(224, 255, 251);\n"
"background-color: rgb(104, 199, 167);\n"
"border-radius: 13px;\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0415\u041a\u0410\u0420\u0421\u0422\u0412\u041e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u044f\u0442\u044c \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043a\u0430\u0436\u0434\u044b\u0435:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"...", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0436\u0434\u044b\u0439 \u0434\u0435\u043d\u044c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0447\u0435\u0440\u0435\u0437 \u0434\u0435\u043d\u044c", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0436\u0434\u0443\u044e \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0436\u0434\u044b\u0439 \u043c\u0435\u0441\u044f\u0446", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0443\u0434\u043e\u0431\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0435\u043c\u0430 (00:00):", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

