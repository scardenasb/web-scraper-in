#! /usr/bin/env python

import os


# TODO: Connect a sql base to keep track of this data
# TODO: Schedule an autoexe to run this scrip once a day (heroku add on)
os.system("python3 ./src/connector.py")
