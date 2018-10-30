#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import pandas as pd
from sympy import *
import tools

def pos_x(llimite):
    if llimite>2:
        posX=0
    else:
        posX=llimite+1
    return posX

def moment_flexion_rectangle(b, h):
    I = b*h**3
    return I

def graph(mode):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust()


    ax.plot(l, y1, label="Hauteur plaquette {} mm".format(h))
    ax.plot(l, y2, label="Largeur plaquette {} mm".format(b))
    ax.set(xlabel="Longueur coupe plaquette (mm)", ylabel='Déflexion (pour une force de {} N) (mm)'.format(F1),
           title='Comparaison rigidité hauteur - largeur plaquette {} - {} mm'.format(h, b))
    plt.grid()

    # Draw a default vline at x=... that spans the yrange
    color = 'tab:orange'
    plt.axvline(x=llimite, color=color)
    ax.annotate(
        'Limite de rigidité de $1 \cdot 10^{} N/m$ pour largeur de {} mm.\n'
        'Longueur sortie de la plaquette {} mm.\n'
        'Rapport longueur / largeur: {}.'.format(expok, b, llimite, rapport),
        (pos_x(llimite), ((max(y2) - min(y2))/7)*4), textcoords='data', color=color, bbox=tools.boite)

    plt.legend(loc='best')
    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

if __name__== '__main__':

    # Variables
    l = np.arange(0.0, 4.0+0.1, 0.1) #longueur sortie fraise en mm
    E=650000 #module de Young carbure de tungstène en MPa
    b=0.8 #largeur plaquette
    h=6 #hauteur de la plaquette
    F1=100 #force en N
    expok=7
    klimit=1*10**expok

    SAVE = True
    name_file = 'flexion_plaquette'

    #Equations
    #moment_flexion_rectangle(b,h)
    Ix = (b * h ** 3)/12
    Iy = (h * b ** 3)/12

    y1=(F1*l**3)/(3*E*Ix)
    y2 = (F1 * l ** 3) / (3 * E * Iy)
    llimite=round(((3*E*10**6*Iy/10**12)/(klimit))**(1/3)*1000,2)
    rapport=round(llimite/b,2)

    #Graphique

    graph(tools.PORTRAIT)

    #Tableau