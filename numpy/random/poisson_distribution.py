from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# It has two parameters:
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.
x=random.poisson(lam=2,size=1000)
print(x)

sbn.displot(x)
plt.show()

# Difference Between Normal, binomial and Poisson Distribution
data={
    "normal":random.normal(loc=50,scale=7,size=1000),
    "binomial":random.binomial(n=1000,p=0.3,size=1000),
    "poisson":random.poisson(lam=10,size=1000)
}
sbn.displot(data,kind='kde')
plt.show()