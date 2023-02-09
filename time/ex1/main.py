import time
rodada = 0
while True:
    rodada +=1
    start = time.time()
    input(f'Pressione ENTER para encerrar a rodada {rodada}')
    print(f"A rodada {rodada} durou {round(time.time()-start, 2)} segundos.")
