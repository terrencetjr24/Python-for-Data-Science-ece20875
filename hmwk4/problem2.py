
def stencil(data, f, width) :
    """
    perform a stencil using the filter f with width w on list data
    output the resulting list
    note that if len(data) = k, len(output) = k - width + 1
    f will accept as input a list of size width and return a single number
    :param data: list
    :param f: function
    :param width: int
    :return: list
    """
    #Fill in
    topLevelList = []
    for i in range(len(data)-width+1):
        topLevelList.append(f(data[i:width+i]))

    return topLevelList
    pass


def createBox(box) :
    """
    create a box filter from the input list "box"
    this filter should accept a list of length len(box) and return a simple
    convolution of it.
    the meaning of this box filter is as follows:
    for each element the input list l, multiple l[i] by box[i]
    sum the results of all of these multiplications
    return the sum
    So for a box of length 3, filter(l) should return:
      (box[0] * l[0] + box[1] * l[1] + box[2] * l[2])
    The function createBox returns the box filter itself, as well as the length
    of the filter (which can be passed as an argument to conv)

    :param box: list
    :return: function, int
    """
    #Fill in
    def boxFilter(l) :
        # Fill in

        if len(l) != len(box):
            print("Calling box filter with the wrong length list. Expected list of length ", len(box))
            return
        result = 0
        for x in range(len(box)):
            result += l[x] * box[x]
        return result
        pass
    return boxFilter, len(box)
        
if __name__ == '__main__' :    
    def movAvg(l) :
        if (len(l) != 3) :
            print(len(l))
            print("Calling movAvg with the wrong length list")
            exit(1)
        return float(sum(l)) / 3
    
    def sumSq(l) :
        if (len(l) != 5) :
            print("Calling sumSq with the wrong length list")
            exit(1)
        return sum([i ** 2 for i in l])
    
    
    data = [2, 5, -10, -7, -7, -3, -1, 9, 8, -6]
    
    print(stencil(data, movAvg, 3))
    print(stencil(data, sumSq, 5))
    
    #note that this creates a moving average!
    boxF1, width1 = createBox([1.0 / 3, 1.0 / 3, 1.0 /3])
    print(stencil(data, boxF1, width1))
    
    boxF2, width2 = createBox([-0.5, 0, 0, 0.5])
    print(stencil(data, boxF2, width2))

    data = [1, 2, 5, 4, -1, -2, 3, 4, 5]
    boxF3, width3 = createBox([0.25, 0, 0.25])
    print(stencil(data, boxF3, width3))

    data = [7, 3, 29, 3, 1, 33, -12]
    boxF4, width4 = createBox([2.0, 1.0, 2.0, 1.0])
    print(stencil(data, boxF4, width4))

    data = [8, 5, 8, -9, -10, 2, 6, 7, 4]
    boxF5, width5 = createBox([2, 0, 1])
    print(stencil(data, boxF5, width5))