import sqlite3


class Create:
    @staticmethod
    def createTableLinks(dbName, tableName):
        connection = sqlite3.connect(dbName)
        cursor = connection.cursor()
        try:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS '{tableName}' (url TEXT)")
            connection.commit()
        except sqlite3.OperationalError as e:
            print("Error:", e)
        finally:
            connection.close()

    @staticmethod
    def createTableData(dbName, tableName):
        connection = sqlite3.connect(dbName)
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS '{tableName}' (url TEXT, titles TEXT, body TEXT, navigation TEXT, photoPath TEXT)")
            connection.commit()
        except sqlite3.OperationalError as e:
            print("Error:", e)
        finally:
            connection.close()
