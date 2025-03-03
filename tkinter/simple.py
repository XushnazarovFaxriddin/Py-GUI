from tkinter import *
import ux
win = Tk()
win.geometry("600x800")


btns = [Button(
    win, 
    text=str(i), 
    width=15, 
    height=2
    ) for i in range(1, 5)]

for i, btn in enumerate(btns):
    btn.pack(pady=10)
    btns[i].config(command=lambda b=btn: ux.sayHello(win, b))

    
win.mainloop()
