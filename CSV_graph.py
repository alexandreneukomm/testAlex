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
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax = plt.subplots(figsize=mode)
    plt.subplots_adjust()
    global x
    plt.title(_title)

    mins_y = []
    maxs_y = []

    x = _data[x_label]
    plt.xlabel(x_label)

    plt.ylabel(y_label7200)
    for item in y_labels:
        mins_y.append(min(_data[item]))
        maxs_y.append(max(_data[item]))
        plt.plot(x, _data[item], label=item)
        ######### limiter l'axe X
        # plt.gca().set_xlim([min(data_graph[item]), 0.2])
        ######### limiter l'axe Y
        # plt.gca().set_ylim([min(mins_y), 1.05*max(maxs_y)])
    plt.grid()
    plt.legend(loc='best')

def Plot_data_2_axis(_data, x_label, y_label1, y_label2, _title,mode=tools.PORTRAIT):
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['DejaVu Sans']
    fig, ax1 = plt.subplots(figsize=mode)
    plt.subplots_adjust()
    global x
    plt.title(_title)

    mins_y = []
    maxs_y = []

    x = _data[x_label]

    ax1.plot(x, _data[y_label1], 'r', label=y_label1)
    #ax1.plot(x, _data[y_label3], 'g', label=y_label3)
    ax1.set_xlabel(x_label)

    ax1.set_ylabel(y_label1, color='r')
    ax1.tick_params('y', colors='r')
    ax1.set_ylim(0.006, -0.006)
    ax1.legend(loc=1)

    ax2 = ax1.twinx()

    ax2.plot(x, _data[y_label2],'b', label = y_label2)

    ax2.set_ylabel(y_label2, color='b')
    ax2.tick_params(colors='b')
    ax2.legend(loc=2)

    fig.tight_layout()

    plt.grid()
    plt.legend(loc='best')

    #ax1.set_xlim(0, 1000)

    align_yaxis(ax1, 0, ax2, 0)

def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
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

    file_path7200 = "7200_plotData-2018-12-17T1609.csv"
    data_graph7200, y_label7200 = read_data_graph(file_path7200)

    file_path3600 = "3600_plotData-2018-12-17T1624.csv"
    data_graph3600, y_label3600 = read_data_graph(file_path3600)

    file_pathVide = "A_Vide_plotData-2018-12-17T1609.csv"
    data_graphVide, y_label3600 = read_data_graph(file_pathVide)

    x = None

    data_graph7200 = zero_time(data_graph7200)
    data_graph3600 = zero_time(data_graph3600)
    data_graphVide = zero_time(data_graphVide)


    #Plot_data(data_graph, "Time [ms]", [courant_moteur, courant_moteurB],"Erreur de poursuite")
    Plot_data_2_axis(data_graph3600, "Time [ms]", erreur_regle, courant_moteur, "Mon titre", tools.PAYSAGE)
    Plot_data_2_axis(data_graph7200, "Time [ms]", erreur_regle, courant_moteur, "7200", tools.PAYSAGE)
    Plot_data_2_axis(data_graphVide, "Time [ms]", erreur_regle, courant_moteur, "Vide", tools.PAYSAGE)
    #Plot_data(data_graph, "Time [ms]", ["ActualCurrentQ"],"Ccoco")
    #Plot_data(data_graph, "Time [ms]", ["ActualCurrentD","ActualCurrentQ"])

    plt.show()

