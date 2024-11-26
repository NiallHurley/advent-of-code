#%%
daynum = 2
import numpy as np

with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

# %%
   
def parse_txt1(txt):
   x = 0
   y = 0
   for instr in txt: 
      tmp=  instr.split(' ')
      dir = tmp[0]
      val = int(tmp[1])
      match dir:
         case 'forward':
            x += val
         case 'up':
            y -= val
         case 'down':
            y += val
   return(x*y)

def parse_txt2(txt):
   x = 0
   y = 0
   aim = 0
   for instr in txt: 
      tmp=  instr.split(' ')
      dir = tmp[0]
      val = int(tmp[1])
      match dir:
         case 'forward':
            x += val
            y += val*aim
         case 'up':
            aim -= val
         case 'down':
            aim += val
   return(x*y)

# %%
def part1(txt):
   return parse_txt1(txt)

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
   return parse_txt2(txt)

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
