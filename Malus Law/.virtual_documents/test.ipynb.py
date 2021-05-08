import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks

pd.plotting.register_matplotlib_converters()
get_ipython().run_line_magic("matplotlib", " inline")

plt.rcParams['figure.dpi'] = 100
plt.rcParams['axes.grid'] = True
plt.style.use('seaborn')


data = pd.read_csv('dataset.csv')
imax = data.Imax.values
imin = data.Imin.values


P = [(imax[i] - imin[i]) / (imax[i] + imin[i]) for i in range(len(imax))]
P = [x.__round__(4) for x in P]
data["Polarisation"] = P


#Plotting
plt.plot(data.Angle[0:7],imax[0:7],'rX--')
plt.plot(data.Angle[0:7],imin[0:7],'gX--')
plt.legend(['I max','I min'])
plt.xlabel('Angle of Incidence')
plt.ylabel('Current in Micro-Amperes')
plt.savefig("Figure_1",dpi = 300)


data


plt.plot(data.Angle, data.Polarisation,'rX--');
plt.xlabel('Angle')
plt.ylabel('Degree of Polarisation');
x,y = data.Angle[list(data.Polarisation).index(max(data.Polarisation.values))], max(data.Polarisation)
plt.annotate("  MAX = 56 degrees",(x,y))
plt.savefig('Figure_2',dpi = 300)


data2 = pd.read_csv('dataset_2.csv')
data2["P"] = [(i / max(data2.Current)).__round__(4) for i in data2.Current]


data2["cos^2 θ"] = [((np.cos(x * np.pi/180))**2).__round__(3) for x in data2.RelativeAngle]
m, c = np.polyfit(data2.RelativeAngle,data2.P,1)
data2.index += 1


plt.plot(data2.RelativeAngle,data2.P,'gX');
plt.plot(data2.RelativeAngle,m * data2.RelativeAngle + c, 'r--');
plt.xticks(list(range(0,101,10)))
plt.xlabel("Angle between the Polaroid θ");
plt.ylabel("Relative Intensity");
plt.savefig('Figure_3',dpi = 300)


data2


data3 = pd.read_csv('dataset_3.csv')
data3["P"] = [(i / max(data3.Current)).__round__(4) for i in data3.Current]
data3["cos^2 θ"] = [((np.cos(x * np.pi/180))**2).__round__(3) for x in data3.Angle]
m, c = np.polyfit(data3.Angle, data3.P, 1)


data3


plt.plot(data3.Angle,data3.P,'gX');
plt.plot(data3.Angle,m * data3.Angle + c, 'r--');
plt.xticks(list(range(0,101,10)))
plt.xlabel("Angle between the Polaroid θ");
plt.ylabel("Relative Intensity");
plt.savefig('Figure_4',dpi = 300)
