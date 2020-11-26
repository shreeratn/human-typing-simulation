import pyautogui
import pyperclip
import time

text = pyperclip.paste()

time.sleep(10)
pyautogui.write(text, interval=0.20)

X = pyautogui.confirm(buttons=["Exit"])

if X == "Exit":
    exit()