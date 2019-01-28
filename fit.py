#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
from sympy import *
import tools

if __name__== '__main__':
    # ratio diamètre outil longueur sortie
    x=[1,2,3,10]
    y=[2.12,2.508,3.06,4.574]
    z = np.polyfit(x, y, 1)
    x1=np.arange(1, 10+0.01, 0.05)
    a=z[0]
    b=z[1]
    y1 = a * x1  + b
    # c = z[2]
    # y2 = a * x1 ** 2 + b * x1+ c
    # d = z[3]
    # y3=a*x1**3+b*x1**2+c*x1+d

    tools.GRAPH_LATEX
    fig, ax = plt.subplots()
    plt.subplots_adjust()

    ax.plot(x, y)
    ax.plot(x1, y1)

    plt.show()

    print(z)

