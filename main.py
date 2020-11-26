import pyautogui
import pyperclip
import time

text = pyperclip.paste()
# for e in text:
#     pyautogui.typewrite(e)
#     time.sleep(.1) #change this value to whatever you mean by "a quick manner"

pyautogui.write("Hello world!", interval=0.25)
