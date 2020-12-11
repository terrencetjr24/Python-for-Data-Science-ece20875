def histogram(data, n, l, h):
    # data is a list
    # n is an integer
    # l and h are floats
    hist = n * [0]
    b_width = (h-l)/n

    if(n < 0 or h <1):
        print("invalid bin amount or high-value")
        return hist

    for x in data:
        #if the x is within the given range
        if(not(x <= l or x >= h)):
            work = x - l
            hist[int(work / b_width)] += 1

    # return the variable storing the histogram
    # Output should be a list
    return hist

    pass

def addressbook(name_to_phone, name_to_address):
    #name_to_phone and name_to_address are both dictionaries
    fullDictionary = {}
    namesList = []
    addrList = []
    phoneList = []

    for x in name_to_phone:
        namesList.append(x)
    for x in namesList:
        phoneList.append(name_to_phone[x])
    for x in namesList:
        addrList.append(name_to_address[x])
    #initializing the dictionary
    for x in addrList:
        fullDictionary[x] = 0
    '''
    print(namesList)
    print(addrList)
    print(phoneList)
    print(name_to_phone)
    print(name_to_address)
    '''
    for q in namesList: #iterating through the names for the phone check
        for y in addrList:
            for z in phoneList:
                if name_to_phone[q] == z and name_to_address[q] == y: #found the number to use for the address
                    if fullDictionary[y] == 0:
                        fullDictionary[y] = ([], z)
                    if q not in fullDictionary[y][0]:
                        fullDictionary[y][0].append(q)
    # checking dictionary for multiple names to single address to give warnings
    differentNum = 0
    workingList = []
    for addy in fullDictionary:
        differentNum = 0
        workingList.clear()
        for name in fullDictionary[addy][0]:
            if name_to_phone[name] != fullDictionary[addy][1]:
                differentNum += 1
                workingList.append(name)
        if differentNum > 0:
            print('Warning: ', end='')
            size = differentNum
            i = 0
            while differentNum > 1:
               print(workingList[i] +', ', end='')
               i+=1
               differentNum -= 1
            for x in namesList:
                if name_to_phone[x] == fullDictionary[addy][1]:
                    nameUsedForNumber = x
            print(workingList[size-1] + ' has a different number for ' + addy + ' than ' + nameUsedForNumber + '. Using the number for ' + nameUsedForNumber)
    # return the variable storing address_to_all
    # Output should be a dictionary

    return fullDictionary
    pass
