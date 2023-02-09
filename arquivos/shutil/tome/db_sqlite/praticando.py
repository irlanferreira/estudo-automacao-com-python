import sqlite3
def conectar(p):
    try:
        con = sqlite3.connect(p)

    except sqlite3.Error as ex:
        print(ex)
    return con

def consulta(con, sql):
    try:
        cursor = con.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except sqlite3.Error as ex:
        print(ex)

conex = conectar(".\\banco\\agenda.db")
nome = input("Qual nome você vasculhar?: ")
registros = consulta(conex, "SELECT * from tb_contatos")
for r in registros:
    if nome in r:
        print(f"O nome {nome} está registrado no registro de identificação {r[0]}.")