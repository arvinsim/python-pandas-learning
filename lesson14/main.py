import Quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt', 'r').read()


def mortgage_30y():
    df = Quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df.columns = ['M30']
    df = df.resample('D').mean()
    df = df.resample('M').mean()
    return df


def HPI_Benchmark():
    df = Quandl.get('FMAC/HPI_USA', authtoken=api_key)
    # df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    return df


m30 = mortgage_30y()
HPI_data = pd.read_pickle('fiddy_states3.pickle')
HPI_bench = HPI_Benchmark()

state_HPI_M30 = HPI_data.join(m30)

# print(state_HPI_M30.corr())
print(state_HPI_M30.corr()['M30'].describe())
