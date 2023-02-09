import random
numsorteado = random.randint(1,10)
tentativas = 5
while True:
    res = int(input("Você tem 5 Tentativas.\nQual o número sorteado?: "))
    if res == numsorteado:
        print("Acertou!")
        break
    else:
        tentativas-=1
        print(f"Errou :(\n{tentativas} tentativas restantes.")
    if tentativas <= 0:
        print("Fim de jogo! Você perdeu.")
        break