#!/usr/bin/env python

from operator import itemgetter
import sys

cur_date = None
cur_tmp = 0
date = None

for line in sys.stdin:
    line = line.strip()
    date, tmp = line.split('\t', 1)
    
    try:
        tmp = int(tmp)
    except ValueError:
        continue
    if date == cur_date:
        if cur_tmp < tmp:
            cur_tmp = tmp
    else:
        if cur_date:
            print("%s\t%d" % (cur_date, cur_tmp))
        cur_date = date
        cur_tmp = tmp

if date == cur_date:
    print("%s\t%d" % (cur_date, cur_tmp))