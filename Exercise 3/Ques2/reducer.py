#!/usr/bin/env python3

import sys

previous_location =""
current_location = ""
con_list=[]

for line in sys.stdin:
    #removing the whitespace
    line = line.strip()

    current_location,con_name= line.split('\t',1)


    if previous_location == current_location:
        con_list.append(con_name)

    else:
        if previous_location:
            print(previous_location,'\t',con_list)
        con_list=[con_name]
        previous_location = current_location

print(previous_location,'\t', con_list)