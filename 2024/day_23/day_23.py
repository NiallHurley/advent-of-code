#%%
daynum = "23"
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

def get_all_triples(list_):
    return list(itertools.combinations(list_, 3))
# %%
logger.setLevel(logging.INFO)
def part1(txt):
    tmp = []
    for t in txt:
        tmp.append(t.split('-'))

    # [item for sublist in tmp for item in sublist]

    # create dict of all nodes and connections
    d = {}
    for l in tmp:
        d[l[0]]= d.get(l[0],set()).union([l[1]])
        d[l[1]]= d.get(l[1],set()).union([l[0]]) 

    rec = []
    for n in d:
        vals1 = d[n]
        for v in vals1:
            vals2 = d[v]
            for v2 in vals2:
                vals3 = d[v2]
                if n in vals3 and n!=v and v!=v2 and v2!=v:
                    rec.append([n,v,v2])
    b = []
    for a in rec:
        a = list(set(a))
        a.sort()
        b.append(tuple(a))
    b = set(b)
    return np.sum([1 for r in b if 't' in r[0][0]+r[1][0]+r[2][0]])

    # # for each dict look at pairs with intersections of len==2
    # rec = set()
    # for n in d:
    #     d1 = d[n].union([n])
    #     for n2 in d:
    #         if n2!=n and n in d[n2]: 
    #             d2 = d[n2].union([n2])
    #             ints = list(d2.intersection(d1))
    #             if len(ints)>3:
    #                 print('boom!')
                
    #                 a_list = get_all_triples(ints)
    #                 for a in a_list:
    #                     a = list(set(a))
    #                     a.sort()
    #                     print(f"a: {a}")
    #                     rec.add(tuple(a)) # set keeps things in order and removes dupes :D
    #             elif len(ints)==3:
    #                 a = list(set(ints))
    #                 a.sort()
    #                 rec.add(tuple(a)) # set keeps things in order and removes dupes :D

    # return len(set([tuple(r) for r in rec if len(r)==3])) 

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    tmp = []
    for t in txt:
        tmp.append(t.split('-'))

    from networkx.algorithms import clique
    import networkx as nx
    G = nx.Graph()
    edges_fig_4 = tmp
    G.add_edges_from(edges_fig_4)
    cliques = clique.find_cliques(G)
    maxlen=0
    for index, clq in enumerate(cliques):
        # print( f'Maximal Clique {index+1} ', clq)
        if len(clq)>maxlen:
            maxlen = len(clq)
    
    max_clqs = []
    for index, clq in enumerate(clique.find_cliques(G)):
        # print( f'Maximal Clique {index+1} ', clq)
        if len(clq)==maxlen:
            clq.sort()
            max_clqs.append(clq)

    return ','.join(max_clqs[0])
   

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%



