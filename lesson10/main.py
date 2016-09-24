import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean')
print(HPI_data[['TX', 'TX1yr']].head())
# HPI_data.dropna(how='all', inplace=True)
HPI_data.fillna(value=-99999, limit=10, inplace=True)
print(HPI_data[['TX', 'TX1yr']].head())

HPI_data[['TX', 'TX1yr']].plot(ax=ax1)

plt.legend(loc=4)
plt.show()
