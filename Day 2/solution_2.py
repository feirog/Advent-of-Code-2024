# -*- coding: utf-8 -*-

import pandas as pd

# Reading the data
data = pd.read_csv("input.txt", header = None)
data = data.reset_index()

#--------------------------------------------------------------------------------------------------------
# Task 1
count_safe = 0
count_unsafe = 0
for index, row in data.iterrows():
  print(row[0])
  listed = row[0].split(" ")
  separated_list = []
  count = 0
  length = len(listed)
  for number in listed:
    if count < (length-1):
      separated_list.append(int(listed[count+1])-int(listed[count]))
      count += 1
  print(separated_list)
  if all(number > 0 and number < 4 for number in separated_list):
    print("Safe, and positive!")
    count_safe += 1
  elif all(number < 0 and number > -4 for number in separated_list):
    print("Safe, and negative!")
    count_safe += 1
  else:
    print("Booooooom!!!!! (Unsafe)")
    count_unsafe += 1

print("There were", count_safe, "safe codes, and", count_unsafe, "explosions (unsafe).")

#--------------------------------------------------------------------------------------------------------
# Task 2
count_safe = 0
count_unsafe = 0

for index, row in data.iterrows():
  print(row[0])
  listed = row[0].split(" ") # Creates a list with each number
  separated_list = [] # Initiates an empty list for the differences
  count = 0
  length = len(listed)
  for number in listed: # Create the list with differences
    if count < (length-1):
      separated_list.append(int(listed[count+1])-int(listed[count]))
      count += 1
  print(separated_list)
  if all(number > 0 and number < 4 for number in separated_list): # If all are positive and less than four, safe
    print("Safe, and positive!")
    count_safe += 1
  elif all(number < 0 and number > -4 for number in separated_list): # If all are negative and over minus four, safe
    print("Safe, and negative!")
    count_safe += 1
  else: # We will be changing this for task 2
    print("Unsafe???")
    test_data = data.loc[index,data.columns[1]].split(" ") # Select the list we are having troubles with
    redemption = False # Initialize redemption, to calculate number of failed redemptions
    for i in range(len(test_data)): # Drop a number in the list in each loop
      temp_data = test_data[:]
      del temp_data[i-1]
      print(temp_data)
      new_separated = []
      new_count = 0
      new_length = len(temp_data)
      for new_number in temp_data: # And repeat the creation of the difference list
        if new_count < (new_length-1):
          new_separated.append(int(temp_data[new_count+1])-int(temp_data[new_count]))
          new_count += 1
      print(new_separated)
      if all(number > 0 and number < 4 for number in new_separated): # As well as the safety tests
        print("Actually safe, and positive!")
        count_safe += 1
        redemption = True
        break
      elif all(number < 0 and number > -4 for number in new_separated):
        print("Actually safe, and negative!")
        count_safe += 1
        redemption = True
        break
      else:
        print("Yup, booooooom!!!!!")
    if redemption == False:
      count_unsafe += 1

print("There were", count_safe, "safe codes, and", count_unsafe, "explosions (unsafe).")

#--------------------------------------------------------------------------------------------------------
# Solution from Advent Of Calendar reddit user @Independent_Check_62
def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False
data_1 = open('input.txt').read().split('\n')[:-1] # Had to add [:-1] to fix their code, since it was breaking due to an empty string at the end
data_2 = [[int(y) for y in x.split(' ')] for x in data_1]

safe_count = sum([is_safe(row) for row in data_2])
print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data_2])
print(safe_count)