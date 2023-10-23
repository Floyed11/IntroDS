import numpy as np

x = np.linspace(0,100,30)
sample = [9 * i + 8 for i in x]
noise = np.random.standard_normal(30)
sample = sample + noise
print(sample)