import numpy as np
import matplotlib.pyplot as plt


#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    targetVar = []
    explVar = []

    #fill in
    #read the input file, assuming it has two columns, where each row is of the form [x y] as
    #in poly.txt.
    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.
    FILEIN = open(datapath, 'r')
    for x in FILEIN:
        hold1, hold2 = x.split()
        explVar.append(float(hold1))
        targetVar.append(float(hold2))
    FILEIN.close()

    featureMatrixList = []
    for deg in degrees:
        # *** Need to figure out what the format of each element in the paramFits list is supposed to be
        featureMatrixList.append(feature_matrix(explVar, deg))

    for x in featureMatrixList:
        paramFits.append(least_squares(x, targetVar))

    # display(xData=explVar, yData=targetVar, parameterList=paramFits)

    # converting paramFits to regular list
    dummy = []
    ind = -1
    for x in paramFits:
        dummy.append([])
        ind += 1
        for y in x:
            dummy[ind].append(y)
    return dummy


#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    X = []
    for sampleIndex in range(len(x)):
        X.append([])
        for deg in range(d, -1, -1):
            X[sampleIndex].append(float(x[sampleIndex]**(deg)))

    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^d, x^(d-1), ..., x^0.

    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    #print(X)
    #print(y)
    #fill in
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B = np.linalg.inv(X.T @ X) @ (X.T @ y)
    return B

def display(xData, yData, parameterList):
    scat = plt.scatter(x=xData, y=yData)
    increment = []
    for x in np.linspace(-10, 20, 1000):
        increment.append(x)
    deg1Out = []
    deg2Out = []
    deg3Out = []
    deg4Out = []
    deg5Out = []
    for x in increment:
        deg1Out.append(parameterList[0][0]*(x**1) + parameterList[0][1]*(x**0))
        deg2Out.append(parameterList[1][0]*(x**2) + parameterList[1][1]*(x**1) + parameterList[1][2]*(x**0))
        deg3Out.append(parameterList[2][0]*(x**3) + parameterList[2][1]*(x**2) + parameterList[2][2]*(x**1) + parameterList[2][3]*(x**0))
        deg4Out.append(parameterList[3][0]*(x**4) + parameterList[3][1]*(x**3) + parameterList[3][2]*(x**2) + parameterList[3][3]*(x**1) + parameterList[3][4]*(x**0))
        deg5Out.append(parameterList[4][0]*(x**5) + parameterList[4][1]*(x**4) + parameterList[4][2]*(x**3) + parameterList[4][3]*(x**2) + parameterList[4][4]*(x**1) + parameterList[4][5]*(x**0))

    line1, = plt.plot(increment, deg1Out, scaley=True)
    line2, = plt.plot(increment, deg2Out, scaley=False)
    line3, = plt.plot(increment, deg3Out, scaley=False)
    line4, = plt.plot(increment, deg4Out, scaley=False)
    line5, = plt.plot(increment, deg5Out, scaley=False)
    scat.set_label('data')
    line1.set_label('degree = 1')
    line2.set_label('degree = 2')
    line3.set_label('degree = 3')
    line4.set_label('degree = 4')
    line5.set_label('degree = 5')
    plt.legend()
    plt.savefig('problem1_figure')

    x = 2
    x_is_two_val = parameterList[4][0]*(x**5) + parameterList[4][1]*(x**4) + parameterList[4][2]*(x**3) + parameterList[4][3]*(x**2) + parameterList[4][4]*(x**1) + parameterList[4][5]*(x**0)
    print(f"For x = 2, we'd expect a value of {x_is_two_val}")
    #plt.show()

    return

if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [1, 2, 3, 4, 5]

    paramFits = main(datapath, degrees)

    print("The paramaters")
    for x in paramFits:
        print(x)
    #print(paramFits)
