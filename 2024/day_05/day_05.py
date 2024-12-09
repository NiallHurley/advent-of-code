#%%
daynum = "05"
import numpy as np

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]



#%%

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def non_intersecting(lst1,lst2):
    return len(intersection(lst1,lst2))==0


# t1 = []
# t2=[]
# for l in txt:
#     if '|' in l:
#         t1.append(l)
#     elif len(l)==0:
#         pass
#     else:
#         t2.append(l)

#%%
# after = {}
# before = {}
# for i,l in enumerate(rules):
#     k = l[0]
#     v = l[1]
#     # all values of in list must have every entry in the 'before' list before it
#     if v not in before.keys():
#         before[v] = set([])
#     before[v] = before[v].union([k])

#     if k not in after.keys():
#         after[k] = set([])
#     after[k] = after[k].union([v])
# after

#%%
# cnt = 0
# ans = []
# for t in t2:
#     local_pass = True
#     l = t.split(',')
#     for i in range(len(l)):
#         if i!=0:
#             bef = l[:i]
#         else:
#             bef =[]
#         cur = l[i]
#         if i < len(l)-1:
#             aft = l[i+1:]
#         else: 
#             aft = []
#         # print(f"{bef} - {cur} -  {aft}")
#         # .get(cur,[]) to return empty if key not found

#         ## not this.. we need to ENSURE that all the befores appear befoe... 
#         # if non_intersecting(after.get(cur,[]),bef) and non_intersecting(before.get(cur,[]),aft):
#         #     pass
#         # else:
#         #     local_pass = False
#         #     break

#         # https://docs.python.org/3/library/stdtypes.html#frozenset.issubset
#         # set <= other
#         # Test whether every element in the set is in other.


#         print(f"   {i}- {cur} - {set(before.get(cur,[]))} -- {set(bef)}")
#         # if set(after.get(cur,[]))<=set(aft):
#         if set(before.get(cur,[]))<=set(bef):        
#             pass
#         else:
#             local_pass = False
#             break

        


#     if local_pass:
#         ans.append(int(l[int((len(l)-1)/2)]))
#     cnt+=1
#     print(f"{cnt}: {local_pass}... {ans}")
    
#%%

# #  attempt 2!
# t1 = []
# t2=[]
# for l in txt:
#     if '|' in l:
#         t1.append(l)
#     elif len(l)==0:
#         pass
#     else:
#         t2.append(l)

# rules = [l.split('|') for l in t1] # rules

# cnt=0
# ans = []
# i = 0
# for t in t2:
#     i+=1

#     local_pass = True
#     for r  in rules:
#         if r[0] in t and r[1] in t:
#             print(f"{r} ... {t}... {(t.find(r[1]),t.find(r[0]))}")
#             if t.find(r[1])>t.find(r[0]):
#                 pass
#             else:
#                 local_pass = False
#                 break
       
#     if local_pass:
#         tmp = t.split(',')
#         ans.append(int(tmp[int((len(tmp)/2))]))
#     cnt+=1
#     print(f"{cnt}: {local_pass}... {ans}")

# %%

def process_input(txt):
    t1 = []
    t2=[]
    for l in txt:
        if '|' in l:
            t1.append(l)
        elif len(l)==0:
            pass
        else:
            t2.append(l)

    rules = [l.split('|') for l in t1] # rules
    updates = t2
    rules = [[int(x[0]),int(x[1])] for x in rules]
    updates = [[int(y) for y in x.split(',')] for x in t2]
    return rules,updates

def test_update(rules, update_):
    local_pass = True
    for r  in rules:
        if r[0] in update_ and r[1] in update_:
            # print(f"{r} ... {update_}... {(update_.index(r[1]),update_.index(r[0]))}")
            if update_.index(r[1])>update_.index(r[0]):
                pass
            else:
                return False
    return True


#%%
def part1(txt):
    rules,updates = process_input(txt)

    cnt=0
    ans = []
    i = 0
    for t in updates:
        i+=1
        local_pass = test_update(rules, t)
        if local_pass:
            tmp = t 
            ans.append(int(tmp[int((len(tmp)/2))]))
        cnt+=1
        # print(f"{cnt}: {local_pass}... {ans}")
    return np.sum(ans)    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# 3321 is too low
# %%

def rearrange_to_fit_rules(rules, master_list,maxiter = 10000):
    i = 0
    while not (test_update(rules,master_list)):
        for r  in rules:
            if r[0] in master_list and r[1] in master_list:
                # print(f"{r} ... {update_}... {(update_.index(r[1]),update_.index(r[0]))}")
                if master_list.index(r[1])>master_list.index(r[0]):
                    pass
                else:
                    # print(f"{r} ... {master_list}... {(master_list.index(r[1]),master_list.index(r[0]))}")
                    # move the later one before the other
                    tmp = r[1]
                    master_list.remove(tmp)
                    master_list.insert(r[0],tmp)
                    break
        i+=1
        # if int(i/100)==i/100:
        #     print(i)
        if i>maxiter:
            return master_list,0

    return master_list,1

