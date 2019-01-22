#!/usr/bin/env python3

from matplotlib import rcParams
import csv
import matplotlib.pyplot as plt
import os
import numpy as np
import tools

def read_data_graph(filename, header = True):
    result = {}
    y_label = "Error!"
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for ix, row in enumerate(csvReader):
            if ix > 0 or not header:
                for jx, item in enumerate(result):
                    result[item].append(float(row[jx]))
            else:
                for item in row[:len(row)-1]:
                    result[str(item)] = []
                y_label = row[-1]
    return result, y_label

def zero_time(_data, data_label='Time [ms]'):
    data_res = _data

    offset = min(data_res[data_label])
    for ix, time in enumerate(data_res[data_label]):
        data_res[data_label][ix] = round((data_res[data_label][ix] - offset) * 1000, 0)
    return data_res

def Plot_data(_data, x_label, y_labels, _title,mode=tools.PORTRAIT):
    tools.GRAPH_LATEX
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust(left=0.14,bottom=0.13,right=0.95)
    global x
    plt.title(_title)

    mins_y = []
    maxs_y = []
    color="r"
    x = _data[x_label]
    plt.xlabel(x_label)
    plt.ylabel("Courant (mA)")
    for item in y_labels:
        mins_y.append(min(_data[item]))
        maxs_y.append(max(_data[item]))
        plt.plot(x, _data[item], label=item)
        ######### limiter l'axe X
        plt.gca().set_xlim(10400,11200)
        ######### limiter l'axe Y
        plt.gca().set_ylim(820,1150)
    plt.grid()
    plt.legend(loc='best')

def Plot_2data(_data1,_data2 ,x_label, y_labels, _title,mode=tools.PORTRAIT):
    tools.GRAPH_LATEX
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust(left=0.14,bottom=0.13,right=0.95)
    global x
    plt.title(_title)

    mins_y = []
    maxs_y = []
    x = _data1[x_label]
    plt.xlabel(x_label)
    plt.ylabel("courant (mA)")
    # ax.tick_params(axis="y", labelcolor=color)
    # for item in y_labels:
        # mins_y.append(min(_data[item]))
        # maxs_y.append(max(_data[item]))
    plt.plot(x, _data1,_data2)
        ######### limiter l'axe X
        # plt.gca().set_xlim(730,800)
        ######### limiter l'axe Y
        # plt.gca().set_ylim(-0.004,0.004)
    plt.grid()
    plt.legend(loc='best')

def Plot_data_2_axis(_data, x_label, y_label1, y_label2, _title,mode=tools.PORTRAIT):
    tools.GRAPH_LATEX
    fig = plt.figure(figsize=mode)
    ax = fig.add_subplot(111)
    # fig, ax1 = plt.subplots(figsize=mode)
    # plt.subplots(figsize=mode)
    plt.subplots_adjust()
    global x
    plt.title(_title)

    mins_y = []
    maxs_y = []

    x = _data[x_label]

    lns1=ax.plot(x, _data[y_label1], 'r', label=y_label1)
    #ax1.plot(x, _data[y_label3], 'g', label=y_label3)
    ax.set_xlabel(x_label)
    ax.set_xlim(0, 4000)

    ax.set_ylabel(y_label1, color='r')
    ax.tick_params('y', colors='r')
    ax.set_ylim(0.006, -0.006)

    ax2 = ax.twinx()

    lns2=ax2.plot(x, _data[y_label2],'b', label = y_label2)

    ax2.set_ylabel(y_label2, color='b')
    ax2.tick_params(colors='b')

    fig.tight_layout()

    plt.grid()

    # added these three lines
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    first_legend=plt.legend(lns, labs, loc=0)

    ax2.add_artist(first_legend)

    # first_legend = plt.legend(handles1, labels1, loc='center')
    # ax2.add_artist(first_legend)

    # plt.legend(loc='best')

    #ax1.set_xlim(0, 1000)

    align_yaxis(ax, 0, ax2, 0)

def align_yaxis(ax, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)


if __name__ == "__main__":

    erreur_moteur = "Erreur position moteur (mm)"
    erreur_regle = "Erreur position regle (mm)"
    courant_moteur = "Courant moteur (A)"
    courant_moteurB = "ActualCurrentD"

    file_path14400 = "14400_plotData-2018-12-17T1627.csv"
    data_graph14400, y_label14400 = read_data_graph(file_path14400)

    file_path7200 = "7200_plotData-2018-12-17T1609.csv"
    data_graph7200, y_label7200 = read_data_graph(file_path7200)

    file_path3600 = "3600_plotData-2018-12-17T1624.csv"
    data_graph3600, y_label3600 = read_data_graph(file_path3600)

    file_pathVide = "A_Vide_plotData-2018-12-17T1609.csv"
    data_graphVide, y_label7200 = read_data_graph(file_pathVide)

    file_pathbroche = "broche.csv"
    data_graph_broche, y_labelbroche = read_data_graph(file_pathbroche)


    x = None

    data_graph14400 = zero_time(data_graph14400)
    data_graph7200 = zero_time(data_graph7200)
    data_graph3600 = zero_time(data_graph3600)
    data_graphVide = zero_time(data_graphVide)


    Plot_data(data_graph_broche, "Time [ms]", ["Courant a vide","Courant en usinage"],"Courant broche superposé")

    # Plot_data(data_graph_broche7200, "Time [ms]", ["courant (mA)"],"Erreur de poursuite à vide")
    # Plot_data_2_axis(data_graph3600, "Time [ms]", erreur_regle, courant_moteur, "Mesure à une vitesse de 3600 mm/min", tools.PORTRAIT)
    # Plot_data_2_axis(data_graph7200, "Time [ms]", erreur_regle, courant_moteur, "Mesure à une vitesse de 7200 mm/min", tools.PORTRAIT)
    # Plot_data_2_axis(data_graph14400, "Time [ms]", erreur_regle, courant_moteur, "Mesure à une vitesse de 14400 mm/min", tools.PORTRAIT)
    # Plot_data_2_axis(data_graphVide, "Time [ms]", erreur_regle, courant_moteur, "Mesure à vide à une vitesse de 7200 mm/min", tools.PORTRAIT)
    # Plot_data(data_graph, "Time [ms]", ["ActualCurrentQ"],"Ccoco")

    plt.show()

