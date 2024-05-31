# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mane.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import res_main_rc

class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow, w, h):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(w, h)
        MainWindow.setMinimumSize(QSize(0, 30))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 114, 150), stop:1 rgb(102,225,205));\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255,215,238), stop:1 rgb(217,255,246));")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon = QIcon()
        icon.addFile(u":/newPrefix/picture/pill.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.action.setIcon(icon)
        self.my_pill = QAction(MainWindow)
        self.my_pill.setObjectName(u"my_pill")
        self.my_pill.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/picture/doctor_heh_analysis_hehcare_analytics_monitoring_patient_icon_261616.png", QSize(), QIcon.Normal, QIcon.Off)
        self.my_pill.setIcon(icon1)
        self.add_pill = QAction(MainWindow)
        self.add_pill.setObjectName(u"add_pill")
        self.add_pill.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/picture/emotsick_heh_hehcare_doctor_treatment_patient_icon_261608.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_pill.setIcon(icon2)
        self.add_pill.setShortcutVisibleInContextMenu(False)
        self.exit_ = QAction(MainWindow)
        self.exit_.setObjectName(u"exit_")
        self.exit_.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/picture/home_doctor_care_treatment_support_medical_hehcare_icon_261646.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_.setIcon(icon3)
        self.change_akk = QAction(MainWindow)
        self.change_akk.setObjectName(u"change_akk")
        self.change_akk.setCheckable(True)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/picture/clipboard_checklist_check_document_list_record_patient_icon_261627.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change_akk.setIcon(icon4)
        self.change_akk.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background-color: none;\n"
"font: 700 italic 16pt \"Segoe UI\";\n"
"color: rgb(145, 145, 145);")

        self.verticalLayout.addWidget(self.label_36, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"padding: 10px;")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 2, 0, 1, 1)

        self.textEdit_25 = QTextEdit(self.frame)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_25.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_25, 8, 3, 1, 1)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_20, 5, 5, 1, 1)

        self.textEdit_11 = QTextEdit(self.frame)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_11.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_11, 4, 3, 1, 1)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_22, 7, 0, 1, 1)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_21, 5, 6, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_4, 1, 4, 1, 1)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_18, 5, 3, 1, 1)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_24, 7, 2, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_35, 9, 6, 1, 1)

        self.textEdit_21 = QTextEdit(self.frame)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_21.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_21, 6, 6, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(198, 0, 106);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_5, 1, 3, 1, 1)

        self.textEdit_26 = QTextEdit(self.frame)
        self.textEdit_26.setObjectName(u"textEdit_26")
        self.textEdit_26.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_26.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_26, 8, 4, 1, 1)

        self.textEdit_5 = QTextEdit(self.frame)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_5.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_5, 2, 4, 1, 1)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_31, 9, 2, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_30, 9, 1, 1, 1)

        self.textEdit_15 = QTextEdit(self.frame)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_15.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_15, 6, 0, 1, 1)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_23, 7, 1, 1, 1)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_29, 9, 0, 1, 1)

        self.textEdit_18 = QTextEdit(self.frame)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_18.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_18, 6, 3, 1, 1)

        self.textEdit_31 = QTextEdit(self.frame)
        self.textEdit_31.setObjectName(u"textEdit_31")
        self.textEdit_31.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_31.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_31, 10, 2, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_3.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_3, 2, 2, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_11, 3, 3, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.textEdit_33 = QTextEdit(self.frame)
        self.textEdit_33.setObjectName(u"textEdit_33")
        self.textEdit_33.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_33.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_33, 10, 4, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_2, 2, 1, 1, 1)

        self.textEdit_9 = QTextEdit(self.frame)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_9.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_9, 4, 1, 1, 1)

        self.textEdit_20 = QTextEdit(self.frame)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_20.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_20, 6, 5, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_14, 3, 6, 1, 1)

        self.textEdit_23 = QTextEdit(self.frame)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_23.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_23, 8, 1, 1, 1)

        self.textEdit_7 = QTextEdit(self.frame)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_7.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_7, 2, 6, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_17, 5, 2, 1, 1)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_28, 7, 6, 1, 1)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_25, 7, 3, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.textEdit_8 = QTextEdit(self.frame)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_8.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_8, 4, 0, 1, 1)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_26, 7, 4, 1, 1)

        self.textEdit_27 = QTextEdit(self.frame)
        self.textEdit_27.setObjectName(u"textEdit_27")
        self.textEdit_27.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_27.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_27, 8, 5, 1, 1)

        self.textEdit_24 = QTextEdit(self.frame)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_24.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_24, 8, 2, 1, 1)

        self.textEdit_35 = QTextEdit(self.frame)
        self.textEdit_35.setObjectName(u"textEdit_35")
        self.textEdit_35.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_35.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_35, 10, 6, 1, 1)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_33, 9, 4, 1, 1)

        self.textEdit_6 = QTextEdit(self.frame)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_6.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_6, 2, 5, 1, 1)

        self.textEdit_32 = QTextEdit(self.frame)
        self.textEdit_32.setObjectName(u"textEdit_32")
        self.textEdit_32.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_32.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_32, 10, 3, 1, 1)

        self.textEdit_13 = QTextEdit(self.frame)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_13.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_13, 4, 5, 1, 1)

        self.textEdit_12 = QTextEdit(self.frame)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_12.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_12, 4, 4, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_12, 3, 4, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_16, 5, 1, 1, 1)

        self.textEdit_28 = QTextEdit(self.frame)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_28.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_28, 8, 6, 1, 1)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_19, 5, 4, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_13, 3, 5, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(198, 0, 106);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_2, 1, 5, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(198, 0, 106);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.textEdit_17 = QTextEdit(self.frame)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_17.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_17, 6, 2, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_27, 7, 5, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_10, 3, 2, 1, 1)

        self.textEdit_34 = QTextEdit(self.frame)
        self.textEdit_34.setObjectName(u"textEdit_34")
        self.textEdit_34.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_34.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_34, 10, 5, 1, 1)

        self.label_34 = QLabel(self.frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_34, 9, 5, 1, 1)

        self.textEdit_19 = QTextEdit(self.frame)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_19.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_19, 6, 4, 1, 1)

        self.textEdit_29 = QTextEdit(self.frame)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(248, 255, 255);")
        self.textEdit_29.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_29, 10, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_3, 1, 6, 1, 1)

        self.textEdit_14 = QTextEdit(self.frame)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_14.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_14, 4, 6, 1, 1)

        self.textEdit_16 = QTextEdit(self.frame)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_16.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_16, 6, 1, 1, 1)

        self.textEdit_4 = QTextEdit(self.frame)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_4.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_4, 2, 3, 1, 1)

        self.textEdit_30 = QTextEdit(self.frame)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_30.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_30, 10, 1, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(9,149,131);\n"
