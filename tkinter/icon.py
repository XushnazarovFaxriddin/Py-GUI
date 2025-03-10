from tkinter import *

win = Tk()
win.title("Bukhara State University")
win.geometry("300x400")

icon = PhotoImage(file="src/buxdu-logo.png")
win.iconphoto(False, icon)

win.minsize(200, 200)
win.maxsize(600, 800)

win['bg'] = 'green'
win.attributes("-alpha", 0.9)

win.mainloop()
