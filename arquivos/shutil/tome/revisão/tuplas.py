from random import randint
numeros = (int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")),int(input("Digite um número: ")))
print(f"Os números digitados foram {numeros}.")
print(f"O número 9 apareceu {numeros.count(9)} vezes.")
if numeros.count(3) >= 0:
    print(f"O número 3 foi digitado na posição {numeros.index(3)}.")
else:
    print("O número 3 não foi digitado nenhuma vez.")
print("Os números pares são:")
for n in numeros:
    if n % 2 == 0:
        print(n)
