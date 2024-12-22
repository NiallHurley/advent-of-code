#%%
daynum = "11"
import numpy as np
from tqdm.autonotebook import tqdm

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]



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

#%%

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits,
#   it is replaced by two stones. The left half of the digits are engraved on the new left stone, 
#   and the right half of the digits are engraved on the new right stone. 
#   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

def flatten_list(l):
    return [item for row in l for item in row]

def apply_rules(stone):
    if stone =='0':
        return '1'
    
    elif len(stone)%2 ==0:
        m = int(len(stone)/2)
        return [str(int(stone[:m])),str(int(stone[m:]))]
    
    else:
        return str(int(stone)*2024)
    
def blink(stones):
    if not isinstance(stones,list):
        stones = [stones]
    stones_new=[]
    for s in stones:
        tmp = apply_rules(s)
        if isinstance(tmp, list):
            [stones_new.append(l) for l in tmp]
        else:
            stones_new.append(tmp) 
    return stones_new

txt = '0 1 10 99 999'
stones= txt.split()
blink(stones)

txt = '125 17'
stones= txt.split()
for i in range(25):
    stones = blink(stones)
    # print(stones)
len(stones)

txt = '125 17'
stones= txt.split()
retval = 0
for s in stones:
    for i in range(5):
        # print(s)
        s = blink(s)
    # print(s)
    retval += len(s)
retval

#%% more helper functions

def combine_new_and_old_dicts(x,y):
    # where x = new and y = old
    for k in set(x):
        x[k] =  x[k] *y.get(k,1)
    return x

def combine_dicts_sum_values(x,y):
    return {k: x.get(k,0)+ y.get(k,0) for k in set(x) | set(y)}

def list_to_dict(lst):
    dict1 = {}
    for l in lst:
        dict1[l]=dict1.get(l,0)+1
    return dict1
import functools

@functools.cache
def blink_n_times(stones,n=1):
    for i in range(n):
        stones = blink(stones)
    return stones

def blink_n_times_using_dicts(stones_dict,n=1):
    # process key by ky
    out_dict = {}
    for sk in stones_dict:
        nkeytimes = stones_dict[sk]
        # do n blinks with the key, then mulitply the output by the key's value 
        #   i.e. there are 10*'0'... so we should blink '0' n times... and then we multiple output by 10
        tmp = list_to_dict(blink_n_times(sk,n))
        for k in tmp:
            tmp[k] = tmp[k]*nkeytimes
        out_dict = combine_dicts_sum_values(out_dict,tmp)
    return out_dict

# unit test for dict methods
stones= ['10', '251']

tmp = []
for s in stones:
    tmp.extend(blink_n_times(s,25))
# list_to_dict(tmp)

assert blink_n_times_using_dicts(list_to_dict(stones),n=25) == list_to_dict(tmp)



# %%
def part1_alt(txt):
    stones= txt[0].split()
    for i in range(25):
        stones = blink(stones)
        # print(stones) 
    return len(stones)   

def part1(txt):
    stones= txt[0].split()
    retval = 0
    for s in stones:
        s=[s]
        for i in range(25):
            s = blink(s)
        retval += len(s)
    return retval 

print(f"Part 1 alt (test): {part1_alt(test_txt)}")
print(f"Part 1 alt: {part1_alt(input_txt)}")
print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
# this needs caching or memoisation or whatever


logger.setLevel(logging.WARN)
def part2(txt):
    stones= txt[0].split()
    
    p = blink_n_times_using_dicts(list_to_dict(stones),n=5) # this does 5 blinks
    for i in range(14):  #<--- need to do another 14 loops of 5 blinks... with caching this is a breeze!
        stones = p
        p = blink_n_times_using_dicts(stones,n=5)
        
    # print(np.sum(list(p.values())))
    return np.sum(list(p.values()))
        
    # print(stones_out)
    return np.sum(list(stones_out.values())) 

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# 232454623677743


# %%
# # # # # # # # # # # # # # # # # 
#  Graveyard

