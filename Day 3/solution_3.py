import pandas as pd
import re

# Task 1 - inspiration from Reddit user @mate_de_pomelo
data = open('input.txt').read()
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

matches = list(pattern.finditer(data)) # Create a list of matches for mul(1-3 digits, 1-3 digits)
multiplied = [eval(match.group()[3:])[0] * eval(match.group()[3:])[1] for match in matches] # Evaluate each match as a tuple and multiply
print("Answer to task 1 is:",sum(multiplied))

# Task 2
data_2 = data.split("do") # Split the data by "do"
do = True
multiplied_2 = 0
for i, seq in enumerate(data_2):
    if i > 0: # Skip the first entry
        if seq.startswith("n't()"): # If a don't has appeared, then don't do the addition
            do = False
        elif seq.startswith("()"): # If a do has appeared, then do
            do = True
    if do:
        matches_2 = pattern.finditer(seq)
        multiplied_2 += sum([eval(match.group()[3:])[0] * eval(match.group()[3:])[1] for match in matches_2])


print("Answer to task 2 is:",multiplied_2)