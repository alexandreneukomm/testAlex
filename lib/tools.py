#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import offsetbox
import os

PORTRAIT = (7, 4)
PAYSAGE = (9.3, 5.9)
FULL15 = (13.9, 8)

GRAPH_LATEX = \
rcParams['font.family'] = 'sans-serif';
rcParams['font.sans-serif'] = ['DejaVu Sans'];
rcParams['font.size'] = 12;
rcParams['axes.titlesize'] = 12;
rcParams['legend.handlelength'] = 1;
rcParams['legend.borderaxespad'] = 0.3;
rcParams['legend.borderpad'] = 0.8;

#constante mécanique

# module de Young divers matériaux en MPa
MATIERE = { "acier": { "E": 210000},
              "md": {"E": 650000},
              "alu": {"E": 70000},
              "laiton": {"E": 110000} }


save_path_pdf = 'C:/Users/alexandr.neukomm/Desktop/TM-A.Neukomm/Documents/Rapport/graph/pdf'
save_path_pgf = 'C:/Users/alexandr.neukomm/Desktop/TM-A.Neukomm/Documents/Rapport/graph'

save_path_tab = 'C:/Users/alexandr.neukomm/Desktop/TM-A.Neukomm/Documents/Rapport/tab'

boite = dict(boxstyle="round", fc="1", pad=0.65)




def save_auto(name_file):
    plt.savefig(os.path.join(save_path_pdf,name_file + '.pdf'), format='pdf')
    plt.savefig(os.path.join(save_path_pgf,name_file + '.pgf'), format='pgf')