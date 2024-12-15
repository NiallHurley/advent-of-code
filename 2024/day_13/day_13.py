#%%
daynum = "13"
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
    As = []
    Bs = []
    Xs = []
    for t in txt:
        if len(t)==0:
            pass
        elif t[:8]=='Button A':
            As.append([int(x) for x in re.findall(r'[\d]+',t)]) 
        elif t[:8]=='Button B':
            Bs.append([int(x) for x in re.findall(r'[\d]+',t)]) 
        else: # t[0]=='P':
            Xs.append([int(x) for x in re.findall(r'[\d]+',t)]) 

    Amats = [*zip(As,Bs)]
    bmat = Xs

    return Amats,bmat

def linsolve(A,b):
    m,n = A
    a1,a2 = m
    b1,b2 = n
    c1,c2 = b
    x = (c1*b2-b1*c2)/(a1*b2-a2*b1)
    y = (a1*c2-c1*a2)/(a1*b2-a2*b1)
    return x,y




# %%
logger.setLevel(logging.INFO)
def part1(txt):
    Amats,bmat = process_input(txt)
    result =0
    for i in range(len(Amats)):
        x,y = linsolve(Amats[i],bmat[i])
        if x.is_integer() and y.is_integer():
            result += 3*x+y
    return result   

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    Amats,bmat = process_input(txt)
    result =0
    for i in range(len(Amats)):
        new_bmat = [x+10000000000000 for x in bmat[i]]
        x,y = linsolve(Amats[i],new_bmat)
        if x.is_integer() and y.is_integer():
            result += 3*x+y
    return result  

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
