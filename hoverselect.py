import tkinter as tk
class CustomListBox(tk.Listbox):

    def __init__(self, master=None, on_motion=print, on_click=print, *args, **kwargs):
        tk.Listbox.__init__(self, master, *args, **kwargs)
        self.current = 0
        self.last = None
        self.motion_func = on_motion
        self.click_func = on_click
        self.bind("<Motion>", self.on_motion)
        self.bind("<<ListboxSelect>>", self.on_click)

    def on_motion(self, event):
        index = self.index(f"@{event.x},{event.y}")
        self.current = index
        if self.last != self.current :
            data = self.get(self.current)
            self.motion_func(data)            
            self.last = self.current
    def on_click(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.click_func(data)

if __name__ == "__main__":
    root = tk.Tk()
    txt = tk.Label(root, text="a")
    listbox = CustomListBox(root, on_motion=lambda x: txt.config(text=x))
    listbox.pack()
    txt.pack()
    listbox.insert("end", "one", "two", "three", "four", "five")
    
    root.mainloop()