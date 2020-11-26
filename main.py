import pyautogui
import pyperclip
import time

text = pyperclip.paste()

# X = pyautogui.confirm(buttons=["Exit"])
# if X == "Exit":
#     exit()


time_needed = int(
    pyautogui.prompt(
        """
        How much time(in seconds) do you need for
        1. Minimizing this dialouge 
        2. switching to the editor you want to simulate typing
        3. Placing the cursor at starting postion
    """
    )
)

time.sleep(time_needed)
pyautogui.write(text, interval=0.14)