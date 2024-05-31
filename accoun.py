import sqlite3

# t = 0
# user_login = input("Login: ")
# user_password = input("Password: ")
#
# sql.execute("SELECT login FROM users")
# if sql.fetchall() is None:
#     sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
#     db.commit()
#
#     print("Zar!")
# else:
#     print("it is!")
#     sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
#     db.commit()
#
#     for value in sql.execute("SELECT * FROM users"):
#         if (value[0] == "123"):
#             print(value[1])

from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_account()

    def create_account(self):
        db = sqlite3.connect("server.db")
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER primary key AUTOINCREMENT,
            login TEXT,
            password TEXT,
            email TEXT
            )""")

        db.commit()
        return True

    # def execute_query_with_params(self, sql_query, query_values=None):
    #     query = QtSql.QSqlQuery()
    #     query.prepare(sql_query)
    #
    #     if query_values is not None:
    #         for query_value in query_values:
    #             query.addBindValue(query_value)
    #
    #     query.exec()
    #     return query

    def add_new_account_query(self, login, password, email):
        # sql_query = "INSERT INTO accounts (Login, Password) VALUES (?, ?)"
        # self.execute_query_with_params(sql_query, [login, password])
        db = sqlite3.connect("server.db")
        sql = db.cursor()
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (None, login, password, email))
        db.commit()

    # def update_account_query(self, login, password, id):
    #     sql_query = "UPDATE accounts SET Login=? Password=? WHERE ID=?"
    #     self.execute_query_with_params(sql_query, [login, password, id])
    #
    # def delete_account_query(self, id):
    #     sql_query = "DELETE FROM accounts WHERE ID=?"
    #     self.execute_query_with_params(sql_query, [id])

    def search(self, login, pessword):
        db = sqlite3.connect("server.db")
        sql = db.cursor()

        for value in sql.execute("SELECT * FROM users"):
            if value[1] == login and value[2] == pessword:
                return True
        return False

    def pas_search(self, login):
        db = sqlite3.connect("server.db")
        sql = db.cursor()

        for value in sql.execute("SELECT * FROM users"):
            if value[1] == login and len(value) == 4:
                return [value[2], value[3]]
        return []