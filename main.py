import re
import numpy as np
import pandas
import statsmodels as statM
import pandas as pd
import statsmodels.robust.scale
import matplotlib.pyplot as plt

file = [0,0,0,1,5,7,7,7,10,11,11,11,13,14,15,20,20,21,21,22,23,25,29,]

x2 = [3.5, 4, 5, 5.5, 6, 3, 10, 9.5, 8]
y2 = [50, 39, 80, 74, 60, 66, 89, 77, 100]

aM = sum(file)/len(file)
M = 0

for n in file:
    M += abs(n - aM)

M = M / len(file)
print(f"M: {M}")

std = np.std(file)
v = std*std

mad = statsmodels.robust.scale.mad(file)

print(f"v: {v}, std: {std}, MAD: {mad}")

df = pd.DataFrame(file)

q1 = df.quantile(0.25)
q2 = df.quantile(0.75)

print(f"25% Perzentil: {q1}, 75% Perzentil: {q2}")
# Daten erstellen
data = {'X2': [3.5, 4, 5, 5.5, 6, 3, 10, 9.5, 8],
        'Y2': [50, 39, 80, 74, 60, 66, 89, 77, 100]}

# DataFrame erstellen
df = pd.DataFrame(data)

# Scatter Plot erstellen
plt.scatter(df['X2'], df['Y2'])

# Achsentitel hinzufügen
plt.xlabel('X2')
plt.ylabel('Y2')

# Diagrammtitel hinzufügen
plt.title('Scatter Plot von X2 gegen Y2')


# Plot speichern
plt.savefig('scatter_plot.png')

# Optional: Plot anzeigen (nur wenn eine interaktive Umgebung vorhanden ist)
# plt.show()