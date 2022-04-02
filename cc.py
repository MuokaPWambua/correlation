

import numpy as np
from matplotlib import pyplot as plt
from statistics import mean

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)

    return np.dot(de_mean(x), de_mean(y)) / (n-1)

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
correlation = np.corrcoef(pageSpeeds, purchaseAmount)

print(f'coveriance: {covariance (pageSpeeds, purchaseAmount)}')
print(f'correlation: {correlation}')
