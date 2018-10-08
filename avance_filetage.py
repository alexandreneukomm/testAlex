import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import *

# Fonctions

def graph(a):
    fig, ax = plt.subplots(figsize=a)
    plt.subplots_adjust()

    ax.plot(fz, f1, label="Vitesse de rotation de {} tr/min".format(n1))
    ax.plot(fz, f2, label="Vitesse de rotation de {} tr/min".format(n2))
    ax.plot(fz, f3, label="Vitesse de rotation de {} tr/min".format(n3))
    ax.plot(fz, f4, label="Vitesse de rotation de {} tr/min".format(n4))
    ax.set(xlabel="Pas de filetage (mm)", ylabel='Avance (mm/min)',
           title='Vitesse avance de l\'axe Z fonction du pas de filetage')
    plt.grid()

    # Draw a default vline at x=... that spans the yrange
    color = 'tab:brown'
    plt.axhline(y=fzlimit, color=color)
    ax.annotate('Limite d\'avance de l\'axe Z', (0.01, fzlimit + 1000), textcoords='data', color=color)
    # ax.annotate('Rapport longueur / dimaètre: {}'.format(rapport) , (llimite+1, max(y1)-max(y1)*0.05), textcoords='data', color = color,rotation=90)

    plt.legend(loc='best')


# Variables
portrait = (7, 4)
paysage = (9.2, 5.8)
fz = np.arange(0.0, 1.7, 0.1) #longueur sortie fraise en mm
n1 = 10000 # vitesse broche
n2 = 20000 # vitesse broche
n3 = 30000 # vitesse broche
n4 = 40000 # vitesse broche
fzlimit=16000

#Equations
f1=fz*n1
f2=fz*n2
f3=fz*n3
f4=fz*n4

#Graphique
graph(portrait)

plt.show()