#%%
daynum = "08"
import numpy as np
from tqdm.autonotebook import tqdm

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

def process_input(txt):
    tmp = []
    for line in txt:
        tmp.append([c for c in line])
    return(np.array(tmp))





# %%
def part1(txt):

    mat = process_input(txt)
    R,C = mat.shape
    uvals = np.unique(mat)

    u_dict = {} # unique list of antennas and locs
    antinodes = []
    for u in uvals:
        if u != '.':
            u_dict[u] = list(zip(*np.array(np.where(mat==u))))

            for p in get_all_pairs(u_dict[u]):
                d = tuple_diff(p[0],p[1])
                a1 = tuple_sum(p[0],d)
                a2 = tuple_diff(p[1],d)
                
                if 0<=a1[0]<R and 0<=a1[1]<C:
                    antinodes.append(a1)
                if 0<=a2[0]<R and 0<=a2[1]<C:
                    antinodes.append(a2)
    return len(set(antinodes))    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    mat = process_input(txt)
    R,C = mat.shape
    uvals = np.unique(mat)

    u_dict = {} # unique list of antennas and locs
    antinodes = []
    for u in uvals:
        if u != '.':
            u_dict[u] = list(zip(*np.array(np.where(mat==u))))

            for p in get_all_pairs(u_dict[u]):
                d = tuple_diff(p[0],p[1])

                a1 = tuple_sum(p[0],d)
                while 0<=a1[0]<R and 0<=a1[1]<C:
                    antinodes.append(a1)
                    a1 = tuple_sum(a1,d)

                # could be between them
                a1 = tuple_diff(p[0],d)
                while 0<=a1[0]<R and 0<=a1[1]<C:
                    antinodes.append(a1)
                    a1 = tuple_diff(a1,d)

                a2 = tuple_diff(p[1],d)
                while 0<=a2[0]<R and 0<=a2[1]<C:
                    antinodes.append(a2)
                    a2 = tuple_diff(a2,d)

                # could be between them
                a2 = tuple_sum(p[1],d)
                while 0<=a2[0]<R and 0<=a2[1]<C:
                    antinodes.append(a2)
                    a2 = tuple_sum(a2,d)
    return (len(set(antinodes)))

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%



# %%
