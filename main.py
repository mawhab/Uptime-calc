import requests
import tkinter
import datetime
import time

url = "https://www.bing.com/"
tim = 5
inter = True


while inter:
    time.sleep(4)
    try:
        x = requests.get(url, timeout=tim)
    except:
        inter = False

if inter is False:
    now = datetime.datetime.now()
    curr = now.strftime("%H:%M:%S")
    print(curr)