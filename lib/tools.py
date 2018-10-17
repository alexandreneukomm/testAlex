#!/usr/bin/env python3

import matplotlib.pyplot as plt
import os

PORTRAIT = (7, 4)
PAYSAGE = (9.3, 5.9)

#constante mécanique

# module de Young divers matériaux en MPa
Emd = 650000
Elaiton = 110000
Eacier = 210000
Ealu = 70000

save_path_pdf = 'C:/Users/alexandr.neukomm/Desktop/TM-A.Neukomm/Documents/Rapport/graph/pdf'
save_path_pgf = 'C:/Users/alexandr.neukomm/Desktop/TM-A.Neukomm/Documents/Rapport/graph'

save_path_tab = 'C:/Users/alexandr.neukomm/Desktop/TM-A.Neukomm/Documents/Rapport/tab'

def save_auto(name_file):
    plt.savefig(os.path.join(save_path_pdf,name_file + '.pdf'), format='pdf')
    plt.savefig(os.path.join(save_path_pgf,name_file + '.pgf'), format='pgf')