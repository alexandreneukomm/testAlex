#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
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

def plot_result_working_area(result_wa, a ,l1 ,l2 ,mode):
    size = 10
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust(left=0.07, bottom=0.1, right=0.9, top=0.88, wspace=0, hspace=0)
    compteur_pt_ok = 0

    for signeX in [-1,1]:
        for signeY in [-1,1]:
            for res in result_wa:
                state = get_state_from_r1_r2(res[2], res[3])
                if state[1] is COLOR[-1][1]:
                    compteur_pt_ok += 1
                plt.scatter(signeX*res[0], signeY*res[1], c=state[0], s=size, marker= state[2])


    #plt.legend(('Model length', 'Data length', 'Total message length'), loc='best')
    ax.set(title='Angle des rails de {}°, {} pts couverts / L1={}, L2={}'.format(a, compteur_pt_ok, l1, l2))
    plt.axis('equal')
    plt.gca().set_xlim(-40, 40)

    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

if __name__== '__main__':
    a = 45 # angle degrée rail l2
    l1 = 42 # longueur de sortie limite l1
    l2 = 38.2 # longueur de sortie limite l2
    SAVE = False
    name_file = 'zone_travail_{}_pays'.format(a)
    pas = 1
    X = np.arange(0, 42+1, pas)
    Y = np.arange(0, 42+1, pas)

    result = []
    for x in  X:
        for y in Y:
            R1, R2 = is_on_rail(x, y, a, l1, l2)
            result.append([x, y, R1, R2])

    plot_result_working_area(result, a, l1, l2, tools.PAYSAGE)

    # fig, ax = plt.subplots()
    # plt.subplots_adjust()
    # plt.plot(X, Y)
    # ax.set(title='Angle des rails de {}°'.format(a))
    # plt.axis('equal')
    # plt.show()