"background-color: rgb(238,255,254);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"font-size: 16px;\n"
"color: rgb(235, 0, 133);\n"
"background-color: rgb(255,240,249);\n"
"font: 11pt \"Segoe Script\";\n"
"padding-left: 50px;")

        self.gridLayout_2.addWidget(self.label_32, 9, 3, 1, 1)

        self.textEdit_10 = QTextEdit(self.frame)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_10.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_10, 4, 2, 1, 1)

        self.textEdit_22 = QTextEdit(self.frame)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(255, 253, 255);")
        self.textEdit_22.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_22, 8, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 10))
        self.menubar.setMinimumSize(QSize(0, 10))
        self.menubar.setMaximumSize(QSize(16777215, 1))
        self.menubar.setStyleSheet(u"")
        self.menu_Open = QMenu(self.menubar)
        self.menu_Open.setObjectName(u"menu_Open")
        self.menu_Open.setMinimumSize(QSize(0, 30))
        self.menu_Open.setStyleSheet(u"background-color: rgb(134, 176, 255);")
        self.menu_Open.setIcon(icon)
        self.menu_Open.setToolTipsVisible(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.toolBar.setIconSize(QSize(60, 60))
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        self.toolBar_2.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        self.toolBar_2.setIconSize(QSize(70, 70))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menu_Open.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.my_pill)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.add_pill)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.change_akk)
        self.toolBar_2.addAction(self.action)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.exit_)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u043e", None))
        self.my_pill.setText(QCoreApplication.translate("MainWindow", u"&\u041c\u043e\u0438 \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0430", None))
#if QT_CONFIG(tooltip)
        self.my_pill.setToolTip(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0438 \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.add_pill.setText(QCoreApplication.translate("MainWindow", u"&\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u043e", None))
#if QT_CONFIG(tooltip)
        self.add_pill.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.exit_.setText(QCoreApplication.translate("MainWindow", u"&\u0412\u044b\u0445\u043e\u0434", None))
        self.change_akk.setText(QCoreApplication.translate("MainWindow", u"&\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.change_akk.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0410\u041b\u0415\u041d\u0414\u0410\u0420\u042c", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.menu_Open.setTitle(QCoreApplication.translate("MainWindow", u"&Open", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

