#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:25:23 2021

@author: giuliano
"""

import pandas as pd
from datetime import datetime,timedelta

def CleanDataframe(database_taxi,year,month):
    """
    sottoprogramma che in base all'anno e al mese che vengono inseriti in input
    (quelli del file) elimina eventuali dati che non sono di tale periodo.
    N.B. Tengo conto della data in cui il passeggero è salito nel taxi
    """
    database_taxi['tpep_pickup_datetime'] = pd.to_datetime(database_taxi['tpep_pickup_datetime'])
    database_taxi['year'] = database_taxi['tpep_pickup_datetime'].dt.year  
    database_taxi['month'] = database_taxi['tpep_pickup_datetime'].dt.month                             
    database_taxi = database_taxi[database_taxi['year'] == datetime.strptime(str(year), '%Y').year] 
    database_taxi = database_taxi[database_taxi['month'] == datetime.strptime(str(month), '%m').month]
    del database_taxi['year']
    del database_taxi['month']
                       
    return database_taxi

def zero_passenger(database_taxi):
    """
    sottoprogramma che elimina eventuali dati con 0 passeggeri
    """
    database_taxi = database_taxi[database_taxi['passenger_count'] > 0]
    return database_taxi

   # Utile.writeJsonFile(features_df)
def separateBorough(database_taxi,borough_name):
    """
    Sottoprogramma che, dati in ingresso il dataframe dei taxi, il dataframe dei codici dei 
    borough e il nome del borough,
    restituisce un dataframe che contiene tutti i dati del dataframe dei taxi che
    hanno come 'PULocationID' un codice che appartiene al borough in ingresso
    """
   
    df_zone= pd.read_csv('/Users/giuliano/Desktop/taxi+_zone_lookup.csv')
    # borough : DataFrame vuoto che sarà riempito degli eventuali dati che 
    # hanno come 'PULocationID' un codice che corrisponde al borough richiesto
    borough = pd.DataFrame(columns=(database_taxi.columns))
    
    # loc_borough : Lista vuota che sarà riempita di tutti i codici che 
    # corrispondono al borough considerato
    loc_borough = []
    
    # scorro le righe del dataframe delle zone in modo da riempire la lista 
    # loc_borough definita precedentemente
    for i,zona in df_zone.iterrows():
        if zona[1] == borough_name:  # se il codice corrisponde al borough...
            loc_borough = loc_borough + [zona[0]]  # ..aggiungo il codice alla lista

    borough = database_taxi[database_taxi['PULocationID'].isin (loc_borough)]
    
    return borough  



def timeSlots(database_taxi):
    #modifico il tipo della colonna tpep da stringa a datetime
    # database_taxi['tpep_pickup_datetime']=pd.to_datetime(database_taxi['tpep_pickup_datetime'])
    #creo un'altra colonna hour che estrae l'ora dal dato datetime presente in tpep
    database_taxi['hour']=database_taxi['tpep_pickup_datetime'].dt.hour
    #elimino le colonne che non servono più (voglio una tabella con solo time slots e somma passeggeri)
    del database_taxi['PULocationID']
    #suddivido in base al valore presente nella colonna hour e per ciascuna sommo il numero di passeggeri
    time_slots = database_taxi.groupby(by=['hour']).sum().groupby(level=0).cumsum()
    
    return time_slots

           

 
  
  
