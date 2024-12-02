#%%
daynum = "01"
import numpy as np

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%

# def intersection(list1, list2):
#     list3 = [value for value in list1 if value in list2]
#     return list3

def intersection(list1, list2):
    return list(set(list1) & set(list2))



# %%
def part1(txt):
    arr = np.array([x.split() for x in txt]).astype(np.int32)
    freqs1={}
    for num in arr[:,0]:
        freqs1[num] = freqs1.get(num, 0) +1

    freqs2={}
    for num in arr[:,1]:
        freqs2[num] = freqs2.get(num, 0) +1

    outlist = []
    for x in intersection(arr[:,0],arr[:,1]):
        outlist.append(x*freqs1[x]*freqs2[x])

    return np.sum(outlist)

    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    return None

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
