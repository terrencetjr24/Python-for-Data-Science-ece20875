import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def main():
    #Importing dataset
    diamonds = pd.read_csv('diamonds.csv')

    #Feature and target matrices
    X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z', 'clarity', 'cut', 'color']]
    y = diamonds[['price']]

    #Training and testing split, with 25% of the data reserved as the test set
    X = X.to_numpy()
    y = y.to_numpy()
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)

    #Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    #Define the range of lambda to test
    lmbda = np.logspace(-1, 2, 101)

    MODEL = []
    MSE = []
    for l in lmbda:
        #Train the regression model using a regularization parameter of l
        model = train_model(X_train,y_train,l)
        #Evaluate the MSE on the test set
        mse = error(X_test,y_test,model)

        #Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    #Plot the MSE as a function of lmbda
    fig = plt.figure()
    plt.plot(lmbda, MSE)
    plt.xlabel('Regularization Parameter Lambda')
    plt.ylabel('Mean Squared Error')
    plt.title('MSE vs Lambda')
    plt.tight_layout()
    plt.savefig('problem2_figure')

    #Find best value of lmbda in terms of MSE
    holder = min(MSE)
    for z in range(len(MSE)):
        if MSE[z] == holder:
            break

    ind = z
    [lmda_best,MSE_best,model_best] = [lmbda[ind],MSE[ind],MODEL[ind]]

    print('Best lambda tested is ' + str(lmda_best) + ', which yields an MSE of ' + str(MSE_best))

    return model_best


#Function that normalizes features in training set to zero mean and unit variance.
#Input: training data X_train
#Output: the normalized version of the feature matrix: X, the mean of each column in
#training set: trn_mean, the std dev of each column in training set: trn_std.
def normalize_train(X_train):
    height = len(X_train)
    width = len(X_train[0])
    featureList = []
    meanList = []
    stdList = []

    # Reorganizing the data for manipulation
    ind = -1
    for x in range(width):
        featureList.append([])
        ind += 1
        for y in range(height):
            featureList[ind].append(X_train[y][x])
    # Finding the mean and std of each feature list
    for x in featureList:
        meanList.append(np.mean(x))
        stdList.append(np.std(x))
    # normalizing the data
    for feat in range(width):
        for x in range(height):
            featureList[feat][x] = (featureList[feat][x] - meanList[feat]) / stdList[feat]
    # Putting the data back into the same format that I received it in
    X = []
    ind = -1
    for x in range(height):
        X.append([])
        ind+=1
        for feat in range(width):
            X[ind].append(featureList[feat][x])

    return X, meanList, stdList


#Function that normalizes testing set according to mean and std of training set
#Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each
#column in training set: trn_std
#Output: X, the normalized version of the feature matrix, X_test.
def normalize_test(X_test, trn_mean, trn_std):
    height = len(X_test)
    width = len(X_test[0])
    featureList = []

    # Reorganizing the data for manipulation
    ind = -1
    for x in range(width):
        featureList.append([])
        ind += 1
        for y in range(height):
            featureList[ind].append(X_test[y][x])
    # normalizing the data
    for feat in range(width):
        for x in range(height):
            featureList[feat][x] = (featureList[feat][x] - trn_mean[feat]) / trn_std[feat]
    # Putting the data back into the same format that I received it in
    X = []
    ind = -1
    for x in range(height):
        X.append([])
        ind += 1
        for feat in range(width):
            X[ind].append(featureList[feat][x])

    return X



#Function that trains a ridge regression model on the input dataset with lambda=l.
#Input: Feature matrix X, target variable vector y, regularization parameter l.
#Output: model, a numpy object containing the trained model.
def train_model(X,y,l):
    #fill in
    model = linear_model.Ridge(alpha=l)
    model.fit(X, y)
    # model.coef_ is the object attribute that contains the coefficients of the model
    # model.intercept_ is the object attribute that contains the intercept of the model
    return model


#Function that calculates the mean squared error of the model on the input dataset.
#Input: Feature matrix X, target variable vector y, numpy model object
#Output: mse, the mean squared error
def error(X,y,model):
    width = len(X[0])
    y_pred = []
    y_true = []
    coef_holder = model.coef_[0]
    intercept_holder = model.intercept_

    # calculating the predicted values
    for z in X:
        holder = 0
        for q in range(width):
            holder += (z[q] * coef_holder[q])
        y_pred.append(holder + intercept_holder) # adding the intercept
    # converting list of arrays into a list of numbers
    for z in range(len(y_pred)):
        y_pred[z] = y_pred[z][0]
    for z in y:
        y_true.append(z[0])
    mse = mean_squared_error(y_true=y_true, y_pred=y_pred)
    return mse

if __name__ == '__main__':
    model_best = main()

    print(model_best.coef_)
    print(model_best.intercept_)

    price = (model_best.coef_[0][0] * 0.25) + (model_best.coef_[0][1] * 3) + (model_best.coef_[0][2] * 3) + (model_best.coef_[0][3] * 5) + (model_best.coef_[0][4] * 60) + (model_best.coef_[0][5] * 55) + (model_best.coef_[0][6] * 4) + (model_best.coef_[0][7] * 3) + (model_best.coef_[0][8] * 2) + (model_best.intercept_[0] * 1)
    print("price of this diamond is: ", price)