def swap_to_fit_rules(rules, input_list,maxiter = 10000):
    i = 0
    while not (test_update(rules,input_list)):
        for r  in rules:
            if r[0] in input_list and r[1] in input_list:
                # print(f"{r} ... {update_}... {(update_.index(r[1]),update_.index(r[0]))}")

                r_0_ind = input_list.index(r[0])
                r_1_ind = input_list.index(r[1])

                if r_1_ind>r_0_ind:
                    pass
                else:
                    # print(f"{r} ... {master_list}... {(master_list.index(r[1]),master_list.index(r[0]))}")
                    # move the later one before the other
                    input_list[r_1_ind] = r[0]
                    input_list[r_0_ind] = r[1]
                    break
        i+=1
        # if int(i/100)==i/100:
        #     print(i)
        if i>maxiter:
            return input_list,0

    return input_list,1

#%%


# part 2
rules,updates = process_input(test_txt)


before = {}
for i,l in enumerate(rules):
    k = l[0]
    v = l[1]
    # all values of in list must have every entry in the 'before' list before it
    if v not in before.keys():
        before[v] = set([])
#     before[v] = before[v].union([k])

def process_all_elements(before,k):
    l1 = None
    l = before[k]
    while l!=l1:
        l1 = l
        for v in l:
            go_deeper = False
            tmp = before.get(v,set())
            if len(tmp)>0:
                l.union(tmp)
    return l

before_all = {}
for k in before.keys():
    before_all[k] = process_all_elements(before,k)


cnt=0
ans = []
i = 0
for t in updates:
    i+=1

    local_pass = True
    for r  in rules:
        if r[0] in t and r[1] in t:
            # print(f"{r} ... {t}... {(t.find(r[1]),t.find(r[0]))}")
            if t.index(r[1])>t.index(r[0]):
                pass
            else:
                local_pass = False
                break
    
    if local_pass:
        tmp = t 
        ans.append(int(tmp[int((len(tmp)/2))]))
    else:
        # process part 2
        # 
        pass

    cnt+=1

print(cnt)


#%%
def part2(txt):
    ans = []
    rules,updates = process_input(txt)
    master_list = list(set([x for u in updates for x in u]))
    master_list =  swap_to_fit_rules(rules, master_list)


    keep = []
    broken = []
    fixed = []
    fixed_yn = []
    ans = []
    for t in tqdm(updates):
        if test_update(rules,t):
            pass #keep.append(t)
        else:
            broken.append(t)
            slist,x = swap_to_fit_rules(rules,t,1e7)
            if x==0:
                print('prob!!')
            fixed_yn.append(x)
            fixed.append(slist)
            mid1 = slist[int((len(slist)-1)/2)]
            # print(f"{mid1}  {int((len(slist)-1)/2)} {slist}")
            ans.append(mid1)
    return np.sum(ans) #- part1(txt)


print(f"Part 2 (test): {part2(test_txt)}")
print("   ")
print(f"Part 2: {part2(input_txt)}")

# 5671 is too high
# %%

# graveyard
if 0: 


    list(set([x for u in updates for x in u]))
    master_list = list(set([x for u in updates for x in u]))
    # %%
    # combine successful lists but keep order!!
    keep = []
    broken = []
    for t in updates:
        if test_update(rules,t):
            keep.append(t)
        else:
            broken.append(t)


    a = [96, 58, 87, 28, 31, 12, 81, 91, 14, 25, 38, 82, 73]
    b = [94, 53, 85, 52, 32, 24, 13, 96, 87, 57, 28, 54, 29, 45, 12, 89, 81, 91, 15]

    i=0
    j=0

    inters = intersection(a,b)

    for inst in inters:
        i1 = a.index(inst)
        j1 = a.index(inst)

    # [k[:k.index(96)] for k in keep if 96 in k]


    # find non-intersecting lists... or maybe find lists that intersect only on the first val?

    lst = []
    for i,si in enumerate(keep):
        for j,sj in enumerate(keep):
            if i!=j and len(intersection(si,sj))==0:
                lst.append((i,j))
                print(f"{(i,j)} {len(si)}   {len(sj)} ")

    # %%

    for t in updates:
        # a = t
        # m = np.argsort(a)
        # ans.append( a[m[int(m.size/2)]])
        slist = [x for x in master_list if x in t]
        if not test_update(rules,slist):
            break
        mid1 = slist[int((len(t)-1)/2)]
        print(f"{mid1}  {int((len(t)-1)/2)} {slist}")
        ans.append(mid1)
    np.sum(ans) - part1(test_txt)

    # %%
    from tqdm.autonotebook import tqdm
    keep = []
    broken = []
    fixed = []
    fixed_yn = []
    ans = []
    for t in tqdm(updates):
        if test_update(rules,t):
            pass #keep.append(t)
        else:
            broken.append(t)
            slist,x = swap_to_fit_rules(rules,t,1e7)
            if x==0:
                print('prob!!')
            fixed_yn.append(x)
            fixed.append(slist)
            mid1 = slist[int((len(slist)-1)/2)]
            # print(f"{mid1}  {int((len(slist)-1)/2)} {slist}")
            ans.append(mid1)

    # 2442 is too low
    # 5671 is too high
    # %%
