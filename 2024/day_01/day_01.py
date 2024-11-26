#%%
daynum = 1
import numpy as np

with open(f"day{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]

# %%
def part1(txt):
    return None

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    return None

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
