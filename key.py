import keyboard

key_stroke = keyboard.read_hotkey(suppress=True)
print(key_stroke)