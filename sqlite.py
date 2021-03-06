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
            
    def create(self):
        try:
            # cursor = self.conn.cursor()
            sql = """CREATE TABLE rasxod3 (
                                ID    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                SN_modem   TEXT NOT NULL,
                                IDN INT  NOT  NULL,
                                AVG_VOLUME REAL DEFAULT 0.0,
                                VOLUME     REAL  DEFAULT 0.0,
                                COUNTER    INT  DEFAULT 0,
                                TIME_T     INT NOT NULL
                                )"""
            self.conn.execute(sql)
            print("Created table rasxod")
        except Exception as e:
            print(e, type(e).__name__, __file__, e.__traceback__.tb_lineno)

#         INSERT INTO rasxod VALUES(2885,'860344049635593',1,0.0,0.0,0,1645632255,NULL,NULL);
#         INSERT INTO rasxod VALUES(2886,'860344049636385',1,0.0,0.0,0.020000000000000000416,1645632255,NULL,NULL);
#         INSERT INTO rasxod VALUES(2887,'860344049623227',1,0.0,0.0,0.010000000000000000208,1645632256,NULL,NULL);
#         INSERT INTO rasxod VALUES(2888,'868956047386655',1,0.0,0.0,334915.80999999999766,1645632256,NULL,NULL);

 
    
    def insert(self):
        
        cursor = self.conn.cursor()
        
        sql = "INSERT INTO rasxod3 VALUES('1','860344049635593',1,1,1,0,1645632255);"
        
        cursor.execute(sql)
        self.conn.commit()
        sql = "SELECT * FROM rasxod2;"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        for i in myresult:
            print(i)
        cursor.close()
