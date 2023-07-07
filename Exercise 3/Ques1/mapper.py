#!/usr/bin/env python3

import sys
i=0

for line in sys.stdin:
    line = line.strip()
    acronym, name, year, city, category = line.split('\t')

    #skipping the header
    if i==0:
        i+=1
        continue

    print(city,'\t',1)
