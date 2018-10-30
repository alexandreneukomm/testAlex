#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
from sympy import *
import tools

def moment_quadra(d,I):
    I=(np.pi * d ** 4) / 64
    return I

def pos_x(llimite):
    if llimite>9:
        posX=0
    else:
        posX=llimite+1
    return posX


def graph(mode):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust()

    colorbarre='tab:orange'
    colorfraise = 'tab:blue'

    ax.plot(lbarre, kbarre, label="Rigidité barre acier diamètre {} mm".format(dbarre), color=colorbarre)
    ax.plot(lfraise, kfraise, label="Rigidité fraise métal dur diamètre {} mm".format(dfraise), color=colorfraise)
    plt.ylim(ymax=klimit*2,ymin=klimit/5)  # adjust the top leaving bottom unchanged
    ax.set(xlabel="Longueur sortie barre/fraise (mm)", ylabel='Rigidité (N/m)', title='Rigidité limite de ${} \cdot 10^{}$ N/m barre - fraise'.format(valk, expok))
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.grid()

    #Point intersection
    ax.plot(llimitefraise, klimit, "or", color=colorfraise)
    ax.plot(llimitebarre, klimit, "or", color=colorbarre)

    # Draw a default vline at x=... that spans the yrange
    color = 'tab:red'
    plt.axhline(y=klimit, color=color)
    ax.annotate('Limite longueur fraise {} mm.'
                .format(round(llimitefraise, 2)), (2, klimit*1.2), textcoords='data', color=colorfraise)
    ax.annotate('Limite longueur barre {} mm.'
                .format(round(llimitebarre, 2)), (2, klimit * 1.4), textcoords='data', color=colorbarre)

    plt.legend(loc='best')
    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

if __name__== '__main__':

    # Variables
    lbarre = np.arange(0.1, 12+0.01, 0.01) #longueur sortie fraise en mm
    lfraise = np.arange(0.1, 12+0.01, 0.01) #longueur sortie fraise en mm

    Ebarre = tools.MATIERE["acier"]["E"] # module de Young laiton en MPa
    Efraise= tools.MATIERE["md"]["E"] #module de Young carbure de tungstène en MPa

    dbarre = 2.6 #diamètre barre en mm
    dfraise = 1 #diamètre outil en mm

    expok=7
    valk=1
    klimit=valk*10**expok

    SAVE = False
    name_file = 'flexion_fraise_{}_barre_{} '.format(dfraise,dbarre)

    #Equations

    Ifraise=(np.pi * dfraise ** 4) / 64
    Ibarre=(np.pi * dbarre ** 4) / 64
    # moment_quadra(dfraise,Ifraise)
    # moment_quadra(dbarre,Ibarre)
    kbarre=((3*Ebarre*Ibarre)/(lbarre**3))*1000
    kfraise = (3 * Efraise * Ifraise) / (lfraise ** 3)*1000
    llimitefraise=((3*Efraise*Ifraise*1000)/(klimit)) ** (1 / 3)
    llimitebarre = ((3 * Ebarre * Ibarre*1000) / (klimit)) ** (1 / 3)

    #Graphique

    graph(tools.PORTRAIT)

    #Tableau