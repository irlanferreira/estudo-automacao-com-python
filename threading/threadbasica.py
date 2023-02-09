import threading, time

print('Começo')
def soneca():
    time.sleep(5)
    print('wake up its time to school')
thread = threading.Thread(target=soneca)
thread.start()
print('Fim.')
