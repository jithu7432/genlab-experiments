import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data = pd.read_excel("data.xlsx")

applied_current, theta_minimum = data.keys().to_list()
applied_current, theta_minimum = data[applied_current], data[theta_minimum]

N = 2508  # total number of turns in the coil
l = 15   # length of the coil (cms)
n = N/l  # number of turns per length (cm ^ -1)

"""
B is defined as B = Pi * n * I 
V is definde as V = θ / (l * B)
"""

B = [np.pi * I * n for I in applied_current]
V = [theta_minimum[i] / (l * B[i]) for i in range(len(B))]

data['B'] = B
data['V'] = V
data.index += 1

print(data.to_string())
print(f"\n The mean of Verdet constant = {np.mean(V)}")

f = plt.figure(1)

plt.plot(B, V)
plt.xlabel("Magnetic Field (Osterd)")
plt.ylabel("Verdet constant " + r"$(mins \/\/\/Osterd^{-1} \/ cm^{-1})$")
plt.title("Verdet Constant // Mangnetic Field")
plt.scatter(B, V, color='red')

plt.tight_layout()
plt.grid(True)
plt.savefig('figure_1.png', dpi=100)

g = plt.figure(2)

plt.plot(theta_minimum, V)
plt.xlabel("Angle θ (min)")
plt.ylabel("Verdet constant " + r"$(mins \/\/\/Osterd^{-1} \/ cm^{-1})$")
plt.title("Verdet Constant // Angle θ (min)")
plt.scatter(theta_minimum, V, color='red')

plt.tight_layout()
plt.grid(True)
plt.savefig('figure_2.png', dpi=100)

