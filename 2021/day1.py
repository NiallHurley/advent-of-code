#%%
daynum = 1

import numpy as np

with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

# %%
   
def sum_postive_changes(txt):
   return(np.sum([1 for x in np.diff([int(x) for x in txt]) if x>0]))

def part2_len3_rolling_window(txt):
   base = np.array([int(x) for x in txt])
   newbase = base[0:-2]+base[1:-1]+base[2:]
   return(np.sum([1 for x in np.diff([x for x in newbase]) if x>0]))


# %%
def part1(txt):
   return sum_postive_changes(txt)

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
   return part2_len3_rolling_window(txt)

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
