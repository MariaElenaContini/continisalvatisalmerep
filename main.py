#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:20:53 2021

@author: giuliano
"""
import Utils
from df_function import CleanDataframe,timeSlots,separateBorough
from time import perf_counter

"""
Quali sono le fasce orarie con più passeggeri? E quella con meno? 
Impostate le vostre fasce orarie (per esempio ogni ora) e scoprite quali sono quelle in cui i taxi 
guidano il maggior numero di passeggeri e ripetete l'analisi per ogni borough. 
Fornite i risultati attraverso un file e un plot. 
Input: anno, mese*, borough*
Output: file, grafico
"""

if __name__ == '__main__':
    
    args = Utils.initializeParser()
    year = Utils.getYearFromParser(args.year)
    month = Utils.getMonthFromParser(args.month)
    fileName = Utils.generateFileName(year, month)
    
    t_start = perf_counter() # tempo di inizio
    
    data_taxi = Utils.readCsv(fileName)
    
    data_taxi= CleanDataframe(data_taxi, year,month)
    data_taxi = zero_passenger(data_taxi)
    
    borough_Manhattan = separateBorough(data_taxi,'Manhattan')
    borough_Queens = separateBorough(data_taxi,'Queens')
    borough_Bronx = separateBorough(data_taxi,'Bronx')
    borough_Staten_Island = separateBorough(data_taxi,'Staten Island')
    borough_Brooklyn = separateBorough(data_taxi,'Brooklyn')
        
    general_study= timeSlots(data_taxi)


    dt = perf_counter() - t_start # tempo di esecuzione
    
    print('Tempo di esecuzione: ' + str(dt) + ' s')
    print('Fine')
