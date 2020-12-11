#Homework Number: 5
#Name: Terrence Randall

#!/usr/bin/env python3

import numpy as np
import os
import sys
from scipy.stats import norm
from scipy.stats import t

def openFileAngGetData(fileName):
    myFile = open(fileName)
    data = myFile.readlines()
    myFile.close()

    data = [float(x) for x in data]

    return data

def getBasicStats(data):
    avg = np.mean(data)
    sd = np.std(data, ddof=1)

    return (avg, sd, len(data))

def findLowestSE(data_stats):
    x = data_stats1[2]
    print(f"x prior is {x}")
    p_1 = 1
    x = data_stats[2]
    while p_1 > 0.05:
        x += 1
        SE_1 = data_stats[1] / (x ** 0.5)
        z_1 = (data_stats1[0] - 0.75) / SE_1
        p_1 = 2 * norm.cdf(-abs(z_1))
        print(f"The p_score is {p_1}")
        print(f"THe SE is {SE_1}")
        print(f"The size is {x}")
    return

if __name__ == '__main__':
    data0 = openFileAngGetData('eng0.txt')
    data_stats0 = getBasicStats(data0) #[0] is avg, and [1] is standard dev
    print("For eng0:")
    print(f"The avg of the data is {data_stats0[0]} and the std dev is {data_stats0[1]} and the number of samples is {data_stats0[2]}")

    data1 = openFileAngGetData('eng1.txt')
    data_stats1 = getBasicStats(data1)  # [0] is avg, and [1] is standard dev
    print("For eng1:")
    print(f"The avg of the data is {data_stats1[0]} and the std dev is {data_stats1[1]} and the number of samples is {data_stats1[2]}")

    SE_1 = data_stats1[1] / (data_stats1[2] ** 0.5)
    z_1 = (data_stats1[0] - 0.75) / SE_1
    p_1 = 2 * norm.cdf(-abs(z_1))
    print(f"The p_score is {p_1}")
    #findLowestSE(data_stats1)
