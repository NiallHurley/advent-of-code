#%%
daynum = "06"
import numpy as np

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%
from tqdm.autonotebook import tqdm
def complex_to_tuple(c):
   return (int(c.real), int(c.imag))

def rotateR(curdir):
    return curdir*complex(0,-1)

def process_input(txt):
    tmp = []
    for l in txt:
        tmp.append([x for x in l])

    map_ = np.array(tmp)
    # print(map_)

    visited = []
    visited_pt2 = []

    a,b = np.where(map_=='^')
    start_loc = (a[0],b[0])
    start_dir = complex(-1,0)
    return map_,start_loc, start_dir

def loop_detector(map_,start_loc,start_dir,visited = []):
    maxiter = 10000000
    loc = start_loc
    dir = start_dir
    visited.append([loc,dir])
    iter = 0
    while True:
        iter+=1
        if iter>maxiter:
            return None
        # take a step
        new_loc = complex_to_tuple(complex(loc[0],loc[1]) + dir)

        if [new_loc,dir] in visited:
            # print([loc,dir],visited)
            return True # loop found  

        # print(new_loc, dir)
        # check boundary
        hit_boundary =  (new_loc[0]>=map_.shape[0] or
                        new_loc[1]>=map_.shape[1] or
                        new_loc[0]<0 or
                        new_loc[1]<0 )
     
        if hit_boundary:
            return False # loop not found  
        elif map_[new_loc]=='#':
            # change dir
            dir = rotateR(dir)
            visited.append([loc,dir])
        else:
            loc = new_loc
            visited.append([new_loc,dir])

# %%
def part1(txt):
    map_,start_loc, start_dir = process_input(txt)

    loc = start_loc
    dir = start_dir
    visited = []
    visited.append(loc)
    visited_pt2=[]
    visited_pt2.append([loc,dir])

    while True:
        # take a step
        new_loc = complex_to_tuple(complex(loc[0],loc[1]) + dir)
        # print(new_loc)
        # check boundary
        hit_boundary =  (new_loc[0]>=map_.shape[0] or
                        new_loc[1]>=map_.shape[1] or
                        new_loc[0]<0 or
                        new_loc[1]<0 )
        if hit_boundary:
            break
        elif map_[new_loc]=='#':
            # change dir
            dir = rotateR(dir)
            visited_pt2.append([new_loc,dir])
        else:
            loc = new_loc
            visited.append(new_loc)
            visited_pt2.append([new_loc,dir])


    return len(set(visited)), visited  

print(f"Part 1 (test): {part1(test_txt)[0]}")
print(f"Part 1: {part1(input_txt)[0]}")

# %%

def out_of_bounds(new_loc, map_):
    return (new_loc[0]>=map_.shape[0] or
                        new_loc[1]>=map_.shape[1] or
                        new_loc[0]<0 or
                        new_loc[1]<0 )
    
# %%

def part2(txt):

    map_,start_loc, start_dir = process_input(txt)

    cnt = 0
    i = 0
    poslist =[]
    # [v for v in part1(input_txt)[1]]
    # add entries adjacent to the path
    vlist  = set([v for v in part1(input_txt)[1]]+
        [(v[0]+1,v[1]) for v in part1(input_txt)[1]]+
        [(v[0]-1,v[1]) for v in part1(input_txt)[1]]+
        [(v[0],v[1]+1) for v in part1(input_txt)[1]]+
        [(v[0],v[1]-1) for v in part1(input_txt)[1]])
    for pos in tqdm(list(vlist)):
        if not out_of_bounds(pos,map_):
            if map_[pos] == '.' :
                newmap = map_.copy()
                newmap[pos] = '#'
                if loop_detector(newmap,start_loc,start_dir,visited = []):
                    cnt+=1
                    poslist.append(pos)
        i+=1
        
    print([cnt, len(set(poslist))], len(poslist))
    return cnt

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")

# 1933
# %%

map_,start_loc, start_dir = process_input(input_txt)

cnt = 0
i = 0
poslist =[]
# [v for v in part1(input_txt)[1]]
# add entries adjacent to the path
vlist  = set([v for v in part1(input_txt)[1]]+
    [(v[0]+1,v[1]) for v in part1(input_txt)[1]]+
    [(v[0]-1,v[1]) for v in part1(input_txt)[1]]+
    [(v[0],v[1]+1) for v in part1(input_txt)[1]]+
    [(v[0],v[1]-1) for v in part1(input_txt)[1]])
for r in tqdm(range(map_.shape[0])):
    for c in tqdm(range(map_.shape[1])):
        pos = (r,c)
        if not out_of_bounds(pos,map_):
            if map_[pos] == '.' :
                newmap = map_.copy()
                newmap[pos] = '#'
                if loop_detector(newmap,start_loc,start_dir,visited = []):
                    cnt+=1
                    poslist.append(pos)
    i+=1
    
print([cnt, len(set(poslist))], len(poslist))




# %%

cnt = 0
i = 0
poslist =[]
for pos in list(set([v[0] for v in part1(test_txt)[1]])):
    if map_[pos] == '.' :
        newmap = map_.copy()
        newmap[pos] = '#'
        if loop_detector(newmap,start_loc,start_dir,visited = []):
            cnt+=1
            poslist.append(pos)
    i+=1
    
[cnt, len(set(poslist))]
# %%

# test loop detector ... 
tmp = []
for l in test_txt:
    tmp.append([x for x in l])

map_ = np.array(tmp)


locs = [v[0] for v in part1(test_txt)[1]]
pos = (7,4)
assert map_[pos] == '.' 
newmap = map_
newmap[pos] = '#'


visited = []
loc = start_loc
dir = start_dir
visited.append([loc,dir])
for i in range(1000):
    # take a step
    new_loc = complex_to_tuple(complex(loc[0],loc[1]) + dir)

    if [new_loc,dir] in visited:
        # print([loc,dir],visited)
        print(1) # True # loop found  
        break

    print(new_loc, dir)
    # check boundary
    hit_boundary =  (new_loc[0]>=newmap.shape[0] or
                    new_loc[1]>=newmap.shape[1] or
                    new_loc[0]<0 or
                    new_loc[1]<0 )
    
    if hit_boundary:
        print(0) # False # loop not found 
        break 
    elif newmap[new_loc]=='#':
        # change dir
        dir = rotateR(dir)
        visited.append([loc,dir])
    else:
        loc = new_loc
        visited.append([new_loc,dir])

    
     

# %%
[(6,3),(7,6),(7,7),(8,1),(8,3),(9,7)]

['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']]