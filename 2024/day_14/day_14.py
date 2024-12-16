#%%
daynum = "14"
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

import re
def process_input(txt):
    p=[]
    v = []
    for t in txt:
        tmp = [int(x) for x in re.findall(r'[-\d]+',t)]
        # reverse the order as they're in x,y ratehr than r,c
        p.append(np.array([tmp[1],tmp[0]]))
        v.append(np.array([tmp[3],tmp[2]]))
    return p,v

def wrap_around_bounds(val,minv, maxv):
    if val<minv:
        return val+maxv
    elif val>=maxv:
        return val-maxv
    else:
        return val

p,v = process_input(txt)

R = 103
C = 101
R = 7
C = 11


# # # walk thru example
# p1 = np.array([4,2])
# v1 = np.array([-3,2])
# # position_after_n_seconds(p1,v1,5,R,C)
# for i in range(5):
#     p1 = np.array([4,2])
#     v1 = np.array([-3,2])
#     print(position_after_n_seconds(p1,v1,i,7,11))

def position_after_n_seconds(p,v,n,R,C):
    px = p
    for i in range(n):
        px= px + v
        px[0] = wrap_around_bounds(px[0],0, R)
        px[1] = wrap_around_bounds(px[1],0, C)
    return px


    # s = [p1]
    # for i in range(3):
    #     tmp = s[-1]+v1
    #     tmp[0] = wrap_around_bounds(tmp[0],0, R-1)
    #     tmp[1] = wrap_around_bounds(tmp[1],0, C-1)
        
        
    #     print(f"{s[-1]+v1} | {tmp}")
    #     s.append(tmp)

def get_quadrants(p, R, C):
    qr = int((R-1)/2)
    qc = int((C-1)/2)

    q1 = np.sum([1 for x in p if x[0]<qr and x[1]<qc ])
    q2 = np.sum([1 for x in p if x[0]<qr and x[1]>qc ])
    q3 = np.sum([1 for x in p if x[0]>qr and x[1]<qc ])
    q4 = np.sum([1 for x in p if x[0]>qr and x[1]>qc ])
    return q1,q2,q3,q4

def intersection(list1, list2):
    logger.debug(f"list1={list1}")
    logger.debug(f"list2={list2}")
    return list(set([tuple(x) for x in list1]) & set([tuple(y) for y in list2]))


# returns 1 if symmetry: horiz and vert  
def get_symmetry_score(p, R, C):
    hr = int((R-1)/2) # half row
    hc = int((C-1)/2) # half col

    # [4,5,6] -> [0,1,2] -> [2,1,0]
    #         -3        3-x)
    # tests:
    # [(x[0],5-(x[1]-5)) for x in [(0,6),(0,7),(0,8),(0,9),(0,10)]]
    # [(x[0],3-(x[1]-3)) for x in [(0,4),(0,5),(0,6)]]

    h1 = [x for x in p if x[1]<hc ] # top horizontal half
    h2 = [(x[0],hc-(x[1]-hc)) for x in p if x[1]>hc ] # bottom 

    h_score = len(intersection(h1,h2))

    v1 = [x for x in p if x[0]<hr ] # top vertical half
    v2 = [(hr-(x[0]-hr),x[1]) for x in p if x[0]>hr ]
    v_score = len(intersection(v1,v2))
    return h_score, v_score, len(h1+h2), len(v1+v2)

def get_score(p, R, C):
    q1,q2,q3,q4 = get_quadrants(p, R, C)
    return q1*q2*q3*q4
# %%
logger.setLevel(logging.INFO)
def part1(txt,R,C):
    p_in,v_in = process_input(txt)
    new_p =[]
    for i in range(len(p_in)):
        new_p.append(position_after_n_seconds(p_in[i],v_in[i],99,R,C))
    # new_p
    return get_score(new_p, R, C)    

print(f"Part 1 (test): {part1(test_txt,7,11)}")
print(f"Part 1: {part1(input_txt,103,101)}")

# %%
def part2(txt):
    # working hypothesis is that a pic of a christmas tree 
    #  will have some left-right or up-down symmetry 
    p_in,v_in = process_input(input_txt)
    R = 103
    C = 101
    scores = []
    syms  = []
    old_p = p_in
    p_vec=[]
    for s in tqdm(range(10000)):
        new_p =[]
        for i in range(len(p_in)):
            new_p.append(position_after_n_seconds(old_p[i],v_in[i],1,R,C))
        h1,v1,h_denom,v_denom= get_symmetry_score(new_p, R, C)
        syms.append([h1,v1]) 

        if h1>50 or v1>50:
            scores.append([s,h1,v1,new_p])
            
            tmat = np.zeros([R,C])
            for n in new_p:
                tmat[n[0],n[1]] = 1
            fig,ax = plt.subplots()
            ax.imshow(tmat, extent=[0, R-1, 0, C-1])
            plt.title(s+1)
            plt.savefig(f'figs/part_2_{s+1}.png')
            plt.close()
            return s+1
            # logger.info((s,h1,v1))
        old_p = new_p

# print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%

# graveyard
if 0:

    p_in,v_in = process_input(input_txt)
    R = 103
    C = 101
    scores = []
    syms  = []
    old_p = p_in
    p_vec=[]
    for s in tqdm(range(10000)):
        new_p =[]
        for i in range(len(p_in)):
            new_p.append(position_after_n_seconds(old_p[i],v_in[i],1,R,C))
        h1,v1,h_denom,v_denom= get_symmetry_score(new_p, R, C)
        syms.append([h1,v1]) 

        if h1>50 or v1>50:
            scores.append([s,h1,v1,new_p])
            
            tmat = np.zeros([R,C])
            for n in new_p:
                tmat[n[0],n[1]] = 1
            fig,ax = plt.subplots()
            ax.imshow(tmat, extent=[0, R-1, 0, C-1])
            plt.title(s+1)
            plt.savefig(f'figs/{s+1}.png')
            plt.close()
            break
            # logger.info((s,h1,v1))
        old_p = new_p



    #   %%
    print(p_vec[3433][:3])
    new_p = p_vec[3433][3]


    tmat = np.zeros([R,C])
    for n in new_p:
        tmat[n[0],n[1]] = 1
    fig,ax = plt.subplots()
    ax.imshow(tmat, extent=[0, R-1, 0, C-1])
    plt.title(p_vec[3433][0])



    #%%
    s = 3437*2+1

    # plot

    tmat = np.zeros([R,C])

    new_p =[]
    for i in range(len(p_in)):
        new_p.append(position_after_n_seconds(p_in[i],v_in[i],s,R,C))

    for n in new_p:
        tmat[n[0],n[1]] = 1
    fig,ax = plt.subplots()
    ax.imshow(tmat, extent=[0, R-1, 0, C-1])
    plt.title(s)
    plt.show()


            
    # 200, 279
    # %%
    import matplotlib.pyplot as plt
    ss = np.array(scores)
    plt.plot(ss[:,0]-ss[:,1])
    plt.plot(ss[:,0]-ss[:,1])

    # %%




    # %%
    np.where(np.abs(ss[:,0]-ss[:,1])==0)
    # %%
    np.where(np.abs(ss[:,2]-ss[:,3])==0)

    # %%
