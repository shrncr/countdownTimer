#from draw import drawTime
#from guiPractice2 import App
import time
from tkinter import *
from tkinter import messagebox
t = 1
def countDown():
    global t
    root = Tk()

    root.geometry = ("300x250")

    root.title("")

    second=StringVar()
    second.set("10")

    secondEntry= Label(root, width=3, font=("Arial",18,""),textvariable=second)
    secondEntry.place(x=180,y=20)
    
    
    t=int(second.get())

    while t> 0:
        t -= 1
        second.set("{0:2d}".format(t))
        root.update()
        time.sleep(1)

    root.mainloop()
    print("meowmeowmeow")
countDown()