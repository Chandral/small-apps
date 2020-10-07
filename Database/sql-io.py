import mysql.connector
from mysql.connector.errors import InterfaceError, DatabaseError


class DBHandler:

    def __init__(self, config):
        self.cur = None
        self.conn = None
        self.config = config

    def connect_db(self):
        if not self.conn:
            self.conn = mysql.connector.connect(
                host=self.config['db_host'],
                user=self.config['db_user'],
                passwd=self.config['db_passwd'],
                database=self.config['db_name']
            )
            self.cur = self.conn.cursor()
        
    def execute_sql(self, sql, close, return_result=False):
        try:
            self.connect_db()
            self.cur.execute(sql)
            if return_result:
                result = self.cur.fetchall()
            else:
                self.conn.commit()
                result = []
            if close:
                self.cur.close()
                self.conn.close()
                self.cur, self.conn = None, None
            return result
        except (InterfaceError, DatabaseError) as e:
            return f"{e}"

    def get_column_names(self, table_name, close_connection=True):
        sql = f"SHOW COLUMNS FROM {table_name}"
        result = self.execute_sql(sql, close_connection, return_result=True)
        return [column_info[0] for column_info in result] if isinstance(result, list) else result

    def insert(self, table_name, data, close_connection=True):
        columns, values = ",".join(data.keys()), ",".join([f"'{i}'" for i in data.values()])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        self.execute_sql(sql, close_connection)

    def update(self, table_name, data, where_condition, close_connection=True):
        update_string = ",".join([f"{db_column}='{db_value}'" for db_column, db_value in data.items()])
        sql = f"UPDATE {table_name} SET {update_string} WHERE {where_condition};"
        self.execute_sql(sql, close_connection)

    def delete(self, table_name, where_condition, close_connection=True):
        sql = f"DELETE FROM {table_name} WHERE {where_condition};"
        self.execute_sql(sql, close_connection)

    def fetch(self, columns, table_name, where_condition="", close_connection=True):
        columns = ",".join(columns) if isinstance(columns, list) or isinstance(columns, tuple) else columns
        sql = f"SELECT {columns} FROM {table_name};" if where_condition else f"SELECT {columns} FROM {table_name} WHERE {where_condition};"
        return self.execute_sql(sql, close_connection, return_result=True)


config_data = {
    'db_host': '',
    'db_user': '',
    'db_passwd': '',
    'db_name': ''
}

yoma_db = DBHandler(config_data)
cs = yoma_db.get_column_names("sitemaster")
print(cs)
a = ['smSiteID']
b = yoma_db.fetch(a, 'sitemaster', 'smSiteID="1"')
print(b)