#!/usr/bin/env python

from operator import itemgetter
import sys

import math

for line in sys.stdin:
    
    
    #TODO: actually go through correct stripping/assigning methods
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    # word, count = line.split('\t', 1)

    # # convert count (currently a string) to int
    # try:
        # count = int(count)
    # except ValueError:
        # # count was not a number, so silently
        # # ignore/discard this line
        # continue
    
    #split the varialbes and assign them
    print'%s' % (line)
