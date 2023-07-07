#!/usr/bin/env python3

import sys

previous_data =""
previous_data_count = 0
current_data = ""
previous_location = ""
previous_year=""


for line in sys.stdin:
    #removing the whitespace
    line = line.strip()

    current_data,_= line.split('\t',1)
    current_location, current_year = current_data.split('_',1)


    if previous_data  == current_data:
        previous_data_count+=1

    else:
        if previous_data :
            dates = previous_year.split('-')
            year = dates[0].split(',')[1].strip()
            date = year
            print(previous_location,'\t',date,'\t',previous_data_count)
        previous_data_count = 1
        previous_data = current_data
        previous_year = current_year
        previous_location = current_location
dates = previous_year.split('-')
year = dates[0].split(',')[1].strip()
date = year
print(previous_location,'\t',date,'\t',previous_data_count)