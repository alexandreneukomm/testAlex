from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sympy import *

#if __name__== '__main__':
a = 45
a= math.radians(a)

Y1min = 0
Y1max = 76
Y1min = Y1min
Y2max = Y1max
pas = np.arange(0, Y1max + 0.1, 5)




cine_inverse = np.array([[tan(a), 1], [-tan(a), 1]])

Y1 = []

for n_i in pas:
    Y1.append(pas)

pos_mot = np.array([Y1,[]])
#
# plaqueXY = np.array([[],[]])
#
# plaqueXY = cine_inverse.dot(pos_mot)

print(pos_mot)
