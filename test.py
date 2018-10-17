
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.8, 2.5, 2.9, 3.2, 3.7])
y = np.array([1e6, 4.5e6, 8e6, 1.2e7, 2e7])
z = np.polyfit(x, y, 3)

a=z[0]
b=z[1]
c=z[2]
d=z[3]

xfit = np.arange(1.8, 3.7+0.1, 0.01)
fit=(a*xfit**3+b*xfit**2+c*xfit+d)


fig, ax = plt.subplots()
plt.subplots_adjust()

ax.plot(x, y)
ax.plot(xfit, fit)
ax.set(xlabel="Longueur sortie outil (mm)", ylabel='Déflexion (mm)', title='Flexion outil diamètre')
plt.grid()

plt.show()