from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# Rayleigh distribution is used in signal processing.
# It has two parameters:
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.
x=random.rayleigh(scale=2, size=(5,3))
print(x)

sbn.displot(x,kind='kde')
plt.show()