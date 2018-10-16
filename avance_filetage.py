#!/usr/bin/env python3
# AGA: Bonne pratique pour forcer l'utilisation de python 3 (je crois... en tout cas je le vois tjrs en début des codes)

import matplotlib.pyplot as plt
import numpy as np
import tools

# Fonctions
# AGC: Essaie d'avoir des noms les plus précis possible.
# En effet ce n'est pas juste une fonction de graph générique, mais une fonction qui est déjà spécialisée
def graph_avance_filetage(FZ, N, F, fzlimit, mode ="PORTRAIT"):

    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust()

    for ix, n_ix in enumerate(N):
        ax.plot(FZ, F[ix], label="Vitesse de rotation de {} tr/min".format(n_ix))

    ax.set(xlabel="Pas de filetage (mm)", ylabel='Avance de l\'axe Z (mm/min)',
        title='Vitesse d\'avance de l\'axe Z fonction du pas de filetage')
    plt.xticks(np.arange(0, max(FZ)+0.1, 0.1))
    plt.gca().set_ylim(0, fzlimit+5000)
    plt.grid()

    # Draw a default vline at x=... that spans the yrange
    color = 'tab:brown'
    plt.axhline(y=fzlimit, color=color)
    ax.annotate('Limite d\'avance de l\'axe Z {} (mm/min)'.format(fzlimit), (0, fzlimit + 2500), textcoords='data', color=color, bbox=dict(boxstyle="round", fc="w"))

    plt.legend(loc='best')

    if SAVE==True:
        tools.save_auto(name_file)

    plt.show()

# AGC: Bonne pratique en python: limiter pour avoir une seule entrée possible du programme (donc le main).
# Dans ton cas précis ne pose pas de problème car tu run sur le fichier que tu utilise mais si tu veux par exemple
# réutiliser une fonction définie ici dans un autre pogramme, tu vas inclure ce fichier.
# Et là ça va ètre le bordel même en runnant le programme depuis un autre fichier.
if __name__== '__main__':

    # Variables
    SAVE = False
    name_file = 'avance_filetage'
    FZ = np.arange(0.0, 1.5 + 0.1, 0.1) # Pas du filet [mm]
    N = np.arange(10000, 40000 + 1, 10000) # Avance [mm/min]
    #  AGC: 40000+1 car la fonction np.arange à la borne limite max "exclusive" (pas sur du terme "exclusive" :-))
    fzlimit = 18000 # Limite d'avance de l'axe Z [mm/min]
    # AGC: J'ai tendance à mettre des majuscule pour indiquer un vecteur,
    # d'ailleur je crois que c'est normalisé en math non?

    # Equations
    F = []
    for n_i in N:
        F.append(FZ * n_i)
    # AGC: ici on peut discuter du fait de mettre les équations dans la fonction de graph ou non.
    # En effet on a déjà une fonction spécifique pour l'affichage des avance filetage.
    # Donc à prioris les calculs, qui sont également spécifiques pourrait être fait dans la fonction de graph.
    # Ca supprime une boucle, cependant moi je préfère structurer en 1° Définition ou récupération des données,
    # 2° Calculs 3° Affichage
    # Du coup j'ai laissé les calculs la, quite à faire deux fois la boucle.

    # Graphique
    graph_avance_filetage(FZ, N, F, fzlimit, tools.PORTRAIT)