#!/usr/bin/env python
# -*- coding: utf-8 -*-
#FIXME fix window gestion
import utilities
import sys
import subprocess
import glob
import time
import csv

window = int()

csv_file = open("results.csv", "w")
fieldnames = ["Instance", "Windows", "runtime"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
csv_writer.writeheader()

for filename in glob.glob("benchmarks/*.txt"):
    max_length = utilities.sequence_length(filename)
    while(window*10+10 < max_length):
        species = utilities.blast_to_dict(filename, window*10, window*10+10)
        result=open("Problem.dzn", "w")
        neighbourhood = utilities.create_neighborhoods(species)

        result.write(utilities.dict_keys_to_mzn_enum(neighbourhood) + "\n")
        result.write(utilities.dict_to_mzn_array(neighbourhood, "share_species") + "\n")
        result.write(utilities.dict_to_mzn_array(utilities.create_incompatibilities(species), "incompatibilities") + "\n")
        result.write(utilities.dict_keys_to_mzn_set(neighbourhood) + "\n")
        result.write(utilities.dict_keys_to_mzn_axis(neighbourhood, "1") + "\n")
        result.write(utilities.dict_keys_to_mzn_axis(neighbourhood, "2") + "\n")
        result.close()

        command = ["minizinc", "--solver", "Gecode", "Problem.mzn", "Problem.dzn"]
        start = time.time()
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=60)
            end = time.time()
            result = end - start
        except subprocess.TimeoutExpired:
            print("Instance not solvable")
            result = "None"
        
        csv_writer.writerow({'Instance': filename.split("/")[-1], 'Windows': str(window), 'runtime': str(result)})
        window += 1
