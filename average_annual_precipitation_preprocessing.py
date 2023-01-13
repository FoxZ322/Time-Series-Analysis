# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 22:48:15 2023

@author: Hlib
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv('Canadian_climate_history.csv', sep = ',', decimal = '.').fillna(0)

precipitation_GALGARY = list(data.TOTAL_PRECIPITATION_CALGARY)
precipitation_EDMONTON = list(data.TOTAL_PRECIPITATION_EDMONTON)
precipitation_MONCTON = list(data.TOTAL_PRECIPITATION_MONCTON)
precipitation_MONTREAL = list(data.TOTAL_PRECIPITATION_MONTREAL)
precipitation_OTTAWA = list(data.TOTAL_PRECIPITATION_OTTAWA)
precipitation_QUEBEC = list(data.TOTAL_PRECIPITATION_QUEBEC)
precipitation_SASKATOON = list(data.TOTAL_PRECIPITATION_SASKATOON)
precipitation_STJOHNS = list(data.TOTAL_PRECIPITATION_STJOHNS)
precipitation_TORONTO = list(data.TOTAL_PRECIPITATION_TORONTO)
precipitation_VANCOUVER= list(data.TOTAL_PRECIPITATION_VANCOUVER)
precipitation_WHITEHORSE = list(data.TOTAL_PRECIPITATION_WHITEHORSE)
precipitation_WINNIPEG = list(data.TOTAL_PRECIPITATION_WINNIPEG)


precipitations = [precipitation_GALGARY, precipitation_EDMONTON, precipitation_MONCTON,
                precipitation_MONTREAL, precipitation_OTTAWA, precipitation_QUEBEC,
                precipitation_SASKATOON, precipitation_STJOHNS, precipitation_TORONTO,
                precipitation_VANCOUVER, precipitation_WHITEHORSE, precipitation_WINNIPEG]


def to_annual_precipitation(series):
    res = [] 
    current = list(series)
    for i in range(80):
        if not(i % 4):
            res += [sum(current[:366])]
            current = current[366:]
        else:
            res += [sum(current[:365])]
            current = current[365:]
        
    return res
            
            
annual_precipitations = list(map(to_annual_precipitation, precipitations))


def average_sum(series):
    return sum(series) / sum(elem != 0 for elem in series)


average_annual_precipitations = list(map(average_sum, zip(*annual_precipitations)))


df_average_annual_precipitations = pd.DataFrame(average_annual_precipitations, columns = ['Average Parcipations'])


df_average_annual_precipitations.to_csv('average_annual_precipitations.csv')

###############################################################################

annual_precipitations_discrete = []

for i, series in enumerate(annual_precipitations):
    current = []
    for value in series:
        if value:
            current += [i+1]
        else:
            current += [0]
    annual_precipitations_discrete += [current]
    
t = np.linspace(1940, 2019, 80)

colors = ['maroon', 'red', 'orangered',
          'gold', 'yellow', 'greenyellow',
          'lime', 'springgreen', 'aquamarine',
          'cyan', 'dodgerblue', 'mediumblue']

for i in range(12):
    t_copy = np.copy(t)  
    ommit = np.abs(annual_precipitations_discrete[i]) == 0
    t_copy[ommit] = np.nan
    plt.plot(t_copy, annual_precipitations_discrete[i], linewidth=12, color = colors[i])
    
axes = plt.gca()

axes.get_yaxis().set_visible(False)
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)
axes.spines['bottom'].set_visible(False)
axes.spines['left'].set_visible(False)

plt.show()
