#%%
daynum = "15"
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


test_txt2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<""".splitlines()




#%%

def process_input(txt):
    tmp1 = []
    tmp2 = []
    for t in txt:
        if len(t)>0:
            if t[0]=='#':
                tmp1.append([x for x in t])
            else:
                tmp2.append(t)
    map_ = np.array(tmp1)
    moves = ''.join(tmp2)
    return map_, moves

map_, moves = process_input(test_txt2)
sloc = list(zip(*np.where(map_=='@')))[0]

def tuple_add(t1, t2):
    return (t1[0]+t2[0],t1[1]+t2[1])

def print_map(map_,indent=0):
    [print(' '*indent + ''.join(m)) for m in map_]

def coords_where(map_,value):
    return list(zip(*np.where(map_==value)))

def get_next_loc(curr_loc, dir):
    if dir == '^':
        next_loc = tuple_add(curr_loc,(-1,0))
    elif dir == 'v':
        next_loc = tuple_add(curr_loc,(1,0))
    elif dir == '>':
        next_loc = tuple_add(curr_loc,(0,1))
    elif dir == '<':
        next_loc = tuple_add(curr_loc,(0,-1))
    else:
        next_loc = np.nan
    return next_loc

def make_a_move(curr_loc, direction, map_):
    logger.debug(f"{curr_loc} [{map_[curr_loc]}] {direction} ")
    next_loc = get_next_loc(curr_loc, direction)
    logger.debug(f"MAM1 {curr_loc} -> {next_loc} [{map_[curr_loc]} -> {map_[next_loc]}] {direction} ")
    curr_val = map_[curr_loc]
    next_val = map_[next_loc]

    if map_[next_loc] == '.':
        # swap the values!!
        map_[next_loc] = curr_val
        map_[curr_loc] = next_val
    
    elif next_val=='#':
        # do nothing
        pass

    elif next_val in 'O[]':
        # call the function as if we're at this place already... (i.e. check if there's a box ... )
        logger.debug(f"MAM1 recursive call {next_loc} [{map_[next_loc]}] {direction} ")
        map_ = make_a_move(next_loc, direction, map_)
        # if this has freed up a space then move!
        if map_[next_loc] == '.':
            # swap the values!!
            curr_val = map_[curr_loc]
            next_val = map_[next_loc]
            map_[next_loc] = curr_val
            map_[curr_loc] = next_val    
    return map_


# %%
logger.setLevel(logging.INFO)
def part1(txt):
    map_, moves = process_input(txt)
    for direction in moves:
        map_ =  make_a_move(list(zip(*np.where(map_=='@')))[0] , direction, map_)

    return np.sum([box[0]*100+box[1] for box in list(zip(*np.where(map_=='O')))])    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %% ############ PART 2 #######################

# If the tile is #, the new map contains ## instead.
# If the tile is O, the new map contains [] instead.
# If the tile is ., the new map contains .. instead.
# If the tile is @, the new map contains @. instead.

test_txt3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^""".splitlines()

def process_input_part2(txt):
    tmp1 = []
    tmp2 = []
    for t in txt:
        if len(t)>0:
            if t[0]=='#':
                t = t.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')
                tmp1.append([x for x in t])
            else:
                tmp2.append(t)
    map_ = np.array(tmp1)
    moves = ''.join(tmp2)
    return map_, moves

def check_box_alignments(map_):
    lb = list(zip(*np.where(map_=='[')))
    all_lbs_have_rbs = np.all([map_[tuple_add(l,(0,1))]==']' for l in lb])
    rb = list(zip(*np.where(map_==']')))
    all_rbs_have_lbs = np.all([map_[tuple_add(r,(0,-1))]=='[' for r in rb])
    return all_lbs_have_rbs and all_rbs_have_lbs

# works on a list of len 2
def get_next_locs(curr_locs,direction):
    assert len(curr_locs)==2, "def get_next_locs(curr_locs) works only on list of len 2"
    next_locs =[]
    next_locs.append(get_next_loc(curr_locs[0], direction))
    next_locs.append(get_next_loc(curr_locs[1], direction))
    return next_locs

# works on a list of len 2 - returns a list of vals
def get_vals(map_,locs):
    return [map_[c] for c in locs]

