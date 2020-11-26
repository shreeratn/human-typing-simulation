import subprocess
import keyboard

p = subprocess.Popen(['python','main.py'])

key_stroke = keyboard.read_hotkey(suppress=True)
if key_stroke == 'ctrl+esc':
    p.terminate()