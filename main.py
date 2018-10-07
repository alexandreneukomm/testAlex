import csv
import matplotlib.pyplot as plt
import os
import numpy as np

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

#def der(signal):
#    derive =[]
#    derive=np.gradient(f,signal)
#    return derive

if __name__ == "__main__":

    file_path = "graph_xy.csv"
    data_graph, y_label = read_data_graph(file_path)
    plt.figure()
    plt.title(os.path.splitext(os.path.basename(file_path))[0])
    x = None
    #derive_data = []
    mins_y = []
    maxs_y = []
    for ix, item in enumerate(data_graph):
        if ix == 0:
            x = data_graph[item]
            plt.xlabel(item)
            plt.ylabel(y_label)
        else:
            mins_y.append(min(data_graph[item]))
            maxs_y.append(max(data_graph[item]))
            plt.plot(x, data_graph[item], label=item)
            ######### limiter l'axe X
            plt.gca().set_xlim([min(data_graph[item]), 0.2])
            ######### limiter l'axe Y
            plt.gca().set_ylim([min(mins_y), 1.05*max(maxs_y)])

    plt.grid(True,linestyle='-.')
    plt.legend(loc='right')
    plt.show()

