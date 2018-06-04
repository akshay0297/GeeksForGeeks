import pyperclip as pc
import webbrowser as wb
import time

print ("Just Copy a URL and RUN this script to open it !")

address = pc.paste()
time.sleep(1)
wb.open(address)
