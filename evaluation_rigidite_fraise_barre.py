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


def pos_x(llimite):
    if llimite>9:
        posX=0
    else:
        posX=llimite+1
    return posX


def graph(mode, _result, _pointinflex, _matiere_name):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust()

    colorbarre='tab:orange'
    colorfraise = 'tab:blue'



    ax.plot(_result[0][0], _result[0][1], label="Longueur fraise {} mm.\nDistance canon {} mm.".format(lfraise[0], lbarre[0]), color=colorbarre)
    ax.plot(_result[1][0], _result[1][1], label="Longueur fraise {} mm.\nDistance canon {} mm.".format(lfraise[1], lbarre[1]), color=colorfraise)
    plt.xlim(0.1,7+0.1)  # adjust the top leaving bottom unchanged
    ax.set(xlabel="Diamètre barre (mm)", ylabel='Rigidité (N/m)', title='Rigidité fraise vs barre {}'.format(_matiere_name))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.grid()

    bbox = tools.boite
    arrowprops90 = dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=90,rad=10")
    arrowprops45 = dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=-60,rad=10")

    xbas = max(_result[0][0])
    ybas = max(_result[0][1])
    offset = 60
    ax.annotate('point changement :\n(%.1f mm; %.1e N/m)' % (xbas, ybas),
                (xbas, ybas), xytext=(2 * offset, offset), textcoords='offset points',
                bbox=bbox, arrowprops=arrowprops90)

    xhaut =_pointinflex[0][0]
    yhaut =_pointinflex[1][0]
    offset = 1
    ax.annotate('point changement :\n(%.1f mm; %.1e N/m)' % (xhaut, yhaut),
                (xhaut, yhaut), xytext=(-10*offset, -100*offset), textcoords='offset points',
                bbox=bbox, arrowprops=arrowprops45)

    #Point intersection
    # ax.plot(llimitefraise, klimit, "or", color=colorfraise)
    # ax.plot(llimitebarre, klimit, "or", color=colorbarre)

    # Draw a default vline at x=... that spans the yrange
    # color = 'tab:red'
    # plt.axhline(y=klimit, color=color)
    # ax.annotate('Limite longueur fraise {} mm.'
    #             .format(round(llimitefraise, 2)), (2, klimit*1.2), textcoords='data', color=colorfraise)
    # ax.annotate('Limite longueur barre {} mm.'
    #             .format(round(llimitebarre, 2)), (2, klimit * 1.4), textcoords='data', color=colorbarre)

    plt.legend(loc='best')
    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()


def compute_trucmuch(_lbarre, _lfraise, _Ebarre, _Efraise = tools.MATIERE["md"]["E"]):

    dbarre = np.arange(0.2, 7 + 0.001, 0.001)  # diamètre barre en mm
    dfraise = np.full(len(dbarre), 2)  # diamètre outil en mm
    # Equations
    Ifraise = moment_quadra(dfraise)
    Ibarre = moment_quadra(dbarre)

    kbarre = []
    kfraise = []
    for i in range(len(_lbarre)):
        kbarre.append(((3 * _Ebarre * Ibarre) / (_lbarre[i] ** 3)) * 1000)
        kfraise.append(((3 * _Efraise * Ifraise) / (_lfraise[i] ** 3)) * 1000)
    k_min = np.minimum(kbarre, kfraise)

    result = [[], []], [[], []]
    for ix, d in enumerate(dbarre):
        if k_min[0][ix] >= k_min[1][ix]:
            result[0][0].append(d)
            result[0][1].append(k_min[0][ix])
        else:
            result[1][0].append(d)
            result[1][1].append(k_min[1][ix])

    resultx = result[1][0]
    resulty = result[1][1]
    dy = np.gradient(resulty)
    ptinflex = np.where(dy == dy.max())
    _pointinflex = [resultx[ptinflex[0][0]]], [resulty[ptinflex[0][0]]]

    return result, _pointinflex


if __name__== '__main__':

    # Variables

    lbarre = [0.3, 5.7] #longueur sortie fraise en mm
    lfraise = [16.5, 4.9] #longueur sortie fraise n état en mm

    keys = set(tools.MATIERE.keys())
    excludes = set(["md"])

    for key in keys.difference(excludes):
        result, pointinflex = compute_trucmuch(lbarre, lfraise, tools.MATIERE[key]["E"])

        SAVE = True
        name_file = 'broche_meyrat_angle_barre_{}'.format(key)
        # Graphique
        graph(tools.PORTRAIT, result, pointinflex, key)


    #Tableau
    print("coco")