def make_a_move_part2_2_2(curr_loc, direction, map_):

    next_loc = get_next_loc(curr_loc, direction)
    if printy:
        print(f"{curr_loc} -> {next_loc} .... {map_[curr_loc]} -> {map_[next_loc]} ...  {direction} ")
    curr_val = map_[curr_loc]
    next_val = map_[next_loc]

    if direction in '<>':
        # then we can just use part 1
        map_ = make_a_move(curr_loc, direction, map_)
        if printy:
            print_map(map_, 9)
        return map_
    
    # else!! i.e. direction in '^v'

    if next_val == '.':
        # swap the values!!
        map_[next_loc] = curr_val
        map_[curr_loc] = next_val
        if printy:
            print(f'swapping {curr_val} for {next_val}')
    
    elif next_val=='#':
        # do nothing
        pass

    elif next_val in '[]':
        # let's make a map copy and try do all the moves and see if it all works! 
        if curr_val=='@':
            map_orig = map_.copy()

        # get side val... 
        if next_val == '[':
            # we need to move this val and the one to the right.. 
            side_loc = get_next_loc(next_loc,'>')
        else:  # next_val == '[':
            # we need to move this val and the one to the left.. 
            side_loc =  get_next_loc(next_loc,'<')
        
        # now let's try move both next_val and the side_val i.e. the other side of the box
        map_ = make_a_move_part2_2_2(next_loc, direction, map_)
        next_val = map_[next_loc]
        if next_val == '.':
            # swap the values!!            
            map_[next_loc] = curr_val
            map_[curr_loc] = next_val
        if printy:
            print(f'swapping {curr_val} for {next_val}')
            print(f"1: {next_loc}, {map_[next_loc]}")
            print_map(map_)
            
        # move the other half of the box 
        side_val=map_[side_loc]
        next_side_loc = get_next_loc(side_loc,direction)
        next_side_val = map_[next_side_loc]
        if next_side_val == '.':
            # swap the values!!            
            map_[next_side_loc] = side_val
            map_[side_loc] = next_side_val
        else:
            map_ = make_a_move_part2_2_2(side_loc, direction, map_)
            if next_side_val == '.':
                # swap the values!!            
                map_[next_side_loc] = side_val
                map_[side_loc] = next_side_val

        if printy:
            print(f"aligned? :{check_box_alignments(map_)}")
        if curr_val=='@':
            # if map_[next_loc] == '.':
            # swap the values!!
            
            if not check_box_alignments(map_):
                map_ = map_orig.copy()

    return map_


# %%
logger.setLevel(logging.INFO)
printy = False
def part2(txt):
    map_, moves = process_input_part2(txt)
    for direction in moves:
        curr_loc = list(zip(*np.where(map_=='@')))[0] 
        # curr_locs = [curr_loc, get_next_loc(curr_loc,'>')]
        map_ =  make_a_move_part2_2_2(list(zip(*np.where(map_=='@')))[0] , direction, map_)
    [print(''.join(m)) for m in map_]
    

    return np.sum([box[0]*100+box[1] for box in list(zip(*np.where(map_=='[')))])  

print(f"Part 2 (test 3): {part2(test_txt3)}")
print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# 1478960 too low
# %%


# testing ground:

logger.setLevel(logging.DEBUG)
map_, moves = process_input_part2(test_txt3)
print_map(map_)
map_2 = map_
# print_map(map_2)
for i in range(5):
    if i>=0:
        logger.setLevel(logging.DEBUG)
    curr_loc = list(zip(*np.where(map_2=='@')))[0] 
    map_2 = make_a_move_part2_2(curr_loc, moves[i], map_2)
    if i>=0:
        print()
        print(f"{curr_loc}    {moves[i]}")
        print_map(map_2)

print('--------')
print_map(map_2) 
print('--------') 
curr_loc = list(zip(*np.where(map_2=='@')))[0] 
curr_val = map_[curr_loc]
# map_2= make_a_move_part2(curr_loc, '^', map_2)
# print_map(map_2)  
# print(curr_val)      

# get_next_loc(next_loc, '>')
# map_2 = make_a_move(get_next_loc(next_loc, '<'), '^', map_2)
# print_map(map_2)        
# %%
direction='^'
next_loc = get_next_loc(curr_loc, direction)
curr_val = map_[curr_loc]
next_val = map_[next_loc]
map_tmp = map_.copy()
map_tmp = make_a_move_part2_2(next_loc, direction, map_tmp)
print(f"step 1 {next_val} ")
print_map(map_tmp,1) 
print(f"step 2 {next_val} ")
if next_val=='[':
    # then also move the cell to the right
    map_tmp = make_a_move_part2(get_next_loc(next_loc, '>'), direction, map_tmp)
    print(f"map_tmp 2 right bracket:  ")
    print_map(map_tmp,indent=5)
elif next_val==']':
    # then also move the cell to the left
    map_tmp = make_a_move_part2(get_next_loc(next_loc, '<'), direction, map_tmp)
    print(f"map_tmp 2 left bracket:  ")
    print_map(map_tmp,indent=7)

print_map(map_tmp,1) 
# %%







