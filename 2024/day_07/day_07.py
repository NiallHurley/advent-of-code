#%%
daynum = "07"
import numpy as np
from tqdm.autonotebook import tqdm

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]

#%%
def process_input(txt):
    results = []
    nums = []
    for l in txt:
        t =  l.split(':')

        results.append(int(t[0]))
        nums.append([int(x) for x in t[1].split()])

    return results, nums

# part 1 brute force... try all operator options until 1 works
def process_line(r, nums):
    numops = len(nums)-1
    if len(nums)==1:
        return r==nums[0]
    
    for i in range(2**numops):
        # iterate thru binary numbers using 0 for + and 1 for *
        opselection = bin(i)[2:].zfill(numops)
        running_total = nums[0]
        # print(f"{running_total}, {nums[0]}")
        for i,o in enumerate(opselection):
            if o =='0':
                # sum
                running_total +=nums[i+1]
                # print(f"{running_total}, {nums[i+1]}, +")
            else:
                running_total *= nums[i+1]
                # print(f"{running_total}, {nums[i+1]}, *")
        # print(running_total, opselection)
    
        if running_total==r:
            return True # break if we find a winner
        else:
            pass
    return False

# part 2 brute force

# part 1 brute force... try all operator options until 1 works
def process_line_part2(r, nums):
    numops = len(nums)-1
    if len(nums)==1:
        return r==nums[0]
    
    for i in range(3**numops):
        # iterate thru binary numbers using 0 for + and 1 for *
        opselection = np.base_repr(i, base=3).zfill(numops)
        running_total = nums[0]
        # print(f"{running_total}, {nums[0]}")
        for i,o in enumerate(opselection):
            if o =='0':
                # sum
                running_total +=nums[i+1]
                # print(f"{running_total}, {nums[i+1]}, +")
            elif o=='1':
                running_total *= nums[i+1]
            else: # o=='2':
                ll = running_total
                running_total = concat_op(running_total, nums[i+1])
                # print(f"{running_total}, {ll} ||  {nums[i+1]} ")
            
            if running_total>r:
                # break if we've already gone too big
                break
        
    
        if running_total==r:
            if '2' in (running_total, opselection):
                print(r)
            return True # break if we find a winner
        else:
            pass
    return False
# process_line_part2(r, nums)

def concat_op(n1 ,n2):
    return int(''.join([str(n) for n in [n1,n2]]))
# 25.3 µs ± 2.65 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

def concat_op2(n1 ,n2):
    return 10**np.ceil(np.log10(n2))+n1
# 86.3 µs ± 276 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)    

# %%
def part1(txt):
    results,nums_list = process_input(txt)

    ans = []
    for i,r in tqdm(enumerate(results),total=len(results)):
        if process_line(r,nums_list[i]):
            ans.append(r)


    return np.sum(ans)    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    results,nums_list = process_input(txt)

    ans = []
    for i,r in tqdm(enumerate(results),total=len(results)):
        # print(i)
        if process_line_part2(r,nums_list[i]):
            ans.append(r)

    print(ans)
    return np.sum(ans)  

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# 150500184914933 is too high
# %%


# # # # # # # # # # # # # # # # # # # # # # # # # # # 

#    GRAVEYARD

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
if 0:
    from collections import deque

    q = deque(nums[1])



    running_total = -1

    def f2(q,running_total,operator):
        while q:
            # popleft coord
            n = q.popleft()
            running_total = process_q_element(running_total,n,operator)



    # def total_run(q,running_total,operator,r):
    #     while q:
    #         n = q.popleft()
    #         if operator == '':
    #             # first call
    #             running_total = n
    #         elif operator == '+':
    #             running_total += n
    #         else:
    #             running_total *= n

    #         return running_total

    def process_q_element(running_total,q_elem,operator):
        if operator == '':
            # first call
            running_total = q_elem
        elif operator == '+':
            running_total += q_elem
        else:
            running_total *= q_elem
        return running_total


    def f1_(target, running_total, nums, operator):
        nextnum = nums.popleft
        if len(nums)==1:
            if operator == '+':
                return running_total + nums[0] == target
            else:
                return running_total * nums[0] == target
        else:
            nextnum = nums[0]
            if operator = '+':
                running_total += nums[0] 
            else:
                running_total *= nums[0] 







    # %%


    # make all concat possibilities... 

    s = ['a','b','c']
    ','.join(s)

    # %%

    # drop letter at index ind from str
    def drop_ind_from_str(str, ind):
        return str[:ind]+str[ind+1:]




    # %%


    # %%



    # part 2 helper... change list to str.. then use binary to identify the keep or leave the ','
    def process_line_gaps(r, nums):
        numstr = ','.join([str(n) for n in nums])
        gap_locs = [i for i, c in enumerate(numstr) if c == ',']
        numgaps = len(nums)-1

        for i in range(2**(numgaps)):
            # print(f"plg: {i}: {nums}")
            # iterate thru binary numbers to keep or remove the ','
            gappselection = bin(i)[2:].zfill(numgaps)
            numstr_local = numstr

            gap_inds_to_remove = [j for j, x in enumerate(gappselection) if x=='1']
            comma_locs = [j for j,n in enumerate(numstr) if n==',']
            comma_inds_to_remove = [x for j,x in enumerate(comma_locs) if j in gap_inds_to_remove]

            for c in comma_inds_to_remove[::-1]:
                numstr_local = drop_ind_from_str(numstr_local,c)
            numstr_with_gaps_removed = numstr_local


            # print(f"{bin(i)[2:].zfill(numgaps)} | {gaps_to_remove} | {numgaps} | {i} ")

            # numstr_with_gaps_removed = ''.join([n for j,n in enumerate(numstr) if j not in gaps_to_remove])
            # print(f"numstr: {numstr_with_gaps_removed}  {[n for j,n in enumerate(numstr) if j not in gaps_to_remove]} | {numstr} | {gaps_to_remove}")
            
            num_with_gaps_removed = [int(n) for n in numstr_with_gaps_removed.split(',') ]
            # print(num_with_gaps_removed)

            # now try the part 1 brute force on the new nums :) 
            # (also check that no new digits exceed the result value r)
            if all([n<=r for n in num_with_gaps_removed]):
                print(f"{i}: {r} : {num_with_gaps_removed}  ready to process...")
                if process_line(r, num_with_gaps_removed):
                    return True
        return False
    process_line_gaps(r, nums)