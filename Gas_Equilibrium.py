# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:07:08 2016

@author: AB Sanyal
"""

import matplotlib.pyplot as plt
import numpy as np

N = 1 * 1000000

t = 3 * 1000000

blue_box = N
red_box = 0

blue_size = 1
red_size = 1

c_blue = []
c_red = []

i = 1
print("Started calculations.")
while (i <= t):
    r = np.random.uniform(0, 1)
    if (blue_box > 0 and r < blue_box/(N * blue_size)):
        blue_box -= 1
        red_box += 1
    r = np.random.uniform(0, 1)
    if (red_box > 0 and r < red_box/(N * red_size)):
        red_box -= 1
        blue_box += 1
    c_blue.append(blue_box)
    c_red.append(red_box)
    if (i % 1000000 == 0):
        print("Finished calculations for " + str(i) + " time-steps.")
    i += 1

plt.plot(c_blue, 'b')
plt.plot(c_red, 'r')
plt.show()
