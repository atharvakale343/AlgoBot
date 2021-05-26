from Engines.FilteredTrend import Engine2
import numpy as np
import pandas as pd

"""
Data Format for Positions
[(TICKER, LONG/SHORT, Number_Of_Shares_Traded, Entry_Price, Exit_Price, Days_Since_Entry)]


"""
class SwingBacktest:
    initial_capital = 100000
    cash = 0
    position_list = []
    transaction_cost_per_trade = 20
    after_trade_profits = 0
    number_of_live_positions = 0
    base_lookback = 7
    number_of_readings = 5
    def __init__(self, input_dict, training_period, test_period, position_expiry, max_positions = 10, stop_loss_percent = 0.03):
        self.input_dict = input_dict
        self.training_period = training_period
        self.test_period = test_period
        self.position_expiry = position_expiry
        self.max_positions = max_positions
        self.stop_loss_percent = stop_loss_percent

    def clean_dictionary(self):
        input_dict = self.input_dict
        list_tickers = list(input_dict.keys)

        requirement_length = self.training_period + self.test_period
        for i in list_tickers:
            if len(input_dict[i] <= requirement_length):
                print("Deleting Ticker: " + i + " due to insufficient data")
                del input_dict[i]

    def test(self):
        def initial_generate_positions(input_dictionary):
            eng_obj = Engine2(dict_of_dataframes = input_dictionary, base_lookback = self.base_lookback, number_of_readings = self.number_of_readings)
            longs, shorts = eng_obj.generate(absolute_list = False)
            account_size = self.initial_capital

            if(len(longs) <= self.number_of_readings):
                longs = longs[:self.number_of_readings]

            if(len(shorts) <= self.number_of_readings):
                shorts = shorts[:self.number_of_readings]

            self.number_of_live_positions = len(longs) + len(shorts)
            
            pcnt_allocation_longs = len(longs)/self.number_of_live_positions
            pcnt_allocation_shorts = len(shorts)/self.number_of_live_positions

            total_long_strength = 0
            total_short_strength = 0

            for i in longs:
                total_long_strength += i[1]
            
            for i in longs:
                datapoint_df = input_dictionary[i[0]].iloc[-1]
                print(datapoint_df)
                present_price = (datapoint_df['HIGH'] + datapoint_df['LOW'] + datapoint_df['CLOSE'])/3
                ticker = i[0]
                pcnt_pos = i[1]/total_long_strength
                num_of_shares = int((pcnt_pos*pcnt_allocation_longs*account_size)/present_price)
                self.position_list.append((ticker, "LONG", num_of_shares, present_price, 0, 1))
                self.cash -= num_of_shares*present_price

            for i in shorts:
                datapoint_df = input_dictionary[i[0]].iloc[-1]
                present_price = (datapoint_df['High'] + datapoint_df['Low'] + datapoint_df['Close'])/3
                ticker = i[0]
                pcnt_pos = i[1]/total_short_strength
                num_of_shares = int((pcnt_pos*pcnt_allocation_shorts*account_size)/present_price)
                self.position_list.append((ticker, "SHORT", num_of_shares, present_price, 0, 1))
                self.cash -= num_of_shares*present_price

        def portfolio_maintenance():
            #if(self.cash >  self.initial_capital/self.max_positions):
            pass
        def exit_positions():
            pass
        def present_positions():
            pass
        def log_pnl():
            pass
        def logging():
            pass
        def graphing():
            pass
        
        initial_generate_positions(self.input_dict)
        print(self.position_list)
