import subprocess

# p = subprocess.Popen(['python','main.py'])

subprocess.run("python main.py & python key.py", shell=False)
