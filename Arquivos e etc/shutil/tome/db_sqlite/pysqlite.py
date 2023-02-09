import sqlite3
def conectar(p):
    try:
        con = sqlite3.connect(p)
    except sqlite3.Error as ex:
        print(ex)
    return con
def criarTabela(con, sql):
    cur = con.cursor()
    try:
        cur.execute(sql)
    except sqlite3.Error as ex:
        print(ex)
def inserir(con, sql):
    try:
        c = con.cursor()
        c.execute(sql)
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)
def apagarDados(c, sql):
    cursor =  c.cursor()
    try:
        cursor.execute(sql)
        c.commit()
    except sqlite3.Error as ex:
        print(ex)
def atualizarDados(con, sql):
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
    except sqlite3.Error as ex:
        print(ex)
def consulta(con, sql):
    try:
        cursor = con.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except sqlite3.Error as ex:
        print(ex)
conexao = conectar(".\\banco\\agenda.db")
inserir(conexao, f"INSERT INTO tb_contatos(nome, email, telefone) VALUES ('{input('Nome: ')}', '{input('Email: ')}', '{input('Telefone: ')}')")