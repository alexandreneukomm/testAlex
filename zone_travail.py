#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sympy import *
from random import*

# Fonctions

def constant (d, a): #d = numéro constant a = choix de la liste
    I = [None] * n
    for k in range(n):
        I[k] = d
        a.append(d)

def croissante (a): # a = choix de la liste
    for n_i in deplacement_positif:
        a.append(n_i)

def decroissante (a): # a = choix de la liste
    b=[]
    for n_i in deplacement_positif:
        b.append(n_i)
    b.reverse()
    a.extend(b)

if __name__== '__main__':
    Y1 = []
    Y2 = []
    X = []
    Y = []
    a = 60
    a_rad= math.radians(a)

    Y1min = 0
    Y1max = 38
    Y2min = Y1min
    Y2max = Y1max
    pas = 0.1
    deplacement_positif = np.arange(0, Y1max + 0.1, pas)

    n = len(deplacement_positif)

    coco = np.array([[1, 2], [3, 4]])
    gaga = np.array([5,6])

    test=coco.dot(gaga)

    print(test)
    cine_direct = np.array([[1/(2*tan(a_rad)), -1/(2*tan(a_rad))], [0.5, 0.5]])
    print(cine_direct)

    plaqueXY = np.array([[],[]])

    # #Y1
    croissante(Y1)
    constant(Y1max,Y1)
    decroissante(Y1)
    constant(Y2min, Y1)

    # #Y2
    constant(Y2min, Y2)
    croissante(Y2)
    constant(Y1max, Y2)
    decroissante(Y2)

    pos_mot = np.array([Y1, Y2])

    print(pos_mot)


    plaqueXY = cine_direct.dot(pos_mot)

    X = plaqueXY[0]
    Y = plaqueXY[1]



    fig, ax = plt.subplots()
    plt.subplots_adjust()
    plt.plot(X, Y)
    ax.set(title='Angle des rails de {}°'.format(a))
    plt.axis('equal')
    plt.show()
