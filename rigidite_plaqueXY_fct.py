from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import *
import os
import tools


# Fonction

def calcul_rigi(a,b,c,d,e):
    Xrigi = round(f / (a* 1000),0)
    Yrigi = f / (b * 1000)
    Zrigi = f / (c * 1000)
    rigiX.append(Xrigi)
    rigiY.append(Yrigi)
    rigiZ.append(Zrigi)
    X.append(d)
    Y.append(e)

def graph(f,mode):
    fig = plt.figure(figsize=mode)
    plt.subplots_adjust(left=-0.02, bottom=0, right=1, top=0.88, wspace=0, hspace=0)
    #ax = fig.add_subplot(111, projection="3d")
    ax= fig.gca(projection="3d")
    ax.set(xlabel="Position sur l'axe des X (mm)", ylabel="Position sur l'axe des Y (mm)", zlabel="Rigidité (N/m)",
           title='Espace de rigidité')

    # ax.ticklabel_format(axis='z', style='scientific', scilimits=(-1, 2))
    if f>2e7 :
        ax.scatter(X, Y, rigiX, label="Direction X", marker='^', alpha=1)
        ax.scatter(X, Y, rigiY, label="Direction Y", marker='+', alpha=1)
        ax.scatter(X, Y, rigiZ, label="Direction Z", marker='o', alpha=1, c="g")
        ax.plot(X, Y, rigiX)
        ax.plot(X, Y, rigiY)
        ax.plot(X, Y, rigiZ, c="g")
        ax.text2D(0.05, 0.95, "Rapport rigidité max/min: \n X {} \n Y {} \n Z {} \n Total {} ".format(rappX, rappY, rappZ, rappmax), transform=ax.transAxes)
    else:
        ax.scatter(X, Y, rigiZ, label="Direction Z", marker='o', alpha=1, c="g")
        ax.plot(X, Y, rigiZ, c="g")
        ax.text2D(0.05, 0.95, "Rapport rigidité max/min: \n Z {}".format(rappZ), transform=ax.transAxes)

    plt.gca().set_zlim(0, f)

    # anotation
    ax.text(0, 0, 0, "Course de la machine", color='k')

    # cercle de la course course
    plt.plot(27 * np.cos(an), 27 * np.sin(an), c="k", marker='.', linestyle=':')

    plt.legend(loc='best')


# Variables

SAVE = False
name_file = 'zone_travail__pays'

portrait = (7, 4)
paysage = (9.2, 5.8)
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

rappX = round(max(rigiX)/min(rigiX), 2)
rappY = round(max(rigiY)/min(rigiY), 2)
rappZ = round(max(rigiZ)/min(rigiZ), 2)

maxmax = max(max(rigiX), max(rigiY), max(rigiZ))
minmin = min(min(rigiX), min(rigiY), min(rigiZ))
rappmax = round(maxmax/minmin, 2)

# print(rigiX)
    # Graphiques
graph(3e7, tools.PAYSAGE)
graph(3.2e6, tools.PAYSAGE)

plt.show()
    # Création de tableau
    # col1="Position X (mm)"
    # col2="Position Y (mm)"
    # col3="Rigidit\\'e X"
    # col4="Rigidit\\'e Y"
    # col5="Rigidit\\'e Z"
    #
    # df = pd.DataFrame({col1 : X, col2:Y, col3:rigiX,col4:rigiY,col5:rigiZ})
    # pd.options.display.float_format = '{:.2E}'.format
    # print(df)
    # with open("rigiXY.tex", "w") as f:
    #     f.write("\\begin{tabular}{|" + " | ".join(["c"] * len(df.columns)) + "|""}\n")
    #     f.write(col1 + " & "+ col2 + " & "+ col3 + " & "+ col4 + " & "+ col5 + " \\\\\n")
    #     for i, row in df.iterrows():
    #         f.write("\\hline")
    #         f.write(" & ".join([str(x) for x in row.values]) + " \\\\\n")
    #     f.write("\\end{tabular}")