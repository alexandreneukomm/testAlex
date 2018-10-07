
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sympy import *


# Variables
x = np.arange(0.0, 15.0, 0.1) #longueur sortie fraise en mm
E=650000 #module de Young carbure de tungstène en MPa
d=3 #diamètre outil en mm
F1=30 #force en N
F2=5 #force en N
expok=7
klimit=1*10**expok

#Equations
I= (np.pi*d**4)/64
y1=(F1*x**3)/(3*E*I)
y2=(F2*x**3)/(3*E*I)
llimite=round(((3*E*10**6*I/10**12)/(klimit))**(1/3)*1000,2)
rapport=round(llimite/d,2)

#Graphique
portrait = (7, 4)
paysage = (9.2, 5.8)
fig, ax = plt.subplots(figsize=portrait)
plt.subplots_adjust()

ax.plot(x, y1,label="Force de {} N" .format(F1))
ax.plot(x, y2,label="Force de {} N" .format(F2))
ax.set(xlabel="Longueur sortie outil (mm)", ylabel='Déflexion (mm)', title='Flexion outil diamètre {} mm' .format(d))
plt.grid()

# Draw a default vline at x=... that spans the yrange
color='tab:red'
plt.axvline(x=llimite, color = color)
ax.annotate('Limite de rigidité de $1 \cdot 10^{} N/m$ \n longueur de sortie de la fraise {} mm'.format(expok,llimite) ,
            (llimite-1.5, max(y1)-max(y1)*0.05), textcoords='data', color = color, rotation=90)
ax.annotate('Rapport longueur / dimaètre: {}'.format(rapport) ,
            (llimite+1, max(y1)-max(y1)*0.05), textcoords='data', color = color,rotation=90)

plt.legend(loc='best')
plt.show()

#Tableau