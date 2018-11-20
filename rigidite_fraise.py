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


def graph(mode=tools.PORTRAIT):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust()

    ax.plot(x, y1, label="Force de {} N".format(F1))
    ax.plot(x, y2, label="Force de {} N".format(F2))
    ax.set(xlabel="Longueur sortie outil (mm)", ylabel='Déflexion (mm)', title='Flexion outil diamètre {} mm'.format(d))
    plt.grid()

    # Draw a default vline at x=... that spans the yrange
    color = 'tab:red'
    plt.axvline(x=llimite, color=color)
    ax.annotate(
        'Limite de rigidité de $1 \cdot 10^{} N/m$. \n'
        'Longueur de sortie de la fraise {} mm. \n'
        'Rapport longueur / diamètre: {}'.format(expok, llimite,rapport),
        (pos_x(llimite), (max(y1) - min(y1))/2), textcoords='data', color=color, bbox=tools.boite)

    plt.legend(loc='best')
    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

if __name__== '__main__':

    # Variables
    x = np.arange(0.0, 15.0+1, 0.1) #longueur sortie fraise en mm
    E = tools.MATIERE["md"]["E"] #module de Young carbure de tungstène en MPa
    d = 3 #diamètre outil en mm
    F1 = 30 #force en N
    F2 = 5 #force en N
    expok = 7
    klimit = 1*10**expok

    SAVE = False
    name_file = 'flexion_fraise_{}'.format(d)

    #Equations
    I= (np.pi*d**4)/64
    y1=(F1*x**3)/(3*E*I)
    y2=(F2*x**3)/(3*E*I)
    llimite=round(((3*E*10**6*I/10**12)/(klimit))**(1/3)*1000,2)
    rapport=round(llimite/d,2)

    #Graphique

    graph(tools.PORTRAIT)

    #Tableau