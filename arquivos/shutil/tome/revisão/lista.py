galera = []
dado = []
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    galera.append(dado[:])
    if len(galera) == 0:
        max = min = dado[1]
    dado.clear()
    continuar = input("Deseja continuar? S/N: ")
    if continuar in "N/n":
        break
for p in galera:
    if p[1] > max:
        max = p[1]
    if p[1] < min:
        min = p[1]
print(f"Você inseriu {len(galera)} pessoas.")
print(f"O maior peso foi {max}, de ", end='')
for p in galera:
    if p[1] == max:
        print(f"{p[0]}", end='')
print()
print(f"O menor peso foi {min}, de " , end='')
for p in galera:
    if p[1] == min:
        print(f"{p[0]}", end='')
print()