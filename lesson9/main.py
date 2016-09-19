import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

TXT1yr = HPI_data['TX'].resample('A', how='ohlc')
print(TXT1yr.head())

HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI')
TXT1yr.plot(ax=ax1, label='Yearly TX HPI')

# plt.legend().remove()
plt.legend(loc=4)
plt.show()
