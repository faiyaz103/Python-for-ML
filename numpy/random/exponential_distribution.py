from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# Exponential distribution is used for describing time till next event e.g. failure/success etc.
# It has two parameters:
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.
x=random.exponential(scale=2, size=(5,3))
print(x)

sbn.displot(x,kind='kde')
plt.show()