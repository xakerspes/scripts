import sqlite3, time
import numpy as np
class db:

    def __init__(self, connect: bool = True) -> None:
        self.conn = None
        # self.cursor = None
        # self.HOST = "localhost"
        # self.USER = "root"
        # self.PASSWORD = ""
        self.DB_NAME = "db_modem"
        self.TABLE_NAME = "rasxod"
        self.SQL_REQ_DEFAULT = "SELECT * from {} ORDER BY ID DESC LIMIT 0,7".format(self.TABLE_NAME)
        if connect is True:
            self.connect()
            self.cursor = self.conn.cursor()

    def connect(self):
        """"""
        try:
            if self.conn is None:
                self.conn = sqlite3.connect('db_modem.db')
                print("SqlLite is connected")
        except Exception as e:
            print("SqlLite is already connected", e)
            print(
                type(e).__name__,  # TypeError
                e.__traceback__.tb_lineno
            )

    
    
    def select(self, limit: int = 100):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM rasxod " + "ORDER BY TIME_T DESC LIMIT {},{}".format(0, limit)
            cursor.execute(sql)
            res = cursor.fetchall()
            global t_global
            t_global = res[0]
            for i in res:
                print(i)
        except Exception as e:
            print("SqlLite is already connected", e)
            print(
                type(e).__name__,  # TypeError
                e.__traceback__.tb_lineno
            )
