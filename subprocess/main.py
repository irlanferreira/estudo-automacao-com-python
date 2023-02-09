import subprocess
import time

proc = subprocess.Popen(['calibre.exe', 'C:\\Users\\adm\\Downloads\\Apologia de Sócrates.epub'])
while True:
    print(proc.poll())
    time.sleep(2)
