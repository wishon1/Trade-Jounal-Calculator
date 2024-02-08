#!/usr/bin/env python3
"""
Base mmosel for alll the classes in this project:
    Methods:
        Entry price, stoploss price, profit, strategy, picture:
"""
import os
from console.py import do_default.option

class BaseClass():
    """ contains all the core funtionality of the project"""
    new_instance = do_default.option()

    def __init__(self):
        self.__trasaction_date__ = transaction_date
        self.__entry__ = entry
        self.__stoploss__ = stoploss
        self.__take_profit__ = take_profit
        self.__risk_reward__ = risk_reward
        self.__trade_pic__ = trade_pic
        self.__trade_picAft__ = trade_picAft
        self.__tradestrategy__ = strategy

    def currency(self):
        """ currency pair"""
        pair = {1: GBPUSD, 2: AUDUSD, 3: NZDUSD, 4: GBPJPY, 5: EURJPY, 6: CADJPY, 7: AUDJPY} 
        print("\t\t------Please select a pair below--------")
        print(pair.dict())
        val = input("Please choose an option: ")
        int_val = input(val)

        if int_val == pair.key()[0]:
            val_x = input("1: View trade history or \n 2: Enter log :  ")
            val_y = str(val_x)

            if val_y == 2
            'Y':
                pass:
            else:
                add_record()


    def add_record(self):
        if 

