#%%
daynum = "04"
import numpy as np

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%

# generate all directions (lazily!)

import itertools
dirs = []
for r in itertools.product([-1,0,1], [-1,0,1]):
    dirs.append((r[0], r[1]))
dirs   

# %%
def part1(txt):
    # Part 1
    tmp = []
    for l in txt:
        tmp.append([(x) for x in l])

    tmp = np.array(tmp)
    R,C = tmp.shape

    cnt=0

    for r in range(R):
        for c in range(C):
            # print((r,c))
            for dir in dirs:
                dr, dc = dir
                if (0<=r+dr*3<=R-1 and  0<=c+dc*3<=C-1):
                    if 'XMAS' == tmp[r,c]+tmp[r+dr*1,c+dc*1]+tmp[r+dr*2,c+dc*2]+tmp[r+dr*3,c+dc*3]:
                        cnt+=1

    return cnt
    

  

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    # Part2
    tmp = []
    for l in txt:
        tmp.append([(x) for x in l])

    tmp = np.array(tmp)
    R,C = tmp.shape
    cnt=0

    for r in range(R):
        for c in range(C):
            # print((r,c))
            local_cnt = 0
            local_tmp =[]
            for dir in [(-1, -1), (-1, 1),  (1, -1), (1, 1)]: # only diagonals!
                dr, dc = dir

                if tmp[r,c]=='A':

                    if (r-dr)<0 or (r+dr)<0     or (r-dr)>R-1 or (r+dr)>R-1    or (c+dc)<0 or (c-dc)<0   or (c+dc)>C-1  or (c-dc)>C-1:
                        # we've hit a boundary
                        pass
                    else:
                        str1 = tmp[r-dr,c-dc]+tmp[r+0,c+0]+tmp[r+dr,c+dc]
                        if 'MAS' == str1:
                            local_cnt+=1
                            # local_tmp.append([(r,c),dir, str1])
            if local_cnt>1:
                cnt+=1
        
    return cnt

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
