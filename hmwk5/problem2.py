#!/usr/bin/env python3
#Homework Number: 5
#Name: Terrence Randall

import numpy as np
import os
import sys
from scipy.stats import norm
from scipy.stats import t
from problem1 import getBasicStats

def calcS(data, stats):
    s = 0
    summation = 0

    for x in data:
        summation += ((x - stats[0])**2)
    holder = (1/10) * summation
    #holder = (1 / (data[2] - 1)) * summation # data[2] should be 11 but it's not for some reason

    s = holder**(0.5)
    print(f"S is {s}")
    return s

def calcTscore(stats, s_val):
    retVal = (stats[0] - 0) / (s_val / (stats[2]**0.5))

    return retVal

def Q1and2(data, data_stats, df):
    s = calcS(data, data_stats)
    t_score = calcTscore(data_stats, s)
    SE = s / (data_stats[2] ** 0.5)
    p_val = 2 * t.cdf(-abs(t_score), df)

    # t_score coresponding to c
    confidence_level = 0.95
    alpha = (1 - confidence_level) / 2
    t_confidence = t.ppf(1 - alpha, df)

    print(f"The number of samples is {data_stats[2]}")
    print(f"The sample mean is {data_stats[0]}")
    print(f"The s val is {s} (and not the std dev inside of the tuple)")

    print(f"The SE value is {SE}")
    print(f"The t-score is  {t_score}")
    print(f"The p_value is  {p_val}")

    print(f"The t_score corresponding to a {confidence_level * 100}% confidence interval is {t_confidence}")

    # t_score coresponding to c
    confidence_level_2 = 0.9
    alpha_2 = (1 - confidence_level_2) / 2
    t_confidence_2 = t.ppf(1 - alpha_2, df)

    print(f"For problem 2, The t_score corresponding to a {confidence_level_2 * 100}% confidence interval is {t_confidence_2}")

def Q3(data, data_stats, df):
    given_sd = 16.836
    SE = given_sd / (data[2]**0.5)
    z_score = (data_stats[0] - 0) / SE
    p_value = 2 * norm.cdf(-abs(z_score))

    # t_score coresponding to c
    confidence_level = 0.95
    alpha = (1 - confidence_level) / 2
    c_confidence = norm.ppf(1 - alpha)
    lowerVal = data_stats[0] - (c_confidence*SE)
    upperVal = data_stats[0] + (c_confidence*SE)

    print(f"The SE is {SE}")
    print(f"The z_score is {z_score}")
    print(f"The {confidence_level*100}% interval is from {lowerVal} to {upperVal}")

def Q4(data, data_stats, df):
    s = calcS(data, data_stats)
    t_score = calcTscore(data_stats, s)
    SE = s / (data_stats[2] ** 0.5)
    p_val = 2 * t.cdf(-abs(t_score), df)
    #initializing the lower value to test against
    lowerVal = -1
    confidence_level = 1
    while lowerVal < 0:
        # t_score corresponding to c
        confidence_level -= 0.0001
        alpha = (1 - confidence_level) / 2
        t_confidence = t.ppf(1 - alpha, df)

        lowerVal = data_stats[0] - (t_confidence * SE)
        upperVal = data_stats[0] + (t_confidence * SE)

    print(f"The {confidence_level*100}% interval is from {lowerVal} to {upperVal}")



if __name__ == '__main__':
    data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]
    data_stats = getBasicStats(data)  # [0] is avg, and [1] is standard dev [2] is the amount of samples
    df = data_stats[2] - 1

    Q1and2(data, data_stats, df)
    print("------------------")
    Q3(data, data_stats, df)
    print("------------------")
    Q4(data, data_stats, df)