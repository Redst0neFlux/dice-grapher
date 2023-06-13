from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import mplcursors
#toroll = [{4: [1,-1]},{4:[3]}]


def waysToMake(toroll):

    max = 0
    for faces, dice in toroll.items():
        for die in dice:
            max += faces * abs(
                die)  #makes dice positive to account for negatives
    dp = defaultdict(int)  #dynamic programming table
    dp[0] = 1
    for faces, dice in toroll.items():
        for die in dice:
            for c in range(abs(die)):
                sm = defaultdict(int)
                for i in range(max + 1):
                    sm[i] = sm[i - 1] + dp[i]
                for i in range(max + 1):
                    dp[i] = (sm[i - 1] - sm[i - faces - 1])

    down = 0
    for faces, dice in toroll.items():
        for die in dice:
            if die < 0:
                down += (faces + 1) * abs(die)
        dp = {x - down: y
              for x, y in dp.items()
              if y != 0}  #reduces all roll results to make negatives work

    return dp
def plotData(dataList):
    longx = []
    longy = []
    plt.style.use('fivethirtyeight')
    _, ax = plt.subplots()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=None))
    maxx = maxy = float("-inf")  #smallest possible value
    minx = miny = float("inf")  #largest possible value
    for toroll in dataList:
        label = toroll[1]
        toroll = toroll[0]
        result = waysToMake(toroll)
        result = {x: 100 * y / sum(result.values()) for x, y in result.items()}
        #print(result)
        if maxx < max(result.keys()):
            maxx = max(result.keys())
        if maxy < max(result.values()):
            maxy = max(result.values())
        if minx > min(result.keys()):
            minx = min(result.keys())
        if miny > min(result.values()):
            miny = min(result.values())
        longx += result.keys()
        longy += result.values()
        ax.plot(result.keys(), result.values(), linewidth=2.0, marker="o", label=label)
        print(label)
        #ax.set_label(label)

    #print(maxx, maxy, minx, miny)
    """
    ax.set(xlim=(minx - 0.5, maxx + 0.5),
           xticks=np.arange(minx, maxx + 1),
           ylim=(miny - 0.5, maxy + 1),
           yticks=np.arange(int(miny - 1), maxy + 1))"""
    ax.legend()
    dots = ax.scatter(longx, longy, color='none')
    mplcursors.cursor(dots, hover=True)

    plt.show()


#plotData(toroll)
