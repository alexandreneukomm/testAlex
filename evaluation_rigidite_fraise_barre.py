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


def graphsimple(mode, _result, _pointinflex, _lfraise, _lbarre, _name_file,_matiere_name):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax = plt.subplots(figsize=mode)
    # plt.subplots_adjust(left=0.1, bottom=0.12, right=0.97, top=0.88, wspace=0, hspace=0)

    colorbarre='tab:orange'
    colorfraise = 'tab:blue'

    ax.plot(_result[0][0], _result[0][1], label="Longueur fraise {} mm.\nDistance canon {} mm.".format(_lfraise[0], _lbarre[0]), color=colorbarre)
    ax.plot(_result[1][0], _result[1][1], label="Longueur fraise {} mm.\nDistance canon {} mm.".format(_lfraise[1], _lbarre[1]), color=colorfraise)
    plt.xlim(0.1, 7+0.1)  # adjust the top leaving bottom unchanged
    plt.ylim(0e5, 2.9e7)
    ax.set(xlabel="Diamètre barre (mm)", ylabel='Rigidité (N/m)', title='Rigidité fraise vs barre {}'.format(_matiere_name))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.grid()

    bbox = tools.boite
    arrowprops90 = dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=90,rad=10")
    arrowprops45 = dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=-60,rad=1")

    xbas = max(_result[0][0])
    ybas = max(_result[0][1])

    offset = 7
    ax.annotate('point changement :\n%.1f mm; %.1e N/m' % (xbas, ybas),
                (xbas, ybas), xytext=(-9 * offset, 8*offset), textcoords='offset points',
                bbox=bbox, arrowprops=arrowprops90)

    xhaut =_pointinflex[0][0]
    yhaut =_pointinflex[1][0]
    offset = 3
    ax.annotate('point changement :\n%.1f mm; %.1e N/m' % (xhaut, yhaut),
                (xhaut, yhaut), xytext=(6*offset, -20*offset), textcoords='offset points',
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
        tools.save_auto(_name_file)
        # plt.show()
        plt.close()
    else:
        plt.show()

def graphcumuler(mode, _result1, _result2, _result3, _matiere_name):
    tools.GRAPH_LATEX
    fig, ax = plt.subplots(figsize=mode)
    # plt.subplots_adjust(left=0.1, bottom=0.12, right=0.97, top=0.88, wspace=0, hspace=0)

    colordentiste='tab:green'
    colormeyratmhf = 'tab:blue'
    colormeyratangle = 'tab:red'

    ax.plot(_result2[0][0], _result2[0][1],label="Broche dentaire", color=colordentiste)
    ax.plot(_result2[1][0], _result2[1][1], color=colordentiste)


    ax.plot(_result3[0][0], _result3[0][1], label="Broche Meyrat MHF 20", color=colormeyratmhf)
    ax.plot(_result3[1][0], _result3[1][1], color=colormeyratmhf)

    ax.plot(_result1[0][0], _result1[0][1], label="Broche Meyrat renvoi angle", color=colormeyratangle)
    ax.plot(_result1[1][0], _result1[1][1], color=colormeyratangle)


    plt.xlim(0.1, 7+0.1)  # adjust the top leaving bottom unchanged
    plt.ylim(0e5, 2.9e7)
    ax.set(xlabel="Diamètre barre (mm)", ylabel='Rigidité (N/m)', title='Comparaison diverses broches {}'.format(_matiere_name))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.grid()

    plt.legend(loc='best')
    if SAVE==True:
        tools.save_auto(name_file_cumuler)
        # plt.show()
        plt.close()
    else:
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

    #meyrat angle
    lbarre1 = [0.3, 5.7] #longueur sortie fraise en mm
    lfraise1 = [16.5, 4.9] #longueur sortie fraise n état en mm

    #dentiste
    lbarre2 = [0.3, 4.2] #longueur sortie fraise en mm
    lfraise2 = [10.3, 3.8] #longueur sortie fraise n état en mm

    #meyrat MHF 20
    lbarre3 = [0.3, 5.2] #longueur sortie fraise en mm
    lfraise3 = [10.3, 3.8] #longueur sortie fraise n état en mm

    keys = set(tools.MATIERE.keys())
    excludes = set(["md"])

    for key in keys.difference(excludes):
        result1, pointinflex1 = compute_trucmuch(lbarre1, lfraise1, tools.MATIERE[key]["E"])
        result2, pointinflex2 = compute_trucmuch(lbarre2, lfraise2, tools.MATIERE[key]["E"])
        result3, pointinflex3 = compute_trucmuch(lbarre3, lfraise3, tools.MATIERE[key]["E"])

        SAVE = True
        name_file1 = 'broche_meyrat_angle_barre_{}'.format(key)
        name_file2 = 'broche_dentiste_barre_{}'.format(key)
        name_file3 = 'broche_meyrat_barre_{}'.format(key)
        name_file_cumuler = 'broches_cumuler_{}'.format(key)
        # Graphique

        graphsimple(tools.PORTRAIT, result1, pointinflex1, lfraise1, lbarre1, name_file1, key)
        graphsimple(tools.PORTRAIT, result2, pointinflex2, lfraise2, lbarre2, name_file2, key)
        graphsimple(tools.PORTRAIT, result3, pointinflex3, lfraise3, lbarre3, name_file3, key)

        graphcumuler(tools.PORTRAIT, result1, result2, result3, key)


    #Tableau
    print("coco")