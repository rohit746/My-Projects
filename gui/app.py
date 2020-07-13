import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f :
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("executables",
                                                      "*.exe*"),
                                                     ("all files",
                                                      "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        Label = tk.Label(frame, text=app , bg="gray")
        Label.pack()
        
    for app in apps:
        os.startfile(app)
        
def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, width=600, height=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="White", bg="#263D42", command=addApp)

openFile.pack()
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="White", bg="#263D42", command=runApps)

for app in apps:
    label = tk.Label(frame, test=app)
    label.pack()
runApps.pack()
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
