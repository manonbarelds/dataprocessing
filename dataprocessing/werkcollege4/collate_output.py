#!/usr/bin/env python3

"""collate_output.py"""

with open(snakemake.output[0], 'w') as out:
    for i in snakemake.input:
        sample = i.split('.')[0]
        for line in open(i):
            out.write(sample + ':' + line)
