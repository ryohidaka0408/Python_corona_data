import numpy as np
from matplotlib import pyplot as plt

def MakeGraph():
    xmax = 1000
    xmin = 0
    x = np.arange(xmin, xmax)

    ymax = 3000
    ymin = 0
    y = np.arange(ymin,ymax) 

    plt.plot(x,y)

    plt.axhline(y = 0, color = "gray")
    plt.axvline(x = 0, color = "gray")

    plt.show()