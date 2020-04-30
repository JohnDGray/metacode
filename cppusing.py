#!/usr/bin/env python3

import fileinput

results = []
for line in fileinput.input():
    s = []
    if line:
        line = line.strip().replace('/', '::')
        s = ["using ", line.strip(), ";"]
    results.append(''.join(s))
zipped = [(x, y) for x, y in zip(results[::2], results[1::2])]
for pair in zipped:
    l = 40-len(pair[0])
    print(''.join(pair[0] + ' ' * l + pair[1]))
if results and len(results) % 2 == 1:
    print(''.join(results[-1]))
