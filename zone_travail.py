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

# Fonctions

def is_on_rail (x,y,a,l1,l2):
    R1 = False
    R2 = False
    a_rad= math.radians(a)
    cine_inverse = np.array([[tan(a_rad), 1], [-tan(a_rad), 1]])
    pos_plaqueXY = np.array([[x], [y]])
    sortie = cine_inverse.dot(pos_plaqueXY).flatten()

    # Check longeur rail 1
    if sortie[0] < l1:
        R1 = True

    # Check longeur rail 2
    if x < cos(a_rad)*l2:
        R2 = True

    return R1, R2

COLOR = [['k', 'H.C. All', 'o'], ['tab:red', 'H.C. L1', 'o'], ['tab:blue', 'H.C. L2', 'o'], ['tab:green', 'OK', 'o']]

def get_state_from_r1_r2(R1, R2):
    index = 0

    if R1 is True:
        index += 1
    if R2 is True:
        index += 2

    return COLOR[index]

def plot_result_working_area(result_wa, a ,l1 ,l2 ,_name_file ,mode=tools.PORTRAIT):
    size = 10
    tools.GRAPH_LATEX
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust(left=0.07, bottom=0.1, right=0.9, top=0.88, wspace=0, hspace=0)
    compteur_pt_ok = 0

    for signeX in [-1, 1]:
        for signeY in [-1, 1]:
            for res in result_wa:
                state = get_state_from_r1_r2(res[2], res[3])
                if state[1] is COLOR[-1][1]:
                    compteur_pt_ok += 1
                plt.scatter(signeX*res[0], signeY*res[1], c=state[0], s=size, marker= state[2])

    ax.set(title='Angle des rails de {}°, {} pts couverts / L1={}, L2={}'.format(a, compteur_pt_ok, l1, l2))
    plt.axis('equal')
    plt.gca().set_xlim(-40, 40)

    if SAVE==True:
        tools.save_auto(_name_file)
        # plt.show()
        plt.close()
    else:
        plt.show()

if __name__== '__main__':

    a60 = 60 # angle degrée rail l2
    a45 = 45  # angle degrée rail l2
    a30 = 30  # angle degrée rail l2

    l1 = 76/2 # longueur de sortie limite l1, demi course du rail
    l2 = l1 # longueur de sortie limite l2, demi course du rail

    SAVE = True
    name_file60 = 'zone_travail_{}_pays'.format(a60)
    name_file45 = 'zone_travail_{}_pays'.format(a45)
    name_file30 = 'zone_travail_{}_pays'.format(a30)
    pas = 1
    X = np.arange(0, l1+1, pas)
    Y = np.arange(0, l1+1, pas)

    result60 = []
    result45 = []
    result30 = []
    for x in  X:
        for y in Y:
            R1, R2 = is_on_rail(x, y, a60, l1, l2)
            result60.append([x, y, R1, R2])

    for x in  X:
        for y in Y:
            R1, R2 = is_on_rail(x, y, a45, l1, l2)
            result45.append([x, y, R1, R2])

    for x in  X:
        for y in Y:
            R1, R2 = is_on_rail(x, y, a30, l1, l2)
            result30.append([x, y, R1, R2])

    plot_result_working_area(result60, a60, l1, l2, name_file60, tools.PAYSAGE)
    plot_result_working_area(result45, a45, l1, l2, name_file45, tools.PAYSAGE)
    plot_result_working_area(result30, a30, l1, l2, name_file30, tools.PAYSAGE)