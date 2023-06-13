from collections import defaultdict
from grapher4 import plotData
def strToRoll(dice):
    #dice = "1d4-2d4,d4"
    output = []
    for roll in dice.split(","):
        final = []
        part = ""
        for x in roll:
            if x in ("+", "-"):
                final.append(part)
                part = x if x == "-" else ""
            else:
                part += x
        final.append(part)
    
        temp = defaultdict(list)
        for roll2 in final:
            if roll2.count("d") == 1:
                x = roll2.split("d")
                if x[0] == "": 
                    x[0] = "1" # makes d4 == 1d4
                temp[int(x[1])].append(int(x[0]))
            elif roll.count("d") == 0: 
                temp[1].append(int(roll2)) # makes 5 = 5d1
            else:
                raise Exception("OHNO")
    
        output.append([temp,roll])
    plotData(output)