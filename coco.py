import matplotlib.pyplot as plt
import numpy as np

data1,data2,data3,data4 = (np.random.random(100),
                           np.random.random(100),
                           np.random.random(100),
                           np.random.random(100))

fig,ax = plt.subplots()

ax.plot(data1, label="1", color="k")
ax.plot(data2, label="2", color="r")
ax.plot(data3, label="3", color="g")

ax2 = ax.twinx()
ax2.plot(data4, label="4", color="b")

# First get the handles and labels from the axes
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

# Add the first legend to the second axis so it displaysys 'on top'
first_legend = plt.legend(handles1, labels1, loc='center')
ax2.add_artist(first_legend)

# Add the second legend as usual
ax2.legend(handles2, labels2)

plt.show()