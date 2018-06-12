import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

'''
    temp_max : numpy array consisting all the max temperatures
    temp_min : numpy array consisting all the min temperatures
    months   : numpy array range from 0 to 11
'''
temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])
months = np.arange(12)


def yearly_temps(times, avg, amplitude, time_offset):
    return avg + amplitude * np.cos((times + time_offset) * 2 * np.pi / times.max())


res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      temp_max)
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      temp_min)

days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')
plt.show()
