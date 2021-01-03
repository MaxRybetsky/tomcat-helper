import os
import subprocess
import tkinter as tk
import shutil
from time import sleep
from tkinter import messagebox

# TomCat home directory
catalinaHome = os.getenv('CATALINA_HOME')
# TomCat binary files
pathToBin = os.getenv('CATALINA_HOME') + '\\bin\\'
# Path to web applications
pathToWebApps = os.getenv('CATALINA_HOME') + '\\webapps\\'
# Path to source code
source = 'C:\\projects\\spring_course\\spring_course_mvc\\target\\spring_course_mvc.war'
# Is server ON
serverOn = False

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=400)
canvas1.pack()
# Entry field
entry1 = tk.Entry(root, width=70)
canvas1.create_window(300, 50, window=entry1)
entry1.insert(0, source)


def start():
    if serverOn:
        return
    global source
    source = entry1.get()
    shutil.copy2(source, pathToWebApps)
    sleep(1)
    dispatcher(True)


def stop():
    if not serverOn:
        return
    dispatcher(False)


def dispatcher(operation):
    global serverOn
    path = pathToBin
    if operation is True:
        path += 'startup.bat'
        serverOn = True
    else:
        path += 'shutdown.bat'
        serverOn = False
    subprocess.call(path)


def restart_full():
    if serverOn:
        stop()
    res = build_new_war()
    if res == 0:
        start()
    else:
        messagebox.showerror('Error!!!',
                             'There are errors in source code. Check it one more time.')


def build_new_war(destination=source):
    path = get_root_dir(destination)
    return os.system("mvn -f " + path + " clean package")


def get_root_dir(path, level=2):
    dir_elements = path.split("\\")
    root_dir = ""
    for i in range(len(dir_elements) - 2):
        root_dir += dir_elements[i] + "\\"
    return root_dir


# Buttons
# Start server button
startButton = tk.Button(root, width=20, text='Start Server', command=start,
                        bg='green', fg='white')
# Stop server button
stopButton = tk.Button(root, width=20, text='Stop Server', command=stop,
                       bg='green', fg='white')
# Build war package and restart server button
buildAndRestartButton = tk.Button(root, width=20, text='Build and Restart Server', command=restart_full,
                                  bg='green', fg='white')

# Move buttons to canvas
canvas1.create_window(100, 130, window=buildAndRestartButton)
canvas1.create_window(300, 130, window=startButton)
canvas1.create_window(500, 130, window=stopButton)

# Start form running
root.mainloop()
