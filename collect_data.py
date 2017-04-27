#!/usr/bin/env python3
from DataCollection import dataCollection

'''
FAISAL MOHAMMAD
4/25/2017

data_collection - script to collection sample data one by one. Dictionary mapping containing how the user input is
converted into meaningful feature data is via the json files located in json_dictionaries directory. This script will
enter a data sample into all three data text files: raw_data, approach1_data, and approach2_data. - edit later

'''

data_collection = dataCollection()
card_x, card_y, winner = data_collection.collectData()
data_collection.insertData(card_x,card_y,winner)