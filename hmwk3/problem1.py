import numpy as np
import matplotlib.pyplot as plt
from helper import *

#test commit
def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: list
    :return: list
    """
    # n, bins, patches = plt.hist(x=hist)
    totalValues = sum(hist)
    probabilityList = []
    for x in hist:
        probabilityList.append(x/totalValues)

    return probabilityList
    pass


def computeJ(histo, width):
    """
    calculate computeJ for one bin width

    expecting a histo of counts, then calls norm_histogram to get the probabilities

    :param histo: list
    :param width: int
    :return: float
    """
    probabilityHisto = norm_histogram(histo)
    squaredSum = 0
    for x in probabilityHisto:
        squaredSum += (x * x)
    numOfSamples = sum(histo)

    part1 = 2 / (width *(numOfSamples-1))
    part2 = (numOfSamples + 1) / (width * (numOfSamples - 1))
    part3 = part2 * squaredSum
    return part1 - part3

    pass


def sweepN (data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate computeJ for a full sweep [min_bins to max_bins]

    plt.histo used in here (not in computerJ)

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """

    J_List = []
    for x in range(min_bins, max_bins+1):
        widthUsed = (maximum - minimum) / x
        work_list, work_bins, work_patches = plt.hist(x=data, bins=x)
        J_List.append(computeJ(histo=work_list, width=widthUsed))

    return J_List
    pass


def findMin (l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    min = l[0]
    indexSaved = 0

    for x in range(len(l)):
        if l[x] < min:
            min = l[x]
            indexSaved = x

    return (min, indexSaved)
    pass


if __name__ == '__main__':
    data = getData()  # reads data from inp.txt. This is defined in helper.py
    lo = min(data)
    hi = max(data)
    #My test

    js = sweepN(data, lo, hi, 1, 100)

    # the values 1 and 100 represent the lower and higher bound of the range of bins.
    # They will change when we test your code and you should be mindful of that.
    print(findMin(js))

    # Include code here to plot js vs. the bin range

