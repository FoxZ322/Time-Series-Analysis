# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 22:48:15 2023

@author: Hlib
"""

import pandas as pd

data = pd.read_csv('Canadian_climate_history.csv', sep = ',', decimal = '.').fillna(0)

percipation_GALGARY = list(data.TOTAL_PRECIPITATION_CALGARY)
percipation_EDMONTON = list(data.TOTAL_PRECIPITATION_EDMONTON)
percipation_MONCTON = list(data.TOTAL_PRECIPITATION_MONCTON)
percipation_MONTREAL = list(data.TOTAL_PRECIPITATION_MONTREAL)
percipation_OTTAWA = list(data.TOTAL_PRECIPITATION_OTTAWA)
percipation_QUEBEC = list(data.TOTAL_PRECIPITATION_QUEBEC)
percipation_SASKATOON = list(data.TOTAL_PRECIPITATION_SASKATOON)
percipation_STJOHNS = list(data.TOTAL_PRECIPITATION_STJOHNS)
percipation_TORONTO = list(data.TOTAL_PRECIPITATION_TORONTO)
percipation_VANCOUVER= list(data.TOTAL_PRECIPITATION_VANCOUVER)
percipation_WHITEHORSE = list(data.TOTAL_PRECIPITATION_WHITEHORSE)
percipation_WINNIPEG = list(data.TOTAL_PRECIPITATION_WINNIPEG)


percipations = [percipation_GALGARY, percipation_EDMONTON, percipation_MONCTON,
                percipation_MONTREAL, percipation_OTTAWA, percipation_QUEBEC,
                percipation_SASKATOON, percipation_STJOHNS, percipation_TORONTO,
                percipation_VANCOUVER, percipation_WHITEHORSE, percipation_WINNIPEG]


def to_annual_percipation(series):
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
            
            
annual_percipations = list(map(to_annual_percipation, percipations))


def average_sum(series):
    return sum(series) / sum(elem != 0 for elem in series)


average_annual_percipations = list(map(average_sum, zip(*annual_percipations)))


df_average_annual_percipations = pd.DataFrame(average_annual_percipations, columns = ['Average Parcipations'])


df_average_annual_percipations.to_csv('average_annual_percipations.csv')