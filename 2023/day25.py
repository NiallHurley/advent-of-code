#%%
daynum = 25
import numpy as np

with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

# %%
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.minimum_cut.html
   
import networkx as nx
import itertools

#%%

nodelist = set()
G = nx.Graph()
for l in txt:
    tmp = l.split(': ')
    nfrom = tmp[0]
    nodelist.add(nfrom)
    for nto in tmp[1].split(' '):
        G.add_edge(nfrom, nto, capacity=1.0)
        nodelist.add(nto)

minc = []
minp = []

for i1, n1 in enumerate(nodelist):
    for i2, n2 in enumerate(nodelist):
        if i2>i1:
            cut_value, partition = nx.minimum_cut(G, n1, n2)
            if minc == []:
                minc = cut_value
                minp = partition
            elif cut_value<minc:
                minc = cut_value
                minp = partition
print(len(minp[0])*len(minp[1]),minc, minp)
# %%
def part1(txt):
    edgelist = []
    nodelist = set()
    for l in txt:
      tmp = l.split(': ')
      nfrom = tmp[0]
      nodelist.add(nfrom)
      for nto in tmp[1].split(' '):
        edgelist.append([ nfrom, nto])
        nodelist.add(nfrom)
    G = nx.from_edgelist(edgelist) 
    minc = []
    minp = []
    for i1, n1 in enumerate(nodelist):
        for i2, n2 in enumerate(nodelist):
            if i2>i1:
                try:
                    cut_value, partition = nx.minimum_cut(G, n1, n2) 
                    if minc == []:
                        minc = cut_value
                        minp = partition
                    elif cut_value<minc:
                        minc = cut_value
                        minp = partition
                except:
                    pass
    return len(minp[0])*len(minp[1])

print(f"Part 1 (test): {part1(test_txt)}")
# print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
   return None

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
