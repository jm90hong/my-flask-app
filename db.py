import pymysql

def get_db_connection():
    return pymysql.connect(
        host='52.78.143.170',
        port=3306,
        user='jm',
        password='123qwe!',
        database='my_db'
    )