import numpy as np
from scipy import stats

salary = [102, 33, 26, 27, 30, 25, 33, 33, 24]

print("Range:", (np.max(salary)-np.min(salary)))

print("Variance:", (np.var(salary)))

print("Std:", (np.std(salary)))

print("Q1:", (np.percentile(salary, 25)))

print("Q2:", (np.percentile(salary, 50)))

print("Q3:", (np.percentile(salary, 75)))

print("IQR:", (stats.iqr(salary)))
