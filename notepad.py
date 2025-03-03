import tkinter as tk
from tkinter import filedialog, messagebox
import os

class ModernNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Notepad")
        self.root.geometry("900x600")
        
        self.filename = None
        
        # Create text widget
        self.text_area = tk.Text(self.root, wrap="word", undo=True, font=("Consolas", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Add Scrollbar
        self.scrollbar = tk.Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create Menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.create_menus()
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", anchor="w")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind shortcuts
        self.bind_shortcuts()
    
    def create_menus(self):
        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app, accelerator="Ctrl+Q")
        
        # Edit Menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Find & Replace", command=self.find_and_replace, accelerator="Ctrl+F")
        
        # Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda _: self.new_file())
        self.root.bind("<Control-o>", lambda _: self.open_file())
        self.root.bind("<Control-s>", lambda _: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda _: self.save_as())
        self.root.bind("<Control-q>", lambda _: self.exit_app())
        self.root.bind("<Control-x>", lambda _: self.cut_text())
        self.root.bind("<Control-c>", lambda _: self.copy_text())
        self.root.bind("<Control-v>", lambda _: self.paste_text())
        self.root.bind("<Control-f>", lambda _: self.find_and_replace())
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.status_bar.config(text="New File")
    
    def open_file(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            with open(self.filename, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
            self.status_bar.config(text=f"Opened: {os.path.basename(self.filename)}")
    
    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(text=f"Saved: {os.path.basename(self.filename)}")
        else:
            self.save_as()
    
    def save_as(self):
        self.filename = filedialog.asksaveasfilename()
        if self.filename:
            self.save_file()
    
    def exit_app(self):
        self.root.quit()
    
    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")
    
    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")
    
    def find_and_replace(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Find & Replace")
        dialog.geometry("300x150")
        
        tk.Label(dialog, text="Find:").pack()
        find_entry = tk.Entry(dialog)
        find_entry.pack()
        
        tk.Label(dialog, text="Replace:").pack()
        replace_entry = tk.Entry(dialog)
        replace_entry.pack()
        
        def find():
            text = find_entry.get()
            start = self.text_area.search(text, "1.0", stopindex=tk.END)
            if start:
                end = f"{start}+{len(text)}c"
                self.text_area.tag_add("highlight", start, end)
                self.text_area.tag_config("highlight", background="yellow")
        
        def replace():
            text = find_entry.get()
            replacement = replace_entry.get()
            content = self.text_area.get(1.0, tk.END)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, content.replace(text, replacement))
        
        tk.Button(dialog, text="Find", command=find).pack()
        tk.Button(dialog, text="Replace", command=replace).pack()
    
    def show_about(self):
        messagebox.showinfo("About", "Modern Notepad v1.01\nCreated by: Fakhriddin Khasanov")

if __name__ == "__main__":
    root = tk.Tk()
    ModernNotepad(root)
    root.mainloop()
