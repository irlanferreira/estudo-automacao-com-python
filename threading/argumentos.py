import threading
import time


def printarnomes(nome1, nome2):
    time.sleep(2)
    print(f"{nome1} e {nome2}")


thread = threading.Thread(target=printarnomes, args=['kipilipitiki', 'academi'])
thread.start()
