import pyautogui
import time
text="what i want to type"
for e in text: 
    pyautogui.typewrite(e)
    time.sleep(.1) #change this value to whatever you mean by "a quick manner"