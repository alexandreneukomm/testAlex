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
    ax.text(-10, -10, 0, "Zone de travail", color='k')

    # cercle de la course course
    plt.plot(courseX, courseY, c="k", marker='.', linestyle=':')

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
    courseX = [0,-26.87,-26.87,0,26.87,26.87,0]
    courseY = [-38, -11.13, 11.13, 38, 11.13, -11.13,-38]

        # Liste vide
    X = []
    Y = []
    rigiX = []
    rigiY = []
    rigiZ = []

        # OK
    posX = courseX[0]
    posY = courseY[0]
    deplaX = 3.025e-5
    deplaY = 2.645e-5
    deplaZ = 3.351e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

    # OK
    posX = courseX[1]
    posY = courseY[1]
    deplaX = 5.42e-5
    deplaY = 3.577e-5
    deplaZ = 1.59e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

    posX = courseX[2]
    posY = courseY[2]
    deplaX = 8.812e-5
    deplaY = 3.577e-5
    deplaZ = 7.515e-5

    print(deplaZ)

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)
    # OK
    posX = courseX[3]
    posY = courseY[3]
    deplaX = 1.46e-4
    deplaY = 2.645e-5
    deplaZ = 4.489e-5

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

    posX = courseX[4]
    posY = courseY[4]
    deplaX = 8.812e-5
    deplaY = 3.577e-5
    deplaZ = 7.515e-5


    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # OK
    posX = courseX[5]
    posY = courseY[5]
    deplaX = 5.42e-5
    deplaY = 3.577e-5
    deplaZ = 1.59e-4

    calcul_rigi(deplaX, deplaY, deplaZ, posX, posY)

        # OK
    posX = courseX[6]
    posY = courseY[6]
    deplaX = 3.025e-5
    deplaY = 2.645e-5
    deplaZ = 3.351e-4

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
    graph(3e13, tools.PAYSAGE)
    name_file = 'rigidite_plaque_XY_zoom'
    graph(3.2e6, tools.PAYSAGE)

