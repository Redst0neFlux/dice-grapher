import tkinter as tk
from roll import main as roll
def main(old_main):

    def rollcmd():
        output.config(text=roll(entry_box.get()))

    frame = tk.Toplevel(old_main)

    
    title = tk.Label(frame, text="Dice roller", font=("Arial",30))
    entry_box = tk.Entry(frame)
    roll_button = tk.Button(frame, text= "Roll", command=rollcmd)
    output = tk.Label(frame,text="")
    
    title.grid(row=1,column=1,columnspan=3)
    entry_box.grid(row=2,column=1,columnspan=3)
    roll_button.grid(row=3,column=1)
    output.grid(row=3,column=2,rowspan=2)


