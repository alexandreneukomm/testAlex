#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
import math
from sympy import *
from random import*
import tools


#variable

J = 1.29e-5 #kg*m^2
p = 0.01 #m
m1 = 3.1 #kg
mp = 3.5 #kg
theta = 45 #deg
theta_rad= math.radians(theta) #radian
xdd = 0 #m/s^2
ydd = 0 #m/s^2
cine = np.array([[tan(theta_rad), 1], [-tan(theta_rad), 1]])
masse = np.array([m1+(mp/2)])
acc = np.array([xdd,ydd])

fx1 = 1 #N
fy1 = 0 #N

fx2 = 10 #N
fy2 = 0 #N

force1 = np.array([fx1,fy1])
force2 = np.array([fx2,fy2])

couple1 = J + (p/2*math.pi)*masse*(2*math.pi/p)*cine.dot(acc)-(0.5*p/2*math.pi)*cine.dot(force1)
couple2 = J + (p/2*math.pi)*masse*(2*math.pi/p)*cine.dot(acc)-(0.5*p/2*math.pi)*cine.dot(force2)

print(couple1.flatten())
print(couple2.flatten())

print(fx1*100/fx2)