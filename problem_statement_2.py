import numpy as np
import matplotlib.pyplot as plt

temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])
months = np.arange(12)
plt.plot(months,temp_max,'ro')
plt.plot(months,temp_min,'bo')
plt.xlabel('Month')
plt.ylabel('Min and Max temperatures')