if 0:


    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    def non_intersecting(lst1,lst2):
        return set(lst1).symmetric_difference(lst2)

    stones= '125 17'.split()
    for i in range(5):
        stones = blink(stones)
        print(stones) 
    len(stones)  


    stones= '125 17'.split()
    for s in stones:
        for i in range(5):
            s = blink(s)
        print(stones) 
    len(stones)  

    # def part1_alt_messing(txt):
    dict1 = {}
    stones= '125 17'.split()
    for i in range(3):
        stones = blink(stones)
        # uvals = np.unique(stones)
        new_dict = dict((i, stones.count(i)) for i in stones)

        for k in dict1:
            if k in new_dict:
                new_dict[k] *= dict1[k]
        dict1 = new_dict


        # for u in uvals:
        #     num_of_u = len(np.where(u==stones))
        #     if u not in dict1:
        #         dict1[u] = num_of_u
        #     else:
        #         dict1[u] = num_of_u*dict1[u]
        #     # dict1[u] = dict1.get(u,0)+dict1.get(u,0)*len(np.where(u==stones))
        # for k in non_intersecting(dict1.keys(),uvals):
        #     del dict1[k]
        stones = uvals    

    np.sum(list(dict1.values()))
            # print(stones) 
        # return len(stones)  

    # part1_alt_messing('125 17')
    # %%
    a = ["a", "b", "a", "b", "c", "d", "e", "a"]

    result = dict((i, a.count(i)) for i in a)

    print(result)


    # %%

    # %%

    stones= list_to_dict('125 17'.split())
    logger.setLevel(logging.WARN)
    stones_in = stones

    for i in range(75):
        
        stones_out = {}
        for s in stones_in:
            logger.debug(f"s = {s}")
            s_out = blink(s)
            logger.debug(f"s out = {s_out}")
            s_out = s_out*stones_in.get(s,1)
            # stones_out = combine_dicts_sum_values(list_to_dict(s_out), stones_out)
            stones_out = combine_dicts_sum_values(stones_out,list_to_dict(s_out))
        # stones_out = combine_new_and_old_dicts(stones_out,stones_in)
        stones_in = stones_out
        logger.info(stones_out)
        logger.info(f"len = {np.sum(list(stones_out.values()))}")
            
    # print(stones_out)
    np.sum(list(stones_out.values())) 

    # %%
    print('correct')
    stones= '125 17'.split()
    for i in range(6):
        stones = blink(stones)
        print(f"{len(stones)}: {stones}") 
    len(stones)  
    # %%
    #  =========================  ***************  ==================================================
    print('correct')
    stones= ['0']
    for i in range(25):
        stones = blink(stones)
        # print(f"{len(stones)}: {stones}") 
    cache_['0'] = combine_dicts_sum_values({},list_to_dict(stones))
    len(stones)  



    # %%



    # %%
    z1 = blink_n_times_using_dicts(list_to_dict(['0']),n=2)

    p ={}

    for z in z1:
        p = combine_dicts_sum_values(p,blink_n_times_using_dicts(list_to_dict(z),n=1))
    p

    # %%
    # this does n=5 5 times... and gets the same answer to the n=25 part 1

    def part2_alt_dicts_test():
        stones= ['125', '17']
        p = blink_n_times_using_dicts(list_to_dict(stones),n=5)
        for i in range(14):
            stones = p
            p = blink_n_times_using_dicts(stones,n=5)
            
        print(np.sum(list(p.values())))
        return np.sum(list(p.values()))

    def part2_alt_dicts():
        stones= '0 27 5409930 828979 4471 3 68524 170'.split()
        p = blink_n_times_using_dicts(list_to_dict(stones),n=5)
        for i in range(14):
            stones = p
            p = blink_n_times_using_dicts(stones,n=5)
            
        print(np.sum(list(p.values())))
        return np.sum(list(p.values()))


    # %%
    import timeit
    timeit.timeit(part2_alt_dicts_test,number = 1)
    # 0.0034774999985529575
    # %%
    timeit.timeit(part2_alt_dicts,number = 1)

    # %%
