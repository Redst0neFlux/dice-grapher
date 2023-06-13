import tkinter as tk
from diceroller import main as diceroller
from dicegrapher import main as dicegrapher
from hoverselect import CustomListBox
main = tk.Tk()

def change_description(data):
    info_dict = {
        "Dice Roller": "Rolls dice from a given formula",
        "Dice Probability Grapher": "Generates a graph of the probability of outcomes of a given formula",
        "Stats Roller": "Generates dungeons and dragons stats"
    }
    label2.config(text=info_dict[data])

def open_window(data):
    if data == "Dice Roller":
        diceroller(main)
    elif data == "Stats Roller":
        pass
    elif data == "Dice Probability Grapher":
        dicegrapher(main)




label1 = tk.Label(main, text="Main Menu", font=("Arial",30))
listbox = CustomListBox(main,on_motion=change_description, on_click=open_window, width=20)
listbox.insert(0,"Dice Roller","Dice Probability Grapher","Stats Roller")
label2 = tk.Label(main,text="", width=10, wraplength=170, justify=tk.LEFT, font=("Arial",10))

label1.grid(row=1,column=1,columnspan=3)
listbox.grid(row=2,column=1, sticky=tk.W)
label2.grid(row=2, column=2,ipadx=40)

