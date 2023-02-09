import sqlite3
path = ".\\banco\\agenda.db"
def conect(p):
    try:
        con = sqlite3.connect(p)
    except sqlite3.Error as ex:
        print(ex)
    return con

def query(c, sql):
    cursor = c.cursor()
    try:
        cursor.execute(sql)
    except sqlite3.Error as ex:
        print(ex)

conection = conect(path)
vsql = ""
query(conection, vsql)