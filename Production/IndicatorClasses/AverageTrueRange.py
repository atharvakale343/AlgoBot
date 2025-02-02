'''
Name: AVERAGE TRUE RANGE

Naming Convention of DataFrame Columns: 
    Indicator Generated DataFrame head: ATR + lookback_period 
    Signal Generated DataFrame head: ATR SIGNAL + lookback_period 

Function List:
    indicator_generator
    signal_generation
    train_test
    live_signal
    run

Type of Indicator: Volatility

Usage Notes: 
    * Average true range (ATR) is a technical indicator measuring market volatility.
    * A sudden increase in the ATR following a large move counter to the prevailing trend may lead some 
    traders think the ATR is confirming the old trend; however, this may not actually be the case.
    * Simply put, a stock experiencing a high level of volatility has a higher ATR, and a low volatility 
    stock has a lower ATR.
    
'''
'''
Function Checklist
- a function to take the dataframe input and clean it, in order to keep just the HIGH, LOW, CLOSE and VOLUME
- indicator generation function
- signal generation function
- train test function, that returns the efficacy
- current long/short strength 
'''
'''
Inputs: dataframe_input, lookback_period
Outputs: live_signal (scaled)
'''

import math
import pandas as pd
import json 
import numpy as np
import sys
import oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.text

class AverageTrueRange:

    def __init__(self, dataframe_input, lookback_period):
        df_generatedIndicators = pd.DataFrame() #Generated from indicator_generator

        df_generatedSignal = pd.DataFrame() #Generated from signal_generation

        self.dataframe_input = dataframe_input
        self.lookback_period = lookback_period

#######################
#Indicator Generator Function
#######################

    def indicator_generator(self):
        df = self.dataframe_input
        n = self.lookback_period
        
        df_indicators = pd.DataFrame()
                
        temp_list = [None for i in range(len(df))]
        indic_columnhead = 'ATR ' + str(n)
        df_indicators[indic_columnhead] = temp_list
        
        initial_gap = len(df) - int(len(df)/n)*n
        
        low_list = [None for i in range(n)]
        high_list = [None for i in range(n)]
        close_list = [None for i in range(n)]
        atr = [None for i in range(n)]
        
        initial_start_ctr = 0
        initial_end_ctr = n
        
        for i in range(len(df) - n):
            
            low_price = min(list(df['LOW'].iloc[initial_start_ctr : initial_end_ctr]))
            low_list.append(low_price)
            
            high_price = max(list(df['HIGH'].iloc[initial_start_ctr : initial_end_ctr]))
            high_list.append(high_price)
            
            close_price = df['CLOSE'].iloc[initial_end_ctr]
            close_list.append(close_price)
                
            atr_val = max([abs(high_price - low_price), abs(high_price - close_price), abs(low_price - close_price)])
            
            atr_val = atr_val/n
            
            atr.append(atr_val)
            
            initial_start_ctr += 1
            initial_end_ctr += 1

        df_indicators[indic_columnhead] = atr
        
        self.df_generatedIndicators = df_indicators
    
#######################
#Signal Generation Dividers
#######################

    def signal_generation(self, indic_name = 'ATR'):
        n = self.lookback_period
        indic_df = self.df_generatedIndicators
    
        df_internal = pd.DataFrame()
        
        indic_list = list(indic_df[indic_name + ' ' + str(n)])
        indic_list = indic_list[n:]
        
        a = min(indic_list)
        b = max(indic_list)
        b_dash = 100
        a_dash = 0
        scaled_signal_list = [None for i in range(n)]
        for i in indic_list:
            try:
                frac = (i - a)/(b - a)
                val1 = frac*(b_dash - a_dash)
                scaled_val = val1 + a_dash
                scaled_signal_list.append(scaled_val)
            except:
                scaled_signal_list.append(0)
        
        df_internal[indic_name + ' SIGNAL ' + str(n)] = scaled_signal_list
        
        self.df_generatedSignal = df_internal
#######################
#Train Test Function
#######################

    def live_signal(self, live_lookback = 1):
        indic_name = 'ATR'
        mid_string = 'SIGNAL'
        n = self.lookback_period
        col_head = indic_name + ' ' + mid_string + ' ' + str(n)
        out_list = []
        for i in range(-live_lookback, 0):
            out_list.append(self.df_generatedSignal[col_head].iloc[i])
        return out_list

#######################
#Run Function
#######################

    def run(self, live_lookback = 1):
        self.indicator_generator()
        self.signal_generation()
        live_signal = self.live_signal(live_lookback)

        return live_signal
