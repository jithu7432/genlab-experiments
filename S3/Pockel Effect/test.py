import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

plt.style.use('bmh')

data = pd.read_excel('data.xlsx', index_col=False)

applied_voltage, intensity = data['Applied Voltage (V)'], data['Intensity (P(V))']

w = 650  # wavelength of the laser in nm
l = 2.5  # Length of the crystal in cms


peaks, _ = find_peaks(intensity.values, height=40)
half_intensity = 48.62
f = plt.figure(1)
# print(*dir(f), sep="\n")
plt.title(r"Applied Voltage // Intensity")
plt.plot(applied_voltage, intensity, "r:")
plt.scatter(applied_voltage, intensity, marker="s", s=12, c='lime')
plt.plot(1530, intensity[peaks], "ro")
plt.axhline(intensity[peaks].values, linestyle="--")
plt.xlabel("Applied Voltage (V)")
plt.ylabel("Intensity [P(V)] " + r"$\mu A$")
plt.annotate('(1550, 48.62)', xy=(250, 32),
             bbox=dict(facecolor='lime', edgecolor='red'))
plt.grid(b=True)
plt.savefig('test_1.png')

d = [(w/(np.pi * l)) * 180/np.pi * np.arcsin(np.sqrt(i/half_intensity))
     for i in intensity]
d = [i.__round__(3) for i in d]

data["birefringence"] = d

g = plt.figure(2)

plt.plot(applied_voltage, d, "r:")
plt.scatter(applied_voltage, d, marker="s", s=12, c='g')
plt.axvline(1550, ymax=0.95, ls='--')
plt.ylabel('Birefringence  ' + r'$D_n$')
plt.xlabel('Voltage ' + r'$(V)$')
plt.title("Birefringence // Voltage")
plt.plot(1550, 7444, 'ro')
plt.annotate('(1550, 7444)', xy=(350, 4500),
             bbox=dict(facecolor='lime', edgecolor='red'))
plt.grid(b=True)
plt.savefig('test_2.png')


print('Return 1')