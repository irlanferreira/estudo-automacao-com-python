import time, subprocess, playsound

cont = 10
while cont > 0:
    print(cont)
    time.sleep(1)
    cont = cont-1
subprocess.Popen(['start', 'alarm.wav'], shell=True)
