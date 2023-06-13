from random import randint
from math import prod
from tkinter import messagebox

class NotationParseError(Exception):
    def __init__(self, message):
        messagebox.showerror(message=message)


def run(diceroll):
    diceroll = diceroll.replace(" ","")
    total = 0
    if diceroll == "":
        return 0
    elif "+" in diceroll:
        splitdice = diceroll.split("+")
        for x in splitdice:
            total += run(x)
    elif "-" in diceroll:
        splitdice = diceroll.split("-")
        total += run(splitdice.pop(0))
        for x in splitdice:
            total -= run(x)
    elif "*" in diceroll:
        splitdice = diceroll.split("*")
        total += prod(map(run, splitdice))
    elif "d" in diceroll:
        splitdice = diceroll.split("d")
        if len(splitdice) >= 3 or splitdice[1] == "" or int(splitdice[1]) == 0:
            raise NotationParseError("NotationParseError")
        if splitdice[0] == "":
            splitdice[0] = 1
        for x in range(int(splitdice[0])):
            total += randint(1, int(splitdice[1]))
    else:
        total += int(diceroll)
    return total
def main(diceroll):
    if not all([x.isdigit() or x in "d+-* " for x in diceroll]):
        raise NotationParseError("NotationParseError")
    return run(diceroll)
