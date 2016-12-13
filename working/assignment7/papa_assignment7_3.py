import os
import re
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter

def kill_thread(thread):
    import ctypes
    id = thread.ident
    code = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(id),ctypes.py_object(SystemError))
    if code == 0:
        raise ValueError('invalid thread id')
    elif code != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(id),ctypes.c_long(0))
        raise SystemError('PyThreadState_SetAsyncExc failed')

def rollDice(n):
    dice = []
    i = 1
    while i <= n:
        dice.append(random.randint(1,6))
        i += 1
    return dice

def histogram(dice_freq, max_sum):
    plt.hist(dice_freq, bins = 11, range =(2, max_sum))
    plt.title("Frequency vs Dice sum")
    plt.ylabel("Frequency")
    plt.xlabel("Dice Sum")
    plt.show()

def getFreq(dice):
    counter = Counter(dice)
    nums, frq = zip(*counter.most_common())
    return frq, nums

def getCDF(freq):
    cumsum = np.cumsum(freq)
    normedcumsum = [x/float(cumsum[-1]) for x in cumsum]
    return normedcumsum

def plotCDF(x, cumsum, median, median_cdf, prob):
    plt.plot(x, cumsum, 'r-')
    plt.axvline(median, color='b', linestyle='dashed', linewidth=2)
    plt.axhline(median_cdf, color='b', linestyle='solid', linewidth=1)
    plt.axhline(prob, color='y', linestyle='solid', linewidth=1)

    # adds labels to the axis
    plt.ylabel('Probability')
    plt.xlabel('Dice roll')

    # generates legend
    cdf_legend = mpatches.Patch(color='red', label='CDF')
    median_legend = mpatches.Patch(color='blue', label='Median')
    prob_legend = mpatches.Patch(color='yellow', label='Median')

    plt.legend(handles=[cdf_legend, median_legend, prob_legend], loc=5)
    plt.show()

def diceSums(dice_1, dice_2, n):
    i = 0
    dice = []
    while i < n:
        dice.append(dice_1[i] + dice_2[i])
        i += 1
    return dice
def getProb(n,cdf):
    i = 0
    prob = 0
    while i <= 9:
        print(cdf[i])
        prob += cdf[i]
        i += 1
    print(prob)
    return prob
def task():
    #n = 1000
    n = 100
    dice_1 = rollDice(n)
    dice_2 = rollDice(n)
    dice = diceSums(dice_1, dice_2, n)

    max_sum = max(dice)
    histogram(dice, max_sum)

    freq, nums = getFreq(dice)

    cdf = getCDF(freq)
    x = [i for i in range(2, len(cdf) + 2)]

    median = np.median(dice)
    median_cdf = np.median(cdf)
    prob_9= cdf[9]

    plotCDF(x, cdf, median, median_cdf, prob_9)
    return cdf
def main():
    cdf_1 = task()
    cdf_2 = task()
    smirnov_max = []
    smirnov = [cdf_1_i - cdf_2_i for cdf_1_i, cdf_2_i in zip(cdf_1, cdf_2)]
    smirnov_max.append(max(smirnov))
    print(smirnov_max)
    #For 100 vals 0.059
    #For 1000 vals 0.012
if __name__ == "__main__":
        main()