from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# Chi Square distribution is used as a basis to verify the hypothesis.
# It has two parameters:
# df - (degree of freedom).
# size - The shape of the returned array.
x=random.chisquare(df=2, size=(5,3))
print(x)

sbn.displot(x,kind='kde')
plt.show()