#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:00:32 2021

@author: giuliano
"""

import argparse
import pandas as pd
import json
from datetime import datetime

def initializeParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("year",
                        help="The year of which you wants to obtain the analysis",
                        type=str)
    parser.add_argument("-m", "--month",
                        help="The year of which you wants to obtain the analysis. Month must be expressed as number "
                             "or in english.",
                        type=str,
                        default='02'
                        )
    parser.add_argument("-b", "--borough",
                        help="The zone of which you wants to obtain the analysis",
                        type=str,
                        default='.json')
    return parser.parse_args()


def saveJsonFile(filePath, dumpData, indent=3):
    try:
        file = open(filePath, 'w')
        json.dump(dumpData, file, indent=indent)
        file.close()
    except OSError as e:
        print(e)
        exit()


def getYearFromParser(year):
    try:
        return datetime.strptime(year, '%Y').year
    except:
        print('Error! Bad format for \'year\' parameter.')
        exit()


def generateFileName(year, month):
    return 'yellow_tripdata_' + str(year).zfill(4) + '-' + str(month).zfill(2) + '.csv'


def getMonthFromParser(month):
    if month != None:
        try:
            stringSize = len(month)
            if stringSize < 3:
                month = datetime.strptime(month, '%m').month
            elif stringSize == 3:
                month = datetime.strptime(month, '%b').month
            else:
                month = datetime.strptime(month, '%B').month
            return month
        except:
            print('Error! Month format not recognized.')
            exit()
    return month


def readCsv(fileName):
    try:
        df_in = pd.read_csv('taxi_file/'+fileName, usecols=['tpep_pickup_datetime','passenger_count','PULocationID']).head(10000).sort_values(by=['tpep_pickup_datetime'])
        return df_in
    except Exception as execption:
        # print('Data-source not found for given dates.')
        print(execption)
