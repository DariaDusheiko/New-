from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_account()

    def create_account(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('Accounts_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "click cancel to exit", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS accounts (ID integer primary key AUTOINCREMENT, Login VARCHAR(20),"
                   "Password VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_account_query(self, login, password):
        sql_query = "INSERT INTO accounts (Login, Password) VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [login, password])

    def update_account_query(self, login, password, id):
        sql_query = "UPDATE accounts SET Login=? Password=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [login, password, id])

    def delete_account_query(self, id):
        sql_query = "DELETE FROM accounts WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM({column}) FROM accounts"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0))

        return '0'

    def total_balance(self, log):
        return self.get_total(column="ID", filter="Login", value=log)

    def search_query_with_params(self, log=None, pas=None):
        sql_query = "EXISTS(SELECT ID FROM accounts WHERE Login = ? AND Password = ?)"
        query_values = [log, pas]

        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def search(self, login, pessword):
        query = QtSql.QSqlQuery()

        for value in query.exec("SELECT * FROM accounts"):
            print(value)


        # if query_values is not None:
        #     for query_value in query_values:
        #         print(query_value)
        #         if log == query_value:
        #             return True