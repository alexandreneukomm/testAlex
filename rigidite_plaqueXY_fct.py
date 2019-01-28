#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
from sympy import *
import os
import tools


# Fonction

def calcul_rigi(a,b,c,d,e):
    Xrigi = f / (a / 1000)
    Yrigi = f / (b / 1000)
    Zrigi = f / (c / 1000)
    rigiX.append(Xrigi)
    rigiY.append(Yrigi)
    rigiZ.append(Zrigi)
    X.append(d)
    Y.append(e)

def graph(f,mode):
    tools.GRAPH_LATEX
    fig = plt.figure(figsize=mode)
    plt.subplots_adjust(left=-0.02, bottom=0, right=1, top=0.88, wspace=0, hspace=0)
    #ax = fig.add_subplot(111, projection="3d")
    ax= fig.gca(projection="3d")
    ax.set(xlabel="Position sur l'axe X (mm)", ylabel="Position sur l'axe Y (mm)", zlabel="Rigidité (N/m)",
           title='Espace de rigidité')

    # ax.ticklabel_format(axis='z', style='scientific', scilimits=(-1, 2))
    if f>2e7 :
        ax.scatter(X, Y, rigiX, label="Direction X", marker='^', alpha=1)
        ax.scatter(X, Y, rigiY, label="Direction Y", marker='+', alpha=1)
        ax.scatter(X, Y, rigiZ, label="Direction Z", marker='o', alpha=1, c="g")
        ax.plot(X, Y, rigiX)
        ax.plot(X, Y, rigiY)
        ax.plot(X, Y, rigiZ, c="g")
        ax.text2D(0.1, 0.8, "Rigidité max: {} N/m en X \nRigidité min: {} N/m en Z\nRapport rigidité max/min: \nX {} \nY {} \nZ {} \nTotal {}".format(maxmax,minmin,rappX, rappY, rappZ, rappmax), transform=ax.transAxes)
    else:
        ax.scatter(X, Y, rigiZ, label="Direction Z", marker='o', alpha=1, c="g")
        ax.plot(X, Y, rigiZ, c="g")
        ax.text2D(0.1, 0.8, "Rigidité max {} N/m \nRigidité min {} N/m \nRapport rigidité max/min: \nZ {}".format(zmax,zmin,rappZ), transform=ax.transAxes)

    # plt.gca().set_zlim(0, f)

    # anotation
    ax.text(-10, -15, 0, "Zone de travail simplifiée", color='k')

    # cercle de la course course
    plt.plot(27 * np.cos(an), 27 * np.sin(an), c="k", marker='.', linestyle=':')

    plt.legend(loc='best')

    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()


if __name__ == "__main__":

    # Variables

    SAVE = True
    name_file = 'rigidite_plaque_XY'

    f = 1e6  # force en simulation en N
    an = np.linspace(0, 2 * np.pi, 72)

        # Liste vide
    X = []
    Y = []
    rigiX = []
    rigiY = []
    rigiZ = []

        # Simulation 1 a X0 Y-27
    posX = 0
    posY = -27
    deplaX = 5.1e-5
    deplaY = 5.2e-5
    deplaZ = 1e-3

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 2 a X19 Y-19
    posX = 19.1
    posY = -19.1
    deplaX = 4.8e-5
    deplaY = 5.4e-5
    deplaZ = 9.6e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)


        # Simulation 3 a X27 Y0
    posX = 27
    posY = 0
    deplaX = 4.2e-5
    deplaY = 5.5e-5
    deplaZ = 6.3e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 4 a X19 Y-19
    posX = 19.1
    posY = 19.1
    deplaX = 3.9e-5
    deplaY = 5.4e-5
    deplaZ = 3.9e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 5 a X0 Y27
    posX = 0
    posY = 27
    deplaX = 3.8e-5
    deplaY = 5.2e-5
    deplaZ = 3.2e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 6 a X19 Y-19
    posX = -19.1
    posY = 19.1
    deplaX = 3.9e-5
    deplaY = 5.4e-5
    deplaZ = 3.9e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 3 a X27 Y0
    posX = -27
    posY = 0
    deplaX = 4.2e-5
    deplaY = 5.5e-5
    deplaZ = 6.3e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 2 a X19 Y-19
    posX = -19.1
    posY = -19.1
    deplaX = 4.8e-5
    deplaY = 5.4e-5
    deplaZ = 9.6e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # Simulation 1 a X0 Y-27
    posX = 0
    posY = -27
    deplaX = 5.1e-5
    deplaY = 5.2e-5
    deplaZ = 1e-3

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # calculs rigi

    xmax=max(rigiX)
    xmin=min(rigiX)
    ymax=max(rigiY)
    ymin=min(rigiY)
    zmax=max(rigiZ)
    zmin=min(rigiZ)

    # xmax="%10.2e"%(xmax)

    rappX = round((xmax/xmin), 2)
    rappY = round((ymax/ymin), 2)
    rappZ = round((zmax/zmin), 2)

    xmax = ("%10.1e" % (xmax))
    xmin = ("%10.1e" % (xmin))
    ymax = ("%10.1e" % (ymax))
    ymin = ("%10.1e" % (ymin))
    zmax = ("%10.1e" % (zmax))
    zmin = ("%10.1e" % (zmin))

    maxmax = max(max(rigiX), max(rigiY), max(rigiZ))
    minmin = min(min(rigiX), min(rigiY), min(rigiZ))
    rappmax = round(maxmax/minmin, 2)

    maxmax = ("%10.1e" % (maxmax))
    minmin = ("%10.1e" % (minmin))

    # formattedList = ["%10.1e" % member for member in rigiZ]


        # Graphiques
    graph(3e7, tools.PAYSAGE)
    name_file = 'rigidite_plaque_XY_zoom'
    graph(3.2e6, tools.PAYSAGE)

