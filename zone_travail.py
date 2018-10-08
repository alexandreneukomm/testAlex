#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sympy import *
from random import*

# Fonctions

def Numero2(n):
    L = [[None] * 2] * n
    for k in range(n):
        x, y = randint(50, 650), randint(50, 650)
        L[k] = [x, y]
    print(L)

def constant (n, d, a):
    I = [None] * n
    for k in range(n):
        I[k] = d
        a.append(d)

def croissante (a):
    for n_i in deplacement_positif:
        a.append(n_i)

# def décroissante (a):
#     for n_i in deplacement_positif:



if __name__== '__main__':
    a = 45
    a= math.radians(a)

    Y1min = 0
    Y1max = 76
    Y1min = Y1min
    Y2max = Y1max
    pas = 1
    deplacement_positif = np.arange(0, Y1max + 0.1, pas)
    deplacement_negatif = np.arange(Y1max, 0 + 0.1, pas)

    n = len(deplacement_positif)

    print(n)


    cine_inverse = np.array([[tan(a), 1], [-tan(a), 1]])

    Y1 = []
    Y2 = []

    #constant(pas, 5, Y1)
    #constant(pas, 0, Y1)
    croissante(Y1)
    print(Y1)
    # Y1.reverse()
    # print(Y1)

    pos_mot = np.array([Y1, [Y2]])

    plaqueXY = np.array([[],[]])
    #
    # plaqueXY = cine_inverse.dot(pos_mot)
    #print(pos_mot)
