# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:32:09 2020

@author: StoyanBoyukliyski
"""

import ChiouandYoung2014 as CY
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import lognorm
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from itertools import combinations
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

import matplotlib.animation as animation


data = pd.read_csv("C:\\Users\\StoyanBoyukliyski\\OneDrive\\Desktop\\MScDissertation\PythonFiles\\RegressionCoefficients.csv")
data.head()
data = data.set_index("Period(s)")
        
Intensity = []
usablespec = data.index[2:]
for j in usablespec:
    slc = data.loc[j]
    Intensity.append(float(CY.LognormalFunct(slc, 0,0)[0]))


figure = plt.figure()
ax2 = figure.add_subplot(111)
ax2.plot([float(u) for u in usablespec], Intensity, "k-")
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_title("Response Spectrum using C&Y(2014)")
ax2.set_xlabel("Period T (sec)")
ax2.set_ylabel("Acceleration (g)")
ax2.grid(True, which = "both", axis = "both", linestyle = "--")
plt.show()

IntensityDict = pd.DataFrame(usablespec, Intensity)
ax2.text(1, max(Intensity)-0.5, "Max Intenisty = " + str("{:.2f}".format(max(Intensity))) + "g" + "\n" + "at T =" + IntensityDict.loc[max(Intensity)][0] + " sec")