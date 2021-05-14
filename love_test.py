#!/usr/bin/env python

import re

shakes = open("pg1041.txt", "r")
love = open("love_test.txt", "w")

for line in shakes:
    if re.match("(.*)(L|l)ove(.*)", line):
        print(line)  
        love.write(line)
