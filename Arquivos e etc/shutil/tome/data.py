import time
import datetime
#while True:
    #data = datetime.datetime.now()
    #print(f"{data.hour}:{'0' if data.minute < 10 else ''}{data.minute}:{'0' if data.second < 10 else ''}{data.second}")
    #time.sleep(1)
nasc = datetime.datetime(2005, 5, 4)
print(nasc.strftime("%A"))