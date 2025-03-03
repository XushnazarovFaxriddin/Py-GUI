from tkinter import *
from tkinter.messagebox import *

random_colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "black", "white"]


def changeColor(btn: Button, color: str):
    btn.config(bg=color)
    
def changeRandomColor(btn: Button):
    import random
    changeColor(btn, random.choice(random_colors))


def sayHello(window: Tk, btn: Button):
    changeRandomColor(btn)
    showinfo("Hello", f"Hello from button {btn['text']} in window {window.title()}")
    