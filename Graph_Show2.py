"""
Show graph with csv file
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Timelag.csv', index_col = 'Index')

fig = plt.figure(figsize=(15,15))

plt.subplot(1,2,1)
plt.plot(df['Korea'])
plt.xlabel("time")
plt.ylabel("distance")
plt.legend('Country1')

plt.subplot(1,2,2)
plt.plot(df['England'])
plt.xlabel("time")
plt.ylabel("distance")
plt.legend('Country2')

plt.show()