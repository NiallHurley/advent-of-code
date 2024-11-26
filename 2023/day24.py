#%%
daynum = 24

import numpy as np

with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

# %%

# Plan of action... 

# part 1 ignores the z values... 
# eq of line is y=mx+c, need compute m and c for each line
# then the intesection is given by 

# x = (c2-c1)/(m1-m2)
# y = (m2*c1-m1*c2)/(m2-m1)

# and there's a direction component... are we getting towards the intersection or further away
# (can just look at where the x-intersection is relative to the starting point and the velocity)
  

# %%

def part_1_helper(txt,llim=7,ulim=27):

    a =    [x.split('@') for x in txt]
    coords = []
    vels = []
    for y in a:
        coords.append(tuple([float(x) for x in y[0].split(',')]))
        vels.append(tuple([float(x) for x in y[1].split(',')]))

    ms = [vel[1]/vel[0] for vel in vels]
    cs = []
    for i in range(len(coords)):
        coord = coords[i]
        # c = y-mx
        cs.append(coord[1] - ms[i]*coord[0])

    def find_intersec(m1,c1,m2,c2):
        if m2-m1 == 0:
            return((np.nan,np.nan))
        else:
            intx = (c1-c2)/(m2-m1)
            inty = (m2*c1-m1*c2)/(m2-m1)
            return((intx,inty))
    
    def validate_intesection_in_future(coord_,vel_,intersec_,llim,ulim):
        valid = True
        # check for nan
        valid = not(np.isnan(intersec_[0]))
        valid = valid and llim<intersec_[0]<ulim and llim<intersec_[1]<ulim
        valid = valid and np.sign(intersec_[0]-coord_[0])==np.sign(vel_[0])
        return(valid)

    mc_pairs = [x for x in zip(ms,cs)]

    intersec_list =[]
    for i,mc1 in enumerate(mc_pairs):
        ci = coords[i]
        vi = vels[i]
        for i2,mc2 in enumerate(mc_pairs):
            ci2 = coords[i2]
            vi2 = vels[i2]
            if i2>i:
                intersec_ = find_intersec(mc1[0],mc1[1],mc2[0],mc2[1])
                if validate_intesection_in_future(ci,vi,intersec_,llim,ulim) and \
                    validate_intesection_in_future(ci2,vi2,intersec_,llim,ulim) :                    
                    # print(f"{coords[i]} intersects with {coords[i2]} at {intersec_}... mcpairs: {vels[i]}, {vels[i2]}")
                    intersec_list.append(intersec_)
    
    return(len(intersec_list))





# %%
def part1(txt,llim,ulim):
   return (part_1_helper(txt,llim,ulim))

print(f"Part 1 (test): {part1(test_txt,7,27)}")
print(f"Part 1: {part1(input_txt,200000000000000,400000000000000)}")


#%%
def tuplediff(v1,v2):
    return(np.array(v1)-np.array(v2))

def tuplecross(v1,v2):
    return(np.cross(np.array(v1),np.array(v2)))

def tupledot(v1,v2):
    return(np.dot(np.array(v1),np.array(v2)))


# %%
def part2(txt):
    a = [x.split('@') for x in txt]
    coords = []
    vels = []
    for y in a:
        coords.append(tuple([float(x) for x in y[0].split(',')]))
        vels.append(tuple([float(x) for x in y[1].split(',')]))
    # rebase relative to vector 0 
   
    p1 = tuplediff(coords[1],coords[0])
    p2 = tuplediff(coords[2],coords[0])
    v1 = tuplediff(vels[1],vels[0])
    v2 = tuplediff(vels[2],vels[0])

    # t1 = -((p1 x p2) * v2) / ((v1 x p2) * v2)
    # t2 = -((p1 x p2) * v1) / ((p1 x v2) * v1)
    t1 = -tupledot(tuplecross(p1,p2),v2)/tupledot(tuplecross(v1,p2),v2)
    t2 = -tupledot(tuplecross(p1,p2),v1)/tupledot(tuplecross(p1,v2),v1)

    # collision point between hailstone 
    c1 = np.array(coords[1]) + t1*np.array(vels[1])
    c2 = np.array(coords[2]) + t2*np.array(vels[2])

    v = (c2-c1)/(t2-t1)
    p = c1-t1*v

    # (t1,t2,v,p)
    return(p.sum())

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
