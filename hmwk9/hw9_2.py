
from helper import remove_punc
from nltk.stem import PorterStemmer

import string
import nltk
import numpy as np

from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    FILE = open(doc, "r")
    fileString = FILE.read()

    #2. Tokenize string using nltk.tokenize.word_tokenize
    listOfWords = nltk.tokenize.word_tokenize(fileString)

    #3. Filter out punctuation from list of words (use remove_punc)
    newListOfWords = remove_punc(listOfWords)

    #4. Make the words lower case
    newNew = []
    for x in newListOfWords:
        newNew.append(x.lower())

    #5. Filter out stopwords
    almostDone = [word for word in newNew if not word in stopwords.words('english')]

    #6. Stem words
    words = []
    stemer = PorterStemmer()
    for x in almostDone:
        words.append(stemer.stem(x))

    return words
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    ListOfCleanedDocs = []
    for x in doclist:
        ListOfCleanedDocs.append(readAndCleanDoc(x))
    #2. Use these word lists to build the doc word matrix
    uniqueWords = set()
    for x in ListOfCleanedDocs:
        uniqueWords = set(x) | uniqueWords

    listOfUniqueWords = list(uniqueWords)
    listOfUniqueWords.sort()

    docword = np.zeros((len(doclist), len(listOfUniqueWords)))
    for column,uWord in enumerate(listOfUniqueWords):
        for row, wordlist in enumerate(ListOfCleanedDocs):
            for x in wordlist:
                if (x == uWord):
                    docword[row][column]+=1

    return docword, listOfUniqueWords
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    #fill in
    numberOfDocs , numberOfUniqueWords = docword.shape
    tf = np.zeros((numberOfDocs,numberOfUniqueWords))

    # figuring out the number of words in each document (row)
    wordsPerRow = []
    for x in range(numberOfDocs):
        holder = 0
        for y in range(numberOfUniqueWords):
            holder += docword[x][y]
        wordsPerRow.append(holder)

    # Finding the frequency of each word in their document by dividing its instances by the total number of words in the document (row)
    for row, numOfWordsInRow in enumerate(wordsPerRow):
        for col in range(numberOfUniqueWords):
            tf[row][col] = docword[row][col] / numOfWordsInRow

    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in
    numOfDocs, numOfUniWords = docword.shape
    idf = np.zeros((1,numOfUniWords))

    # Figuring out how many time a particular word occurs in the corpus
    wordInstances= []
    for col in range(numOfUniWords):
        holder = 0
        for row in range(numOfDocs):
            if (docword[row][col] > 0):
                holder+=1
        wordInstances.append(holder)

    # Building the idf "table"
    for row, instances in enumerate(wordInstances):
        idf[0][row] = np.log10(numOfDocs/instances)

    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in
    numOfDocs, numOfUniWords = docword.shape
    tf = buildTFMatrix(docword)
    idf = buildIDFMatrix(docword)

    tfidf = np.zeros(docword.shape)

    for row in range(numOfDocs):
        for col in range(numOfUniWords):
            tfidf[row][col] = idf[0][col] * tf[row][col]

    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html

    width = len(wordlist)
    height = len(doclist)

    prevalentDocWords = []

    tfidf = buildTFIDFMatrix(docword)

    # finding the most prevalent words in each document
    for row in range(height):
        workingList = []
        # going through the columns 3 times to get the 3 most prevalent words
        for x in range(3):
            holder = 0
            savedCol = 0
            for col in range(width):
                if (tfidf[row][col] > holder):
                    holder = tfidf[row][col]
                    savedCol = col
            # setting it to -1 so that it doesn't get repeated
            tfidf[row][savedCol] = -1
            workingList.append(wordlist[savedCol])

        prevalentDocWords.append(workingList)

    for index, filePath in enumerate(doclist):
        distinctiveWords[filePath] = prevalentDocWords[index]

    return distinctiveWords


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')

    # Uncomment and recomment ths part where you see fit for testing purposes
    # '''
    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc(path1)[0:5])
    print("*** Testing buildDocWordMatrix ***")
    doclist =[path1, path2]
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing buildTFMatrix ***") 
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    print("*** Testing buildIDFMatrix ***") 
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])
    print("*** Testing buildTFIDFMatrix ***") 
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))
    #'''
