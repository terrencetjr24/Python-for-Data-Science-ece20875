import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from helper import *

data = getData('distB.csv')
hist, _, _ = plt.hist(x=data, bins=170)


#stats.probplot(data, dist = 'laplace', plot=plt)
plt.show()
#plt.savefig('distA-laplace.png') # modify this to write the plot to a file instead