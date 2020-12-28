import os
import subprocess
import tkinter as tk
import shutil
from time import sleep

catalinaHome = os.getenv('CATALINA_HOME')
pathToBin = os.getenv('CATALINA_HOME') + '\\bin\\'
pathToWebApps = os.getenv('CATALINA_HOME') + '\\webapps\\'
source = 'C:\\projects\\spring_course\\spring_course_mvc\\target\\spring_course_mvc.war'

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=400)
canvas1.pack()
# Entry field
entry1 = tk.Entry(root, width=70)
canvas1.create_window(300, 50, window=entry1)
entry1.insert(0, source)


def start():
    global source
    source = entry1.get()
    shutil.copy2(source, pathToWebApps)
    sleep(1)
    dispatcher(True)


def stop():
    dispatcher(False)


def dispatcher(operation):
    path = pathToBin
    if operation is True:
        path += 'startup.bat'
    else:
        path += 'shutdown.bat'
    subprocess.call(path)


# Buttons
button1 = tk.Button(root, width=20, text='Start Server', command=start, bg='green', fg='white')
button2 = tk.Button(root, width=20, text='Stop Server', command=stop, bg='green', fg='white')
canvas1.create_window(200, 130, window=button1)
canvas1.create_window(400, 130, window=button2)

# Start form running
root.mainloop()
