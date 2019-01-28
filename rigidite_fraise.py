#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
from sympy import *
import tools

def pos_x(llimite):
    if llimite>9:
        posX=0
    else:
        posX=llimite+0.5
    return posX

def moment_quadra_cylindre(_diametre):
    result = ((np.pi * _diametre ** 4) / 64)
    return result



def graph(mode=tools.PORTRAIT):
    tools.GRAPH_LATEX
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust(left=0.14, bottom=0.13, right=0.95)

    ax.plot(lbarre, k1, label="Ø {} mm".format(dfraise1))
    ax.plot(lbarre, k2, label="Ø {} mm".format(dfraise2))
    ax.plot(lbarre, k3, label="Ø {} mm".format(dfraise3))
    ax.set(xlabel="Longueur sortie outil (mm)", ylabel='Rigidité (N/m)', title='Rigidité outils axiaux fonction de la longueur de sortie')
    plt.ylim(klimite-3000000, klimite+10000000)
    plt.xlim(0, 10)

    plt.grid()
    color = 'tab:red'
    plt.axhline(y=klimite, color=color)
    ax.annotate('Limite longueur: \n{} mm\n{} mm\n{} mm'
                .format(round(llimitefraise1, 2),round(llimitefraise2, 2),round(llimitefraise3, 2)), (0.5, klimite*1.6), textcoords='data', bbox=tools.boite)

    plt.legend(loc='best')
    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

if __name__== '__main__':

    # Variables

    dfraise1 = 1  # diamètre fraise en mm
    dfraise2 = 2  # diamètre fraise en mm
    dfraise3 = 3  # diamètre fraise en mm
    lbarre = np.arange(0.01, 12+0.01, 0.1)
    Efraise = tools.MATIERE["md"]["E"]  # module de Young md en MPa
    expok = 7
    valk = 1
    klimite = valk*10**expok


    SAVE = False
    name_file = 'rigi_fraise'

    # Equation

    Ifraise1= moment_quadra_cylindre(dfraise1)
    Ifraise2 = moment_quadra_cylindre(dfraise2)
    Ifraise3 = moment_quadra_cylindre(dfraise3)

    k1 = (((3 * Efraise * Ifraise1) / (lbarre ** 3)* 1000) )
    k2 = (((3 * Efraise * Ifraise2) / (lbarre ** 3) * 1000))
    k3 = (((3 * Efraise * Ifraise3) / (lbarre ** 3) * 1000))

    llimitefraise1 = ((3 * Efraise * Ifraise1 * 1000) / (klimite)) ** (1 / 3)
    llimitefraise2 = ((3 * Efraise * Ifraise2 * 1000) / (klimite)) ** (1 / 3)
    llimitefraise3 = ((3 * Efraise * Ifraise3 * 1000) / (klimite)) ** (1 / 3)
    #Graphique

    graph(tools.PORTRAIT)