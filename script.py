#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utilities
import sys
import subprocess

species = utilities.blast_to_dict(sys.argv[1], 30, 40)

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
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
