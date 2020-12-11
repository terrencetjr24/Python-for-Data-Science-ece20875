import string

def Union(list1, list2):
    return list(set(list1) | set(list2))

#Arguments:
#  filename: name of file to read in
#Returns: a list of strings
# each string is one line in the file, 
# and all of the characters should be lowercase, have no newlines, and have both a prefix and suffix of '__' (2 underscores)
#Notes: make sure to pad the beginning and end of the string with '_'
#       make sure the string does not contain newlines
#       make sure to convert the string to lower-case
#       so "Hello World" should be turned into "__hello world__"
#hints: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       https://docs.python.org/3/library/stdtypes.html#str.splitlines
def getFormattedText(filename) :
    #fill in
    lines = []

    dummy1 = []
    dummy2 = []
    holder = '__'
    FILE = open(filename, "r")

    # reading the lines of the file into a list
    for x in FILE:
        if (x != '\n'):
            dummy1.append(x)

    # making sure that all characters are lower case
    for x in dummy1:
        dummy2.append(x.lower())

    # Getting rid of all new line characters and punctuations
    for x in dummy2:
        for y in x:
            if (y == '\n'):
                holder = holder + '__'
            elif (y not in string.punctuation):
                holder = holder + y

        lines.append(holder)
        holder = '__'

    return lines
        

#Arguments:
#  line: a string of text
#Returns: a list of 3-character n-grams
def getNgrams(line) :
    #fill in
    nGrams = []
    line_length = len(line)

    for x in range(line_length-2):
        nGrams.append(line[x:x+3])

    return nGrams

#Arguments:
#  filename: the filename to create an n-gram dictionary for
#Returns: a dictionary
#  where ngrams are the keys and the count of that ngram is the value.
#Notes: Remember that getFormattedText gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       You should use getFormattedText() and getNgrams() in this function.
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def getDict(filename):
    #fill in
    # Getting input lines from the file
    inputLines = getFormattedText(filename)

    # Creating a list of nGrams (without any repeates)
    nGramlist = []
    for x in inputLines:
        nGramlist = Union(nGramlist, getNgrams(x))

    # Initializing the dictionary (each nGram "never" occurs as of now)
    nGramDict = dict.fromkeys(nGramlist, 0)
    # incrementing the count inside the dictionary for each nGrams occurence
    for x in inputLines:
        holder = getNgrams(x)
        for y in holder:
            nGramDict[y] += 1

    return nGramDict

#Arguments:
#   filename: the filename to generate a list of top N (most frequent n-gram, count) tuples for
#   N: the number of most frequent n-gram tuples to have in the output list.
#Returns: a list of N tuples 
#   which represent the (n-gram, count) pairs that are most common in the file.
#   To clarify, the first tuple in the list represents the most common n-gram, the second tuple the second most common, etc...
#You may find the following StackOverflow post helpful for sorting a dictionary by its values: 
#Also consider the dict method popitem()
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def topNCommon(filename,N):
    commonN = []
    nGramDict = getDict(filename)
    holderValue = 0
    nextToAdd = 'x'

    while len(commonN) < N:
        for x in nGramDict:
            if (nGramDict[x] >= holderValue):
                nextToAdd = x
                holderValue = nGramDict[x]
        nGramDict[nextToAdd] = -1
        commonN.append((nextToAdd, holderValue))
        holderValue = 0

    return commonN

########################################## Checkpoint, can test code above before proceeding #############################################

#Arguments:
#   fileNamesList: a list of filepath strings for the different language text files to process
#Returns: a list of dictionaries 
#   where each dictionary corresponds to one of the filepath strings.
#   Each dictionary in the list
#   should have keys corresponding to the n-grams, and values corresponding to the count of the n-gram
#Hint: Use functions defined in previous step.
def getAllDicts(fileNamesList):
    langDicts = []
    for x in fileNamesList:
        langDicts.append(getDict(x))

    return langDicts

#Arguments:
#   listOfDicts: A list of dictionaries where the keys are n-grams and the values are the count of the n-gram
#Returns: an alphabetically sorted list containing all of the n-grams across all of the dictionaries in listOfDicts (note, do not have duplicates n-grams)
#Notes: It is recommended to use the "set" data type when doing this (look up "set union", or "set update" for python)
#   Also, for alphabetically sorted, we mean that if you have a list of the n-grams altogether across all the languages, and you call sorted() on it, that is the output we want
def dictUnion(listOfDicts):
    unionNGrams = []
    holderList = []

    for x in listOfDicts:
        for y in x:
            holderList.append(y)
        unionNGrams = Union(unionNGrams, holderList)

    unionNGrams.sort()
    return unionNGrams


#Arguments:
#   langFiles: list of filepaths of the languages to compare testFile to.
#Returns a sorted list of all the n-grams across the languages
# Note: Use previous two functions.
def getAllNGrams(langFiles):
    allNGrams = []

    allDicts = getAllDicts(langFiles)
    allNGrams = dictUnion(allDicts)
    

    return allNGrams

########################################## Checkpoint, can test code above before proceeding #############################################

#Arguments:
#   testFile: mystery file's filepath to determine language of
#   langFiles: list of filepaths of the languages to compare testFile to.
#   N: the number of top n-grams for comparison
#Returns the filepath of the language that has the highest number of top 10 matches that are similar to mystery file.
#Note/Hint: depending how you implemented topNCommon() earlier, you should only need to call it once per language, and doing so avoids a possible error
def compareLang(testFile,langFiles,N):
    langMatch = ''
    topnGramsForRefFiles = []
    topnGramsforTest = []
    afterIntersection = []

    # Obtaining a list of tuples for the most common nGrams, then turning that into only a list of nGrams
    holder = topNCommon(testFile, N)
    for y in holder:
        topnGramsforTest.append(y[0])

    # Obtaining a list of tuples for the most common nGrams, then turning that into a list of only nGrams, then adding that the the greater list
    for x in langFiles:
        tupleList = topNCommon(x, N)
        holder2 = []
        for y in tupleList:
            holder2.append(y[0])
        topnGramsForRefFiles.append(holder2)

    for x in topnGramsForRefFiles:
        afterIntersection.append(list(set(x).intersection(set(topnGramsforTest))))

    prevHighest = 0
    for x in enumerate(afterIntersection):
        if (len(x[1]) > prevHighest):
            index = x[0]
            prevHighest = len(x[1])

    langMatch = langFiles[index]

    '''
    for x in enumerate(afterIntersection):
        print(f"{langFiles[x[0]]}: {x[1]}")
    '''
    return langMatch




if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext


    #Test topNCommon()
    path = join('ngrams','english.txt')
    print(topNCommon(path,10))
    
    #Compile ngrams across all 6 languages and determine a mystery language
    path='ngrams'
    fileList = [f for f in listdir(path) if isfile(join(path, f))]
    pathList = [join(path, f) for f in fileList if 'mystery' not in f]#conditional excludes mystery.txt
    print(getAllNGrams(pathList))#list of all n-grams spanning all languages
    
    #testFile = join(path,'mystery.txt')
    testFile = 'test.txt'
    print(compareLang(testFile, pathList, 20))#determine language of mystery file
    
