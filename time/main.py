import time

comeco = time.time()
print("Hello World")
time.sleep(1.37)
tempo = time.time()-comeco
print(f"O códigou levou {round(tempo, 2)} segundos para ser executado.")