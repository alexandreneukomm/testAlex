#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rcParams
import numpy as np
import pandas as pd
from sympy import *
import os
import tools

# Fonctions

def ajout(a,b,c,d,e):
    ListeSurface45.append(a)
    ListeSurface30.append(b)
    ListeSurface60.append(c)
    ListeL1.append(d)
    ListeL2.append(e)

def graph(mode):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig = plt.figure(figsize=mode)
    plt.subplots_adjust(left=0, bottom=0, right=0.93, top=0.96, wspace=0, hspace=0)
    #ax = fig.add_subplot(111, projection="3d")
    ax= fig.gca(projection="3d")
    ax.set(xlabel="Longueur rail L1 (mm)", ylabel="Longueur rail L2 (mm)", zlabel="Surface couverte (points)",
           title='Zone de travail')

    ax.plot_trisurf(ListeL1, ListeL2, ListeSurface30, alpha=0.5)
    ax.plot_trisurf(ListeL1, ListeL2, ListeSurface45, alpha=0.5)
    ax.plot_trisurf(ListeL1, ListeL2, ListeSurface60, alpha=0.5)
        # ax.plot(X, Y, rigiX)
        # ax.plot(X, Y, rigiY)
        # ax.plot(X, Y, rigiZ, c="g")
        # ax.text2D(0.05, 0.95, "Rapport rigidité max/min: \n X {} \n Y {} \n Z {} \n Total {} ".format(rappX, rappY, rappZ, rappmax), transform=ax.transAxes)

    fake2Dline30 = mpl.lines.Line2D([0], [0], linestyle="none", c='tab:blue', marker='o')
    fake2Dline45 = mpl.lines.Line2D([0], [0], linestyle="none", c='tab:orange', marker='o')
    fake2Dline60 = mpl.lines.Line2D([0], [0], linestyle="none", c='tab:green', marker='o')
    ax.legend([fake2Dline30,fake2Dline45,fake2Dline60], ['Angle de 30°','Angle de 45°','Angle de 60°'], numpoints=1, loc='upper left')

    # anotation

    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

# Variables
if __name__== '__main__':
    SAVE = False
    name_file = 'zone_travail_opti'

        # Liste vide
    ListeL1 = []
    ListeL2 = []
    ListeSurface45 = []
    ListeSurface30 = []
    ListeSurface60 = []

        # Simulation 1 a L1 35 L2 35
    L1 = 35
    L2 = 35
    Surface45 = 2300
    Surface30 = 3324
    Surface60 = 1496

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 2 a X19 Y-19
    L1 = 37
    L2 = 35
    Surface45 = 2500
    Surface30 = 3572
    Surface60 = 1640

    ajout(Surface45, Surface30, Surface60, L1, L2)


        # Simulation 3 a X27 Y0
    L1 = 39
    L2 = 35
    Surface45 = 2700
    Surface30 = 3820
    Surface60 = 1784

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 4 a X19 Y-19
    L1 = 41
    L2 = 35
    Surface45 = 2900
    Surface30 = 4068
    Surface60 = 1928

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 5 a X0 Y27
    L1 = 43
    L2 = 35
    Surface45 = 3100
    Surface30 = 4316
    Surface60 = 2072

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 35
    L2 = 37
    Surface45 = 2376
    Surface30 = 3464
    Surface60 = 1512

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 37
    L2 = 37
    Surface45 = 2592
    Surface30 = 3728
    Surface60 = 1664

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 39
    L2 = 37
    Surface45 = 2808
    Surface30 = 3992
    Surface60 = 1816

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 41
    L2 = 37
    Surface45 = 3024
    Surface30 = 4256
    Surface60 = 1968

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 43
    L2 = 37
    Surface45 = 3240
    Surface30 = 4520
    Surface60 = 2120

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 35
    L2 = 39
    Surface45 = 2408
    Surface30 = 3528
    Surface60 = 1524

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 37
    L2 = 39
    Surface45 = 2632
    Surface30 = 3800
    Surface60 = 1684

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 39
    L2 = 39
    Surface45 = 2856
    Surface30 = 4072
    Surface60 = 1844

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 41
    L2 = 39
    Surface45 =3080
    Surface30 = 4344
    Surface60 = 2004

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 43
    L2 = 39
    Surface45 = 3304
    Surface30 = 4616
    Surface60 = 2164

    ajout(Surface45, Surface30, Surface60, L1, L2)

       # Simulation 6 a X19 Y-19
    L1 = 35
    L2 = 41
    Surface45 = 2436
    Surface30 = 3652
    Surface60 = 1528

    ajout(Surface45, Surface30, Surface60, L1, L2)

       # Simulation 6 a X19 Y-19
    L1 = 37
    L2 = 41
    Surface45 = 2668
    Surface30 = 3940
    Surface60 = 1696

    ajout(Surface45, Surface30, Surface60, L1, L2)

       # Simulation 6 a X19 Y-19
    L1 = 39
    L2 = 41
    Surface45 = 2900
    Surface30 = 4228
    Surface60 = 1864

    ajout(Surface45, Surface30, Surface60, L1, L2)

       # Simulation 6 a X19 Y-19
    L1 = 41
    L2 = 41
    Surface45 = 3132
    Surface30 = 4516
    Surface60 = 2032

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 43
    L2 = 41
    Surface45 = 3364
    Surface30 = 4804
    Surface60 = 2200

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 35
    L2 = 43
    Surface45 = 2480
    Surface30 = 3768
    Surface60 = 1528

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 37
    L2 = 43
    Surface45 = 2728
    Surface30 = 4072
    Surface60 = 1700

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 39
    L2 = 43
    Surface45 = 2976
    Surface30 = 4376
    Surface60 = 1876

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 41
    L2 = 43
    Surface45 = 3224
    Surface30 = 4680
    Surface60 = 2052

    ajout(Surface45, Surface30, Surface60, L1, L2)

        # Simulation 6 a X19 Y-19
    L1 = 43
    L2 = 43
    Surface45 = 3472
    Surface30 = 4984
    Surface60 = 2228

    ajout(Surface45, Surface30, Surface60, L1, L2)


    #calcul pente deux directions

    deltaXL1 = ListeL1[-1] - ListeL1[0]
    deltaXL2 = ListeL2[-1] - ListeL2[0]
    deltaY60 = ListeSurface60[-1] - ListeSurface60[0]
    deltaY45 = ListeSurface45[-1]-ListeSurface45[0]
    deltaY30 = ListeSurface30[-1]-ListeSurface30[0]
    penteL130 = deltaY30 / deltaXL1
    penteL230 = deltaY30 / deltaXL2
    penteL145 = deltaY45 / deltaXL1
    penteL245 = deltaY45 / deltaXL2
    penteL160 = deltaY60 / deltaXL1
    penteL260 = deltaY60 / deltaXL2
    print(penteL130)
    print(penteL230)
    print(penteL145)
    print(penteL245)
    print(penteL160)
    print(penteL260)

        # Graphiques
    graph(tools.PORTRAIT)


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