#!/usr/bin/env python3

import sys

previous_location =""
previous_location_count =0
current_location = ""

for line in sys.stdin:
    #removing the whitespace
    line = line.strip()

    current_location,_ = line.split('\t',1)

    if previous_location == current_location:
        previous_location_count+=1

    else:
        if previous_location:
            print(previous_location,'\t',previous_location_count)
        previous_location_count = 1
        previous_location = current_location

print(previous_location,'\t', previous_location_count)