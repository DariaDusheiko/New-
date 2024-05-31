import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout
from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlTableModel
from enter1 import Ui_MainWindow
import pyautogui
from accoun import Data
from pill_data import Data_pil
from reg import Ui_MainWindow_1
from mane import Ui_MainWindow_3
from new_pill import Ui_MainWindow_4
from pills_frame import Ui_MainWindow_5
from ac_frame import Ui_MainWindow_6
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt, QTimer, QDateTime
import win10toast
from plyer import notification
import asyncio
import time
from datetime import datetime

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class WIPILLs(QMainWindow):
    def __init__(self):
        super(WIPILLs, self).__init__()
        weight_window, hight_window = pyautogui.size()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, weight_window, hight_window)

        self.ui.enter_pushButton.clicked.connect(self.enter_akk)
        self.ui.reg_pushButton.clicked.connect(self.registration)

        self.ui.pushButton.clicked.connect(self.relive)

        self.datetime_list = []
        self.desired_datetime = QDateTime()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showNotification)
        self.timer.start(1000)  # Проверяйте время каждую секунду

        self.acc = Data()
        self.pill = Data_pil()


    def showNotification(self, pill):
        current_datetime = QDateTime.currentDateTime()
        if current_datetime >= self.desired_datetime:
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("Время пришло!", "Время приема " + pill)
            self.desired_datetime = QDateTime()
            self.timer.start(1000)

    def relive(self):
        value_log = self.ui.login.text()

        if self.ui.login.text() == "":
            self.ui.label.setText("Введите логин и нажмите на кнопку еще раз.")
            self.ui.label.setStyleSheet(u"color: rgb(0, 0, 0)")
        else:
            peremenn = self.acc.pas_search(value_log)
            if peremenn != []:
                if (self.sending(peremenn[1], "Ваш пароль от аккаунта: " + peremenn[0])) == 1:
                    self.ui.label.setText("Письмо с паролем у Вас на почте.")
                    self.ui.label.setStyleSheet(u"color: rgb(0, 0, 0)")
                else:
                    self.ui.label.setText("Проблемы с почтой.")
                    self.ui.label.setStyleSheet(u"color: rgb(220, 20, 60)")
            else:
                self.ui.label.setText("Неправильный логин.")
                self.ui.label.setStyleSheet(u"color: rgb(220, 20, 60)")

    def enter_akk(self):
        value_log = self.ui.login.text()
        value_pass = self.ui.password.text()

        if self.acc.search(value_log, value_pass):
            self.mainpage = QtWidgets.QMainWindow()
            self.many = Ui_MainWindow_3()
            self.many.setupUi(self.mainpage, weight_window, hight_window)

            self.prepare_for_close_enter()
            self.mainpage.show()

            self.many.change_akk.triggered.connect(self.ac)
            self.many.exit_.triggered.connect(self.exity)
            self.many.add_pill.triggered.connect(self.new_pill)
            self.many.my_pill.triggered.connect(self.show_pill)

        else:
            self.ui.label.setStyleSheet(u"color: rgb(220, 20, 60)")
            print("NO")

    def open_mane(self):
        self.new.hide()
        self.mainpage.show()
        self.data_of_ac.hide()
        self.new.hide()

        self.many.change_akk.triggered.connect(self.ac)
        self.many.exit_.triggered.connect(self.exity)
        self.many.add_pill.triggered.connect(self.new_pill)
        self.many.my_pill.triggered.connect(self.show_pill)

    def registration(self):
        self.regista = QtWidgets.QMainWindow()
        self.regy = Ui_MainWindow_1()
        weight_window, hight_window = pyautogui.size()
        self.regy.setupUi(self.regista, weight_window, hight_window)

        self.regy.pushButton.clicked.connect(self.zaregistrate)

        self.prepare_for_close_enter()
        self.regista.show()


    def prepare_for_close_enter(self):
        self.ui.password.clear()
        self.ui.login.clear()
        self.ui.label.setStyleSheet(u"color: rgb(250, 250, 250)")
        window.hide()

    def zaregistrate(self):
        value_log = self.regy.login_lineEdit.text()
        value_pass = self.regy.password_lineEdit_2.text()
        value_repeat_pass = self.regy.repeatpassword_lineEdit_3.text()
        to_email = self.regy.lineEdit.text()

        peremenn = self.acc.pas_search(value_log)

        if peremenn != []:
            self.regy.label.setText("Данный логин уже существует.")
            self.regy.label.setStyleSheet(u"color: (0, 0, 0); border: none;")

        if value_repeat_pass == value_pass:
            if " " not in value_pass:
                self.regy.label.setText("Данная почта некорректна, введите другую.")
                self.regy.label.setStyleSheet(u"color: (0, 0, 0); border: none;")
                if to_email != "":
                    message = 'Вы зарегестрировались в приложении WIPPILs!!!!'

                    if (self.sending(to_email, message)) == 1:
                        self.acc.add_new_account_query(value_log, value_pass, to_email)
                        window.show()
                        self.regista.hide()
                    else:
                        self.regy.label.setText("Данная почта некорректна, введите другую.")
                        self.regy.label.setStyleSheet(u"color: (0, 0, 0); border: none;")
                else:
                    self.regy.label.setText("Данная почта некорректна, введите другую.")
                    self.regy.label.setStyleSheet(u"color: (0, 0, 0); border: none;")
            else:
                self.regy.label.setText("Пароль не может содержать пробелы.")
                self.regy.label.setStyleSheet(u"color: (0, 0, 0); border: none;")
        else:
            self.regy.label.setText("Пароли не совпадают, повторите ввод.")
            self.regy.label.setStyleSheet(u"color: (255, 255, 255); border: none;")

            

    def sending(self, to_email, message):
        msg = MIMEMultipart()

        msg.attach(MIMEText(message, 'plain'))
        msg['From'] = "daria.dusheiko@yandex.ru"
        msg['Subject'] = 'Information of your account in WIPPILs'

        try:
            server = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)
            server.starttls()
            server.login("daria.dusheiko@yandex.ru", "DariaDusheiko13")
            server.sendmail("daria.dusheiko@yandex.ru", to_email, msg.as_string())
            server.quit()
            return 1

        except Exception as err:
            # print(f"{type(err).__name__} was raised: {err}")
            return 0

    def exity(self):
        window.show()
        self.mainpage.hide()

    def new_pill(self):
        self.new = QtWidgets.QMainWindow()
        self.new_pilly = Ui_MainWindow_4()
        weight_window, hight_window = pyautogui.size()
        self.new_pilly.setupUi(self.new, weight_window, hight_window)

        self.new_pilly.action_change_akk.triggered.connect(self.ac)
        self.new_pilly.action_exit.triggered.connect(self.exity)
        self.new_pilly.action_add_pill.triggered.connect(self.open_mane)
        self.new_pilly.my_pill.triggered.connect(self.show_pill)

        self.new_pilly.pushButton.clicked.connect(self.add_pill)

        self.new.show()
        self.mainpage.hide()
        self.data_of_pill.hide()

    def add_pill(self):
        name = self.new_pilly.lineEdit.text()
        time = self.new_pilly.comboBox.currentText()
        rep = self.new_pilly.lineEdit_2.text()

        self.pill.add_new_account_query(name, time, rep)
        self.open_mane()

    def show_pill(self):
        self.data_of_pill = QtWidgets.QMainWindow()
        self.pills_data = Ui_MainWindow_5()
        weight_window, hight_window = pyautogui.size()
        self.pills_data.setupUi(self.data_of_pill, weight_window, hight_window)

        self.pills_data.action_change_akk.triggered.connect(self.ac)
        self.pills_data.action_exit.triggered.connect(self.exity)
        self.pills_data.action_add_pill.triggered.connect(self.new_pill)
        self.pills_data.my_pill.triggered.connect(self.open_mane)
        self.pills_data.pushButton.clicked.connect(self.delete)

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("server.db")
        db.open()

        self.model = QSqlTableModel(self)
        self.model.setQuery("select * from pills", db)
        self.pills_data.tableView.setModel(self.model)

        self.data_of_pill.show()
        self.new.hide()
        self.mainpage.hide()

    def delete(self):
        index = self.pills_data.tableView.selectedIndexes()[0]
        id = str(self.pills_data.tableView.model().data(index))

        self.pill.delete_account_query(id)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("server.db")
        db.open()

        self.model = QSqlTableModel(self)
        self.model.setQuery("select * from pills", db)
        self.pills_data.tableView.setModel(self.model)

    def ac(self):
        self.data_of_ac = QtWidgets.QMainWindow()
        self.acc_tab = Ui_MainWindow_6()
        weight_window, hight_window = pyautogui.size()
        self.acc_tab.setupUi(self.data_of_ac, weight_window, hight_window)

        self.acc_tab.action_change_akk.triggered.connect(self.open_mane)
        self.acc_tab.action_exit.triggered.connect(self.exity)
        self.acc_tab.action_add_pill.triggered.connect(self.new_pill)
        self.acc_tab.my_pill.triggered.connect(self.show_pill)
        self.acc_tab.pushButton.clicked.connect(self.open_mane)

        # db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        # db.setDatabaseName("server.db")
        # db.open()
        #
        # self.model = QSqlTableModel(self)
        # self.model.setQuery("select * from pills", db)
        # self.pills_data.tableView.setModel(self.model)

        self.data_of_ac.show()
        self.new.hide()
        self.mainpage.hide()




if __name__ == "__main__":
    weight_window, hight_window = pyautogui.size()
    app = QApplication(sys.argv)
    window = WIPILLs()
    window.show()

    # while True:
    #     current_dt = datetime.now()
    #     for dt in window.datetime_list:
    #         if current_dt >= dt:
    #             window.showNotification(f"Время пришло для {dt}")
    #
    #     app.processEvents()

    sys.exit(app.exec())