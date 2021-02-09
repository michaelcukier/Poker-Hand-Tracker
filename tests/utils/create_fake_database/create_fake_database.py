import sqlite3
import os


class CreateFakeDatabase:

    def __init__(self, db_name, table_name, columns_labels, data):
        self._db_name = db_name
        self.conn = sqlite3.connect('./' + db_name + '.db')

        _columns = ''.join([str(c) + ' text, ' for c in columns_labels])[:-2]
        self.exec_query("CREATE TABLE " + table_name + " (" + _columns + ")")

        for row_data in data:
            _row_data = ''.join(['"' + str(d) + '", ' for d in row_data])[:-2]
            q = 'INSERT INTO ' + table_name + "(" + ', '.join(columns_labels) + ") VALUES (" + _row_data + ")"
            self.exec_query(q)

    def exec_query(self, query):
        try:
            with self.conn:
                cur = self.conn.cursor()
                cur.execute(query)
                return True
        except Exception as why:
            return False

    def destroy(self):
        os.remove('./' + self._db_name + '.db')

