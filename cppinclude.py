#!/usr/bin/env python3

import fileinput

for line in fileinput.input():
    str = []
    if line:
        str = ["#include <", line.strip(), ">"]
    print(''.join(str))
