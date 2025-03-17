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

btn = Button(win, text="Click me", width=20, height=2)
btn.pack(pady=10)

lbl = Label(win, text="0", font=("Arial", 20))
lbl.pack(pady=10)

def increment():
    lbl.config(text=str(int(lbl["text"]) + 1))

btn.config(command=increment)

win.mainloop()

