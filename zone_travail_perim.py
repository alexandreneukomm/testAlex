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

def perim(_l1,_a):

    grandpan = _l1
    petitpan = (_l1 * 2 - (2 * ((_l1 ** 2) - (l1 * cos(math.radians(_a))) ** 2) ** (1 / 2)))

    p = 4*grandpan + 2* petitpan

    return p


def graph(_result60, _result45, _result30, _l1, mode=tools.PORTRAIT):

    tools.GRAPH_LATEX
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust(bottom=0.12)

    pente60 = round((_result60[0][3]-_result60[0][2])/(_l1[3] - _l1[2]),1)
    pente45 = round((_result45[0][3] - _result45[0][2]) / (_l1[3] - _l1[2]),1)
    pente30 = round((_result30[0][3] - _result30[0][2]) / (_l1[3] - _l1[2]),1)


    ax.plot(_l1, _result30[0], label="Angle des rails de 30° pente de {}".format(pente30))
    ax.plot(_l1, _result45[0], label="Angle des rails de 45° pente de {}".format(pente45))
    ax.plot(_l1, result60[0], label="Angle des rails de 60° pente de {}".format(pente60))

    ax.set(xlabel="Demi course rail L1 et L2 (mm)", ylabel='Périmètre de la zone de travail (mm)', title='Evolution périmètre fonction de la course')
    # plt.xticks(np.arange(0, max(FZ)+0.1, 0.1))
    # plt.gca().set_xlim(0, 40)
    # plt.gca().set_ylim(0, 350)
    plt.grid()
    #
    # # Draw a default vline at x=... that spans the yrange

    # color = 'tab:brown'
    # plt.axhline(y=fzlimit, color=color)
    # ax.annotate( '{} (mm/min)'.format(fzlimit), (0, fzlimit + 2500), textcoords='data', color=color, bbox=dict(boxstyle="round", fc="w"))

    plt.legend(loc='best')

    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

if __name__== '__main__':
    result = []

    a60 = 60 # angle degrée rail l2
    a45 = 45  # angle degrée rail l2
    a30 = 30  # angle degrée rail l2

    l1 = np.arange(30, 40+1, 1) # longueur de sortie limite l1, demi course du rail
    l2 = l1 # longueur de sortie limite l2, demi course du rail
    SAVE = True
    name_file = 'perim'

    result60 = []
    permietre = perim(l1, a60)
    result60.append(permietre)

    result45 = []
    # for y in l1:
    permietre = perim(l1, a45)
    result45.append(permietre)

    result30 = []
    # for y in l1:
    permietre = perim(l1, a30)
    result30.append(permietre)

    graph(result60, result45, result30, l1)