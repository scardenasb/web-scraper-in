#! /usr/bin/env python

import os


# TODO: Connect a sql base to keep track of this data
# TODO: Schedule an autoexe to run this scrip once a day
os.system('python3 web.py >> counter.txt')
