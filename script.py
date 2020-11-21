#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import utilities
import sys
import subprocess
import glob
import time
import csv

window = int()

# prepare output file
csv_file = open("results.csv", "w")
fieldnames = ["instance", "window", "mean runtime"]
csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
csv_writer.writeheader()

for filename in glob.glob("benchmarks/*.txt"): # for each protein
    max_length = utilities.sequence_length(filename) # get the length of the smaller protein
    while(window*10+10 < max_length): # while the window is smaller than the smaller prot
        runtime = 0
        for i in range(100): # 100 repetitions
            species = utilities.blast_to_dict(filename, window*10, window*10+10) # convert protein sequences in dict protein:states
            result=open("Problem.dzn", "w") # the datafile for minizinc
            neighbourhood = utilities.create_neighborhoods(species) # create dict state:neighbors

            result.write(utilities.dict_keys_to_mzn_enum(neighbourhood) + "\n") # write enum in the datafile
            print(str(len(neighbourhood)))
            result.write(utilities.dict_to_mzn_array(neighbourhood, "share_species") + "\n") # write array of neighbors
            result.write(utilities.dict_to_mzn_array(utilities.create_incompatibilities(species), "incompatibilities") + "\n") # write array of incompatibilities
            result.write(utilities.dict_keys_to_mzn_set(neighbourhood) + "\n") # write 1..(total number of nodes)
            result.write(utilities.dict_keys_to_mzn_axis(neighbourhood, "1") + "\n") # write (first node)..(end node) 
            result.write(utilities.dict_keys_to_mzn_axis(neighbourhood, "2") + "\n") # same but for the 2nd axis
            result.close()

            command = ["minizinc", "--time-limit", "1800000", "--solver", "Gecode", "Problem.mzn", "Problem.dzn"] # launch minizinc with proper parameters
            
            # measuring runtime
            start = time.time()
            result_process = subprocess.run(command, capture_output=True, text=True)
            end = time.time()
            runtime = runtime + (end - start)
            print(result_process.stdout)
            
        runtime = runtime / 20
        csv_writer.writerow({'instance': filename.split("/")[-1], 'Window': str(window), 'mean runtime': str(runtime)})
        window += 1 # increase size of the window
    window = 0
