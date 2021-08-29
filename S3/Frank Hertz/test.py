from matplotlib.style import available
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.ticker import AutoLocator

plt.style.use("classic")

df = pd.read_excel('data.xlsx')
accelerating_voltage = df["Accelerating voltage (V)"]
output_current = df["Output Current (nA)"]
peaky = find_peaks(output_current)[0]

fig, ax = plt.subplots()
plt.grid()

ax.plot(accelerating_voltage,output_current,":g", alpha=0.7)
ax.scatter(accelerating_voltage,output_current,marker="X", color="blue",alpha=0.5)

ax.set_xlabel("Accelerating Voltage (V)")  
ax.set_ylabel("Output Current (nA)")

ax.set_xticks(peaky)
ax.xaxis.set_major_locator(AutoLocator())
for x in peaky:

    plt.text(x,1, f"{x}", color="black")

plt.title("Accelerating Voltage // Output Current")#%%
plt.savefig('test.png', dpi=100)


