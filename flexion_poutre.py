#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
from sympy import *
import tools

def moment_quadra(d):
    result = ((np.pi * d ** 4) / 64)
    return result


if __name__== '__main__':

    # Variables

    dbarre = 5  # diamètre barre en mm
    lbarre = np.arange(0.1, 5+0.01, 1)
    Ebarre = tools.MATIERE["acier"]["E"]  # module de Young laiton en MPa
    Ibarre=moment_quadra(dbarre)

    k=[]

    k=(((3 * Ebarre * Ibarre) / (lbarre ** 3)* 1000) )

    #print("{:.2e}".format(k))
    print(k)