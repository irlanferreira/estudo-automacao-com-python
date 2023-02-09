import shelve
import datetime
sharq = shelve.open('dados')
try:
    sharq['registros']
except:
    sharq['registros'] = []
    print(f"Não foi encontrados registros salvos. Nova base de registros criada.")
while True:
    res = int(input(f"O que deseja fazer?\n\n1.Registrar\n2.Ver Registros\n3.Sair\n:"))
    match res:
        case 1:
            nome = input('Nome: ')
            agora = datetime.datetime.now()
            hora = f"{0 if agora.hour < 10 else ''}{agora.hour}:{0 if agora.minute < 10 else ''}{agora.minute}"
            dia = f'{0 if agora.day < 10 else ""}{agora.day}'
            mes = f'{0 if agora.month < 10 else ""}{agora.month}'
            ano = f'{0 if agora.year < 10 else ""}{agora.year}'
            horario = f"{dia}/{mes}/{ano} - {hora}"
            dados = [nome, horario]
            lista = sharq['registros']
            lista.append(dados)
            sharq['registros'] = lista
            print(f'{nome} registrado com sucesso.\n\n')
        case 2:
            for d in sharq['registros']:
                print(f"Nome: {d[0]}\nHorário de Registro: {d[1]}\n\n")
        case 3:
            break
