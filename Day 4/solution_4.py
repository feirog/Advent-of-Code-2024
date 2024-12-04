import pandas as pd
import re
import numpy as np

# First attempt at solving Task 1
data = ("MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX")
data_2 = [list(i) for i in data]
data_3 = np.array(data_2)

data_x = np.argwhere(data_3 == "X").tolist()
data_m = np.argwhere(data_3 == "M").tolist()
data_a = np.argwhere(data_3 == "A").tolist()
data_s = np.argwhere(data_3 == "S").tolist()

def touch_distance(p0, p1):
  distance_x = p1[0] - p0[0]
  distance_y = p1[1] - p0[1]
  distance = abs(distance_x * distance_y)
  return distance

print(data_3)
print(data_x)

total_xmas = 0
for x in data_x:
  nearby_m = []

  for m in data_m:
    if touch_distance(x,m) == 1:
      nearby_m.append(m)

  nearby_a = []
  for m in nearby_m:
    for a in data_a:
      if touch_distance(m,a) == 1:
        nearby_a.append(a)

  nearby_s = []
  for a in nearby_a:
    for s in data_s:
      if touch_distance(a,s) == 1:
        nearby_s.append(s)

  print(nearby_s)
  print("There were:",len(nearby_s),"XMAS!")
  total_xmas += len(nearby_s)
  print("That makes a total of:",total_xmas,"XMAS so far.")

# Second attempt at Task 1, with directions. Managed to solve with ChatGPT troubleshooting help.
data = open("input.txt").read().splitlines()
data_2 = [list(i) for i in data]
data_3 = np.array(data_2)

# Directions for adjacency (8 possible directions)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),]

def is_valid_position(pos, grid):
    return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]

def find_xmas(grid, pos, index, direction):
    word = "XMAS"
    if index == len(word):  # Found full "XMAS"!
        return 1

    next_pos = (pos[0] + direction[0], pos[1] + direction[1])

    if (is_valid_position(next_pos, grid) and grid[next_pos] == word[index]):
        return find_xmas(grid, next_pos, index + 1, direction)

    return 0

# Find all occurrences of "X"
total_xmas = 0
for x in np.argwhere(data_3 == "X"):
    for direction in directions:
        total_xmas += find_xmas(data_3, tuple(x), 1, direction)

print("Total XMAS occurrences:", total_xmas)

# Solution from Reddit user: 4HbQ
g, m = open('input.txt').read(), 'SAMX'

for f, l, s in (sum, 4, (1,140,141,142)), (all, 3, (140,142)):
    print(sum(f(g[i-x::x][:l] in (m[:l], m[:l][::-1]) for x in s)
                for i in range(len(g))))