import tkinter as tk
from temp import strToRoll
def main(old_main):

    def rollcmd():
        strToRoll(entry_box.get())

    frame = tk.Toplevel(old_main)

    
    title = tk.Label(frame, text="Dice grapher", font=("Arial",30))
    entry_box = tk.Entry(frame)
    roll_button = tk.Button(frame, text= "Graph it", command=rollcmd)
    output = tk.Label(frame,text="")
    
    title.grid(row=1,column=1,columnspan=3)
    entry_box.grid(row=2,column=1,columnspan=3)
    roll_button.grid(row=3,column=1)
    output.grid(row=3,column=2,rowspan=2)


