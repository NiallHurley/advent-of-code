#%%
daynum = "02"
import numpy as np

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%

# %%
def part1(txt):
    keep = [ 0]*len(txt)
    # arr= np.array([x.split() for x in txt]).astype(np.int32)
    # arrdiff = np.diff(arr,1)
    for i,rowtxt in enumerate(txt):
        row = np.array(rowtxt.split()).astype(np.int32)
        rowdiff = np.diff(row,1)
        condition1 = all(np.abs(rowdiff)<=3)
        condition2 =  all(np.abs(rowdiff)>=1)
        condition3 =   (all(np.sign(rowdiff)==-1) or all(np.sign(rowdiff)==1))
        # print(f"{i}: [{condition1}, {condition2}, {condition3}],|{np.sum(np.sign(row)),len(row)}| {rowtxt}")
        if condition1 and condition2 and condition3:
            keep[i]=1



    return  np.sum(keep)   

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%

printy = False

def all_1(arr_row):
    return(np.sum(arr_row) >= len(arr_row)-1)

def testrow(row):
    rowdiff = np.diff(row,1)
    condition1 = all(np.abs(rowdiff)<=3)
    condition2 =  all(np.abs(rowdiff)>=1)
    condition3 =   (all(np.sign(rowdiff)==-1) or all(np.sign(rowdiff)==1))
    if printy:
        print(f" [{condition1}, {condition2}, {condition3}],|{np.sum(np.sign(row)),len(row)}| {row}")
    return(condition1 and condition2 and condition3)

def part2(txt):

    keep = [ 0]*len(txt)
    for i,rowtxt in enumerate(txt):
        if printy:
            print(f"{i}:")
        row = np.array(rowtxt.split()).astype(np.int32)
        if testrow(row):
            keep[i]=1
            if printy:
                print(keep[i])
        else:
            for j in range(len(row)):
                row_1 = list(row[0:j]) + list(row[j+1:])
                
                if testrow(row_1):
                    if printy:
                        print(f"{keep[j]} - reached")
                    keep[i]=1
                    break
    
    return np.sum(keep)


print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")
# %%
