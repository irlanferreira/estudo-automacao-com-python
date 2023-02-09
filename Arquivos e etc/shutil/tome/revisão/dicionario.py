nome = str(input("Nome: "))
media = float(input("Média: "))
aluno = {'nome': nome, 'media': media, 'situacao': "Aprovado" if media >=6 else "Reprovado"}
for k, v in aluno.items():
    print(f"{k}: {v}")