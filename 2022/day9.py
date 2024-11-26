#%%
daynum = 9

with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

import numpy as np

# %%

[x.split(' ') for x in test_txt]
dirs = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)} # directions in matrix index

r,c = dirs[dirlet]

# %%
def part1(txt):
   return 0

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1 : {part1(input_txt)}")

# %%

def part2(txt):
   return 0

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2 (test): {part2(input_txt)}")

# %%

   