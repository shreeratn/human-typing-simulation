import pyautogui
import pyperclip
import time

text = pyperclip.paste()

# X = pyautogui.confirm(buttons=["Exit"])

# if X == "Exit":
#     exit()

time.sleep(5)
pyautogui.write(text, interval=0.14)