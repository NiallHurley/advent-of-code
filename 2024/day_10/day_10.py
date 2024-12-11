#%%
daynum = "10"
import numpy as np
from tqdm.autonotebook import tqdm

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%
import numpy as np

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

def process_input(txt):
    tmp = []
    for t in txt:
        tmp.append([-1 if x=='.' else int(x)  for x in t])
    map_ = np.array(tmp)
    return map_

def find_trailhead_coords(map_,val = 0):
  x,y =  np.where(map_==val)
  return [c for c in zip(x,y) ]

def f1(map_,loc):
  # for this location try up/down/left/right and look for n+1... if n+1
  # count the number of n+1 = 9 and return that
  r = loc[0]
  c = loc[1]
  val = map_[loc]

  # print(loc,val)

  if val==9: # already have checked the bounds
    # print(loc)
    return loc

  R,C = map_.shape
  newlocs = []
   # step in each direction
  for dr,dc in dirs:
    newr, newc  = r+dr, c+dc
    if 0 <= newr < R and 0 <= newc < C:
      if  map_[(newr, newc)]==val+1: # i.e. we're at a
        newlocs.append((newr, newc))

  nines_found =[]
  for l in newlocs:
    newval =  map_[l]
    tmp =  f1(map_,l)

    # print(f"{newval} |  {l} |  {type(tmp)} | {tmp}")
    nines_found.append( tmp)
  return nines_found


# %%
def part1(txt):
    map_ = process_input(txt)
    retval = 0
    for startloc in find_trailhead_coords(map_):
        ans = f1(map_,startloc)
        while any([isinstance(l, list) for l in ans]):
            ans =  [item for row in ans for item in row]
        ans = set(ans)
        # print(f"{startloc}: {len(ans)} --  {ans}")
        retval+=len(ans)
    
    return retval    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    map_ = process_input(txt)
    retval = 0
    for startloc in find_trailhead_coords(map_):
        ans = f1(map_,startloc)
        while any([isinstance(l, list) for l in ans]):
            ans =  [item for row in ans for item in row]
        # ans = set(ans)
        # print(f"{startloc}: {len(ans)} --  {ans}")
        retval+=len(ans)
    
    return retval  

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
