#%%
daynum = "12"
import numpy as np
from tqdm.autonotebook import tqdm

# %%
import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to INFO or WARNING to reduce verbosity
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

# %%


with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%


import itertools

def tuple_diff(t1,t2):
    return (t1[0]-t2[0],t1[1]-t2[1])

def tuple_sum(t1,t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def get_all_pairs(list_):
    return list(itertools.combinations(list_, 2))

def get_area(l1):
    return len(l1)

def get_perimeter(l1):
    cell_perims = 4*len(l1) # count the perimeter of each cell 
    common_edges = 0
    for t in get_all_pairs(l1):
        tmp = tuple_diff(t[0],t[1])
        if tmp in dirs:
            common_edges+=1 
            # print(common_edges,t)
    return cell_perims - 2*common_edges # cos we've counted the perimeter of each cell 


    
def move_joining_locs_from_list2_to_list1(list1,list2):
    
    if not isinstance(list1, list):
        list1 = [list1]

    def is_element_one_away_from_anything_in_the_list(elem1, list1):
        return np.min([np.sum(np.abs(tuple_diff(elem1,c))) for c in list1])==1

    def elems_which_in_l2_and_are_1_away_from_at_least_1_elem_in_l2(l1,l2):
        a = [i for i,elem1 in enumerate(l2) if is_element_one_away_from_anything_in_the_list(elem1,l1) ]
        return [l2[ai] for ai in a]

    elem_moved = True
    while elem_moved:
        move_this = elems_which_in_l2_and_are_1_away_from_at_least_1_elem_in_l2(list1,list2)
        if len(move_this) == 0:
            break

        for m in move_this:
            list1.append(m)
            list2.remove(m)
    
    return list1,list2

def split_into_list_of_contiguous_lists(orig_list):
    remaining = orig_list
    output = [[]]
    output[0],remaining = move_joining_locs_from_list2_to_list1([remaining[0]],remaining[1:])
    logger.debug(f"{output} | {remaining}")
    while len(remaining)>0:
        tmp_output,remaining = move_joining_locs_from_list2_to_list1([remaining[0]],remaining[1:])
        output.append(tmp_output)
        logger.debug(f"{output} | {remaining}")
    
    # ensure we return list of lists
    if not isinstance(output[0],list):
        output = [output]
    return output

def get_num_sides(aa):
    unique_cols = list(set([b[1] for b in aa]))
    unique_rows = list(set([b[0] for b in aa]))
    out = 0
    for c in unique_cols:
        out+=len([b for b in aa if b[1]==c])

    for r in unique_rows:
        out+=len([b for b in aa if b[0]==r])  

    return out

# %%

import numpy as np
tmp = []
for t in txt:
  tmp.append([c for c in t])

map_ = np.array(tmp)
R,C = map_.shape

u_vals = np.unique(map_)
u = u_vals[0]
inds_tmp = np.where(map_==u)
inds = list(zip(*inds_tmp))
inds

# split inds of 'A' into lists of contiguous groups

dirs = [(0,1),(1,0),(-1,0),(0,-1)]

def check_bounds(map_,loc):
  R,C = map_.shape
  return 0<=loc[0]<R and 0<=loc[1]<C

# %%
logger.setLevel(logging.DEBUG)
ans = 0
list_of_groups = []
tmp = []
for t in txt.splitlines():
  tmp.append([c for c in t])

map_ = np.array(tmp)
R,C = map_.shape

u_vals = np.unique(map_)

for u in u_vals:
    inds_tmp = np.where(map_==u)
    inds = list(zip(*inds_tmp))


    remaining = inds
# list_of_groups[0] = current_group

# while we still have 'A' squares
# while len(remaining)>0:

    # for each element in 'remaining' find all
    #  neighbouring squares and if any are in the 'current_group
    #  then append them to the list
    
    
    current_group = [remaining[0]]
    new_remaining = remaining[1:]
    for t in remaining[1:]:
        for d in dirs:
            newloc = (t[0]+d[0],t[1]+d[1])

            if check_bounds(map_,newloc) and newloc in current_group and t not in current_group:
                # logger.debug(f"t: {t}")
                current_group.append(t)
                new_remaining.remove(t)
    list_of_groups.append(current_group)
    remaining = new_remaining # replace with the 'current group' values removed
    # logger.debug(f"remaining: {remaining}")
    logger.debug(f"current_group: {current_group}")
    # logger.debug(f"list_of_groups: {list_of_groups}")
    logger.debug(f"cost: {get_area(current_group)*get_perimeter(current_group)}")
    ans+= get_area(current_group)*get_perimeter(current_group)
    
ans


# %%
# asdf


logger.setLevel(logging.INFO)
def part1(txt):
    
    ans = 0
    list_of_groups = []
    tmp = []
    for t in txt:
        tmp.append([c for c in t])


    map_ = np.array(tmp)
    R,C = map_.shape

    u_vals = np.unique(map_)

    out =[]

    for u in tqdm(u_vals):
        inds_tmp = np.where(map_==u)
        inds = list(zip(*inds_tmp))

        list_of_lists = split_into_list_of_contiguous_lists(inds)

        out.append(np.sum([get_area(l)*get_perimeter(l) for l in list_of_lists]))

    return np.sum(out)

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    ans = 0
    list_of_groups = []
    tmp = []
    for t in txt:
        tmp.append([c for c in t])


    map_ = np.array(tmp)
    R,C = map_.shape

    u_vals = np.unique(map_)

    out =[]

    for u in tqdm(u_vals):
        inds_tmp = np.where(map_==u)
        inds = list(zip(*inds_tmp))

        list_of_lists = split_into_list_of_contiguous_lists(inds)

        try: 
            [get_area(l)*get_num_sides(l) for l in list_of_lists]
        except:
            print(f"L: {list_of_lists}")
        

        out.append(np.sum([get_area(l)*get_num_sides(l) for l in list_of_lists]))

print(f"Part 2 (test): {part2(test_txt)}")
# print(f"Part 2: {part2(input_txt)}")
# %%




list1 = [1,2,3,4,7,8,9]
l1 = []
l2 = list1




ans = 0
for t in get_all_pairs(list1):
    ans += np.abs(t[0]-t[1])

ans

# %%


C = list(set([(2, 5), (3, 3), (3, 4), (3, 5), (4, 4), (5, 4), (5, 5), (6, 5),(0, 6), (0, 7), (1, 6), (1, 7), (1, 8), (2, 6),(2, 5), (3, 5),(4,7)]))

l1 = [C[0]]
l2 = C[1:]

grp = C[0]
list1 = C[1:]

l2_element_one_away_from_current = [i for i,elem1 in enumerate(l2) if is_element_one_away_from_anything_in_the_list(elem1,l1) ]



# %%
# %%

def is_element_one_away_from_anything_in_the_list(elem1, list1):
    return np.min([np.sum(np.abs(tuple_diff(elem1,c))) for c in list1])==1

def is_any_element_in_list1_one_away_from_any_element_in_list2(list1,list2):
    return any([is_element_one_away_from_anything_in_the_list(elem1,list2) for elem1 in list2])
# %%
# pp1 = [(0,1),(0,2),(0,3)]
# pp2 = [(0,4),(0,5),(0,7),(0,8),(0,9)]

pp1 = [(0,1)]
pp2 = [(0,2),(0,3), (0,4),(0,5),(0,7),(0,8),(0,9), (2,1),(2,2)]

def move_joining_locs_from_list2_to_list1(list1,list2):
    
    if not isinstance(list1, list):
        list1 = [list1]

    def is_element_one_away_from_anything_in_the_list(elem1, list1):
        return np.min([np.sum(np.abs(tuple_diff(elem1,c))) for c in list1])==1

    def elems_which_in_l2_and_are_1_away_from_at_least_1_elem_in_l2(l1,l2):
        a = [i for i,elem1 in enumerate(l2) if is_element_one_away_from_anything_in_the_list(elem1,l1) ]
        return [l2[ai] for ai in a]

    elem_moved = True
    while elem_moved:
        move_this = elems_which_in_l2_and_are_1_away_from_at_least_1_elem_in_l2(list1,list2)
        if len(move_this) == 0:
            break

        for m in move_this:
            list1.append(m)
            list2.remove(m)
    
    return list1,list2

    # print(f"{list1} |  {list2} ")

l1,l2 = move_joining_locs_from_list2_to_list1(pp1,pp2)
print(f"result: {l1} |  {l2} ")
# %%

pp1 = [(0,1)]
pp2 = [(0,2),(0,3), (0,4),(0,5),(0,7),(0,8),(0,9), (2,1),(2,2)]

l1,l2 = move_joining_locs_from_list2_to_list1(pp1,pp2)
print(f"result: {l1} |  {l2} ")
l21,l31 = move_joining_locs_from_list2_to_list1([l2[0]],l2[1:])
print(f"result: {l21} |  {l31} ")

# %%

def split_into_list_of_contiguous_lists(orig_list):
    remaining = orig_list
    output = [[]]
    output[0],remaining = move_joining_locs_from_list2_to_list1([remaining[0]],remaining[1:])
    print(f"{output} | {remaining}")
    while len(remaining)>0:
        tmp_output,remaining = move_joining_locs_from_list2_to_list1([remaining[0]],remaining[1:])
        output.append(tmp_output)
        print(f"{output} | {remaining}")
    
    # ensure we return list of lists
    if not isinstance(output[0],list):
        output = [output]
    return output
# %%

aa = [(1, 2), (2, 2), (2, 3), (3, 3)]
[b[1] for b in aa]
# %%



# %%
tmp = []
for l in """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""".splitlines():
    tmp.append([1 if t == 'E' else 0 for t in l])
tmp = np.array(tmp)
tmp+0.5


# np.diff(np.fliplr(tmp),axis=1)



# %%
