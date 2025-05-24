from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
# It has two parameter:
# a - shape parameter.
# size - The shape of the returned array.
x=random.pareto(a=2, size=(1000))
print(x)

sbn.displot(x)
plt.show()