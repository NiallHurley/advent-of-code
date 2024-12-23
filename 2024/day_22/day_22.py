#%%
daynum = "22"
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
def combine_dicts_sum_values(x,y):
    return {k: x.get(k,0)+ y.get(k,0) for k in set(x) | set(y)}

def gen_sec(val):
    # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    a = val
    b = np.mod(a*64 ^ a,16777216) 
    c = np.mod(int(b/32) ^ b,16777216) 
    d = np.mod(c*2048 ^ c,16777216) 
    return(d)

def gen_sec_repeat(val, num_iters=2000):
    for i in range(num_iters):
        val = gen_sec(val)
    return val

def part2_prices(val,num_iters=2000):
    # same as above but remember the last digit at each iter
    prices = [np.mod(val,10)]
    # prices = []
    seqs = {}
    for i in range(num_iters):
        val = gen_sec(val)
        price = np.mod(val,10)
        prices.append(price)
        key_ = tuple(np.diff(prices[i+1-5:i+1]))
        logger.debug(f"\n ====  {i} ====")
        logger.debug(f"{len(prices)}, {i}")
        logger.debug(f"{price} | {prices[i+1-5:i+1]} | {key_}")
   
        if i>=4:        
            if len(key_)==4 and key_ not in seqs:
                # seqs[key_] =  prices[i] # take first value
                seqs[key_] = seqs.get(key_,0) + prices[i] # if each seller can sell multiple times

    return prices,seqs

tmp,seq = part2_prices(123,num_iters=10)
tmp,seq




# %%
logger.setLevel(logging.INFO)
def part1(txt):
    vals = [int(t) for t in txt]

    ans = 0
    for val in vals:
        ans += gen_sec_repeat(val, num_iters=2000)
    return ans    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    vals = [int(t) for t in txt]

    overall_seqs = {}
    for val in vals:
        tmp,seq = part2_prices(val,num_iters=2001) # <--- off by one !! ffs... last element wasn't getting checked :doh:
        overall_seqs = combine_dicts_sum_valuess(overall_seqs,seq)
    return np.max(list(overall_seqs.values()))    


print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%

