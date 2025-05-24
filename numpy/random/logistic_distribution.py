from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.
# It has three parameters:
# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.

x=random.logistic(loc=4,scale=2,size=(5,3))
print(x)

sbn.displot(x,kind='kde')
plt.show()