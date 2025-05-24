from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# Zipf's Law: In a collection, the nth common term is 1/n times of the most 
# common term. E.g. the 5th most common word in English occurs nearly 1/5
#  times as often as the most common word.

# It has two parameters:
# a - distribution parameter.
# size - The shape of the returned array.
x=random.pareto(a=2, size=(1000))
print(x)
# Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.
sbn.displot(x[x<10])
plt.show()