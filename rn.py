#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script make batch renaming in current directory easy to use.
"""
import os
import re

ARGUMENTS = os.sys.argv
CWD = os.getcwd()
if len(ARGUMENTS) < 3:
    print("\n\
|------------------------------------------------------------|\n\
|=========              To rename files                  ====|\n\
|=========           Use regexp arguments                ====|\n\
|=========  rn.py PATTERN END_PATTERN [WORK DIRECTORY]   ====|\n\
|____________________________________________________________|")
    exit()

def rename_this(pattern, out_pattern, path):
    """
    Rename function. Read filelist from current directory and
    rename files from pattern to out_pattern.
    """
    counter = 0
    for filename in os.listdir(path):
        bingo = re.search(pattern, filename)
        if bingo:
            counter += 1
            print("Before:", filename)
            end_name = re.sub(pattern, out_pattern, filename)
            print("After:", end_name)
            os.rename(filename, end_name)
    print("Total files: %d" %counter)

try:
    rename_this(ARGUMENTS[1], ARGUMENTS[2], ARGUMENTS[3])
except IndexError:
    rename_this(ARGUMENTS[1], ARGUMENTS[2], CWD)
