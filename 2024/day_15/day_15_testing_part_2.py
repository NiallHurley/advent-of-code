#%%
daynum = "15"
import numpy as np
from tqdm.autonotebook import tqdm

printy = True


with open(f"2024/day_15/day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"2024/day_15/day_{daynum}_input.txt", "r") as f:
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

def make_a_move(curr_loc, direction, map_):
    next_loc = get_next_loc(curr_loc, direction)
    print(f"MAM1 {curr_loc} -> {next_loc} [{map_[curr_loc]} -> {map_[next_loc]}] {direction} ")
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
        print(f"MAM1 recursive call {next_loc} [{map_[next_loc]}] {direction} ")
        map_ = make_a_move(next_loc, direction, map_)
        # if this has freed up a space then move!
        if map_[next_loc] == '.':
            # swap the values!!
            curr_val = map_[curr_loc]
            next_val = map_[next_loc]
            map_[next_loc] = curr_val
            map_[curr_loc] = next_val    
    return map_

def make_a_move_part2_2(curr_loc, direction, map_):
    
    print(f"MAM2-2  initial {curr_loc} `{map_[curr_loc]}` {direction} ")
    if printy:
        print('MAM2-2')

    next_loc = get_next_loc(curr_loc, direction)
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
        map_ = make_a_move_part2_2(next_loc, direction, map_)
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
            map_ = make_a_move_part2_2(side_loc, direction, map_)
            if next_side_val == '.':
                # swap the values!!            
                map_[next_side_loc] = side_val
                map_[side_loc] = next_side_val

        # if map_[next_side_loc] == '.': # if the box moved successfully with the recursive call
            

        
        # if printy:
        #     print(f"2: {side_loc}, {map_[side_loc]}  - {next_side_loc},{map_[next_side_loc]}")
        #     print_map(map_)
        #     print()
            
        #     print('success!!')
        # print(f'swapping {curr_val} for {next_val}  ----locs:  {curr_loc} to {next_loc}')
        # if map_[next_loc] == '.':
            # map_ = make_a_move_part2_2(curr_loc, direction, map_)
        # next_next_loc = get_next_loc(next_loc,direction)
        # if map_[next_side_loc] == '.' and map_[next_next_loc] == '.' :
        #     # swap the values!!
        #     if printy:
        #         print(f" -- 2: {side_loc}, {map_[side_loc]}  - {next_side_loc},{map_[next_side_loc]}")
        #     side_val = map_[side_loc]
            
        #     map_[side_loc] = '.'
        #     map_[next_side_loc] = side_val

        #     next_val = map_[next_loc]
            
        #     map_[next_loc] = '.'
        #     map_[next_next_loc] = next_val

        #     next_val = map_[next_loc]
        #     map_[next_loc] = curr_val
        #     map_[curr_loc] = next_val

        # if printy:    
        #     print_map(map_)
        #     print()
        

        # print(f'swapping {curr_val} for {next_val}')
        
        # if map_[next_loc]=='.':
        #     print('success!!')
        #     print(f'swapping {curr_val} for {next_val}  ----locs:  {curr_loc} to {next_loc}')

        # # if map_[next_loc] == '.':
        #     # swap the values!!
        #     next_val = map_copy[next_loc]
        #     map_copy[next_loc] = curr_val
        #     map_copy[curr_loc] = next_val
        #     print(f'swapping {curr_val} for {next_val}')


        
        if printy:
            print(f"aligned? :{check_box_alignments(map_)}")
        if curr_val=='@':
            # if map_[next_loc] == '.':
            # swap the values!!
            if printy:
                print(f" -- 1: {curr_loc}, {map_[next_loc]}  - {next_loc},{map_[next_loc]}")

            # next_val = map_[next_loc]
            # map_[next_loc] = curr_val
            # map_[curr_loc] = next_val
            # if printy:
            #     print(f'swapping {curr_val} for {next_val}') 
        

            if not check_box_alignments(map_):
                map_ = map_orig.copy()
                # pass
            # swap the values!!
            # print(f"just overwrote mat {next_loc}, {map_[next_loc]}")
            # map_ = make_a_move_part2_2(curr_loc, direction, map_)
            # print_map(map_copy)
            # assert map_[next_loc]=='.', "at this point the path should be clear for the robot to move!!"
            # map_ = make_a_move_part2_2(curr_loc, direction, map_)

            
        # if map_[next_loc]=='.':
        #     map_[next_loc] = curr_val
        #     map_[curr_loc] = next_val
        #     print(f'last ditch: swapping {curr_val} for {next_val}  ----locs:  {curr_loc} to {next_loc}')

    return map_

test_txt = ['#######',
 '#.....#',
 '#..O..#',
 '#.O@O.#',
 '#..O..#',
 '#..O..#',
 '#.....#',
 '#######',
 '',
 '<']

# map_, moves = process_input_part2(test_txt)

map_,moves = process_input("""##############
##..........##
##....[]....##
##..[]@.[]..##
##....[]....##
##...[][]...##
##..........##
##......#...##
##############""".splitlines())
print_map(map_)
curr_loc = list(zip(*np.where(map_=='@')))[0] 

map_ = make_a_move_part2_2(list(zip(*np.where(map_=='@')))[0] , 'v', map_)
print(1)
print_map(map_)

# %%
