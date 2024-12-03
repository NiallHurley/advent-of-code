#%%
daynum = "03"
import numpy as np

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


# %%
def part1(txt):
    tmp = [l.split(')') for l in ''.join(txt).split('mul(')]
    ret=0
    for t in tmp:
        try:
            a,b= t[0].split(',')
            ret += int(a)*int(b)
        except:
            pass     
    return ret

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    # these are all the bits that start with 'don't()'
    tmp = ''.join(txt).split('don\'t()')

    # drop the bit before the 'do()'
    tmp2 = [''.join(t.split('do()')[1:]) if 'do()' in t else '' for t in tmp]
    # add back in the very first bit (before the first don't() )
    tmp3 = tmp[0]+''.join(tmp2)

    # same as first bit now
    return part1(tmp3)

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
