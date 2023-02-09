import sqlite3, time
def conectar(p):
    try:
        con = sqlite3.connect(p)
        return con
    except sqlite3.Error as ex:
        print(ex)
def registrar(con, dados):
    cursor = con.cursor()
    try:
        cursor.execute(f"INSERT INTO tb_contatos (nome, email, telefone) VALUES ('{dados[0]}', '{dados[1]}', '{dados[2]}')")
        con.commit()
    except sqlite3.Error as ex:
        print(ex)
def deletar(con, id):
    cursor = con.cursor()
    try:
        cursor.execute(f"DELETE FROM tb_contatos WHERE id = {id}")
        con.commit()
    except sqlite3.Error as ex:
        print(ex)
def atualizar(con, id):
    cursor = con.cursor()
    try:
        cursor.execute(f"UPDATE tb_contatos SET nome = '{input('Novo Nome: ')}', email = '{input('Novo Email: ')}', telefone = '{input('Novo Telefone: ')}' where id = {id}")
        con.commit()
    except sqlite3.Error as ex:
        print(ex)
def consultarId(con, i):
    cursor = con.cursor()
    try:
        cursor.execute(f"SELECT * FROM tb_contatos WHERE id = ?", [i])
        return cursor.fetchall()
    except sqlite3.Error as ex:
        print(ex)
def consultarNomes(con):
    cursor = con.cursor()
    try:
        cursor.execute(f"SELECT * FROM tb_contatos")
        return cursor.fetchall()
    except sqlite3.Error as ex:
        print(ex)
conexao = conectar("..\\banco\\agenda.db")
while True:
    print(f"{'='*30}\n1 - Inserir Novo Registro\n2 - Deletar Registro\n3 - Atualizar Registro\n4 - Consultar ID\n5 - Consultar Nomes\n6 - Sair\n{'='*30}")
    op = input("O que você quer fazer?: ")
    match op:
        case '1':
            while True:
                dadosadicionar = [input("Nome: "), input("Email: "), input("Telefone: ")]
                registrar(conexao, dadosadicionar)
                print("Dados registrados com sucesso!")
                time.sleep(1.5)
                break
        case '2':
            while True:
                idremover = input("Qual registro você deseja remover? (Insira o id): ")
                deletar(conexao, idremover)
                print(f"Usuário deletado com sucesso!")
                time.sleep(1.5)
                break
        case '3':
            while True:
                idatualizar = input("Qual registro você deseja atualizar? (insira o id): ")
                atualizar(conexao, idatualizar)
                print("Registro atualizado com sucesso!")
                time.sleep(1.5)
                break
        case '4':
            while True:
                idconsult = input("Qual id você deseja consultar?")
                dados = consultarId(conexao, idconsult)[0]
                print(f"{'='*30}\nNome: {dados[1]}\nEmail: {dados[2]}\nTelefone: {dados[3]}\n{'='*30}")
                time.sleep(1.5)
                break
        case '5':
            while True:
                dados = consultarNomes(conexao)
                for d in dados:
                    print(f"{'=' * 30}\nNome: {d[1]}\nEmail: {d[2]}\nTelefone: {d[3]}\n{'=' * 30}")
                break
        case '6':
            break
        case _:
            print(f"Valor '{op}' inválido.")
            time.sleep(1.5)