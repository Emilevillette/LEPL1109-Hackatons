import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from datetime import datetime
from scipy import stats

df = pd.read_csv('Data_energy_load.csv', sep=';', parse_dates=['Date'], skipinitialspace=True)
df['Date'] = [dt['Date'].replace(hour=dt['Hour']) for i, dt in df.iterrows()]

plt.figure(figsize=(11, 3))
plt.xlim(df['Date'].min(), df['Date'].max())
plt.plot(df['Date'], df['Load'], lw=0.1)
plt.title('Time serie of consumption')
plt.xlabel('Date')
plt.ylabel('Power consumption (MW)')

if __name__ == '__main__':
    plt.show()
