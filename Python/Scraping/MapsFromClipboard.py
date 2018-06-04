import pyperclip as pc
import webbrowser as wb
import time

print ("Just copy an Address and RUN this script to open it in MAP IT !")

address = pc.paste()
time.sleep(1)
wb.open('https://www.google.com/maps/place/' + address)
