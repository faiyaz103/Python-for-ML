from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn
# Given 10 trials for coin toss generate 10 data points:
x=random.binomial(n=10,p=0.5,size=(5))
print(x)
# You're now asking to simulate 5 experiments, where:
# Each experiment consists of 10 coin tosses (n=10).
# Each coin toss has a 50% chance of success (heads) (p=0.5).
# You want to run this experiment 5 times (size=5).
sbn.displot(x)
plt.show()

# Difference Between Normal and Binomial Distribution
data={
    "nomral": random.normal(loc=50, scale=5, size=1000),
    "binomial": random.binomial(n=100,p=0.5,size=1000)
}

sbn.displot(data, kind='kde')
plt.show()