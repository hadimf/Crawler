import sqlite3


class Read:
    @staticmethod
    def getLinksFromTable(dbName, tableName):
        queryRead = f"SELECT url FROM '{tableName}'"
        with sqlite3.connect(dbName) as conn:
            cursor = conn.cursor()
            cursor.execute(queryRead)
            count = 0
            while count < 10:
                res = cursor.fetchone()
                if not res:
                    break
                link = res[0]
                count += 1
                yield link
