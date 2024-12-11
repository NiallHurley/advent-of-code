#%%
daynum = "09"
import numpy as np
from tqdm.autonotebook import tqdm

with open(f"day_{daynum}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day_{daynum}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]


#%%
from collections import deque
def process_input(txt):
    tmp = []
    for t in txt:
        tmp.append([int(x) for x in t])
    return tmp

import re

def str_split(ip_str):
    ip = [int(x) if x!='.' else -1 for x in ip_str]
    l1 = re.split(r'\.+', ip_str)
    l2 = re.split(r'\d+', ip_str) 
    return l1, l2

def str_join(l1,l2):
    return ''.join([''.join([x,y]) for x,y in zip(l2,l1)])

def checksum(new_tmpstr):
    return np.sum([int(c)*i if c!='.' else 0 for i,c in enumerate(new_tmpstr)])

def checksum_on_list(listoflists):
    # return np.sum([int(c)*i if c!='.' else 0 for i,c in enumerate(new_tmpstr)])
    tmp = [x for x in flatten_list(listoflists) if x>-9]
    return np.sum([n*i if n>0 else 0 for i,n in enumerate(tmp)])


# final list will be len np.sum(files)
# but positions come from gaps.. 

# %%
def part1(txt):

    ip_list= process_input(txt)
    ans = 0
    for ip in ip_list: 
        files = [x for i,x in enumerate(ip) if i%2 ==0]
        gaps = [x for i,x in enumerate(ip) if i%2 ==1]

        files_vals = [i*[f] for f,i in enumerate(files)]
        files_vals = [item for sublist in files_vals for item in sublist]
        files_vals_rev = files_vals[::-1]

        
        q = deque(files_vals)

        out = []
        for i,c in enumerate(ip):
            
                if i%2==0: # first, third etc i.e. files
                    for j in range(c):
                        if len(q)>0:
                            out.append(q.popleft())
                            ans+= (len(out)-1)*out[-1]
                else:
                    for j in range(c):
                        if len(q)>0:
                            out.append(q.pop())
                            ans+= (len(out)-1)*out[-1]

        # ans, out
    return ans    

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1: {part1(input_txt)}")

# %%
def part2(txt):
    new1 = process_input(txt)[0]

    listoflists =  [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(new1)]
    maxval = np.max(flatten_list(listoflists))

    for v in range(maxval,0,-1):
        firstvals = [l[0] if len(l)>0 else -1 for i,l in enumerate(listoflists)]
        ind = firstvals.index(v)
        # if v==2:
        #     break
        # file_to_move = listoflists[i]
        for fi,f in enumerate(firstvals):
            # if gap (i.e. <0) and it's long enough
            is_gap = f==-1
            gap_is_big_enough = len(listoflists[fi])>=len(listoflists[ind])
            if is_gap and gap_is_big_enough and fi<ind: # gap has to be before file
                # print(fi)
                # fi = 1
                # f = firstvals[fi]


                # then add it to the prev. list item... and reduce the gap size ... and remove the original
                # no no no!!
                # insert the file and then insert the gap!!
                file_to_move = listoflists[ind]

                # reduce gap size 
                listoflists[fi] = listoflists[fi][len(listoflists[ind]):]

                #  clear the moved file
                listoflists[ind] = [-1]*len(file_to_move)

                # insert file .. and insert a gap before it 
                listoflists.insert(fi,file_to_move)
                listoflists.insert(fi,[-10])
                

                # print(listoflists)
                break
    # print(''.join([str(x) if x>=0 else '.' for x in [x for x in flatten_list(listoflists) if x>-9]]))
    return checksum_on_list(listoflists)

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2: {part2(input_txt)}")


# %%

if 0:
    ip_list= process_input(txt)
    ans = 0
    for ip in ip_list: 
        files = [x for i,x in enumerate(ip) if i%2 ==0]
        gaps = [x for i,x in enumerate(ip) if i%2 ==1]

        files_vals = [i*[f] for f,i in enumerate(files)]
        files_vals_rev = files_vals[::-1]

        gapsvals = [[0]*x for i,x in enumerate(ip) if i%2 ==1]

        # out = []
        # for i1,f1 in enumerate(files_vals):
        #     print(i1)
        #     out.append(f1)
        #     gaplen = gaps[i1]
        #     gap_to_fill = [0]*gaplen 
        #     for i2,f2 in enumerate(files_vals_rev):
        #         # print(f"{i1}, {i2}")
        #         if gaplen<=len(f2):
        #             gap_to_fill = f2
        #             # print(f"{files_vals} {i2}")
        #             files_vals.remove(f2)
        #             files_vals_rev.remove(f2)
        #             gaps[i1]=0
        #             break
        #         else:
        #             files_vals_rev.remove(f2)

        #     out.append(gap_to_fill)
        # out        
        tried_file = [False]*len(files_vals)
        newgaps = []
        # for each gap,
        for i,g in enumerate(gapsvals):
            # try each file in reverse
            for fi,ff in enumerate(files_vals[::-1]):
                # if the file fits in the gap then move it (i.e. move it to new gaps and remove from files list)
                # else... mark it as tried.
                if len(ff)<=len(g):
                    move_file = ff
                    files_vals.remove(ff)
                    zeropadded_file = [ff[i] if i <len(ff) else 0 for i in range(len(g)) ]
                    newgaps.append(zeropadded_file)
                else:
                    tried_file[tried_file.index(ff)] = True



    # %%


    '00...111...2...333.44.5555.6666.777.888899'

    listoflists =  [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(ip)]
    listoflists_flattened = [item for sublist in listoflists for item in sublist]
    liststr = ''.join([str(x) if x>=0 else '.' for x in listoflists_flattened])




    gaplens = [x for i,x in enumerate(ip) if i%2 ==1]

    # starting at the last list in the LoL
    new_gaps = []
    for l in listoflists[::-2]:
        # find the first gap longer than l
        for g in gaplens:
            if g>=len(l):
            padded_file = [ff[i] if i <len(ff) else -1 for i in range(len(g)) ]
            new_gaps.append(padded_file)



        for 

        for m in list_of_lists


    tmpstr = inputstr
    tmplist = listoflists_flattened

    # get end bit of str
    val = np.max(tmplist)
    len_val = np.sum((listoflists_flattened==np.max(tmplist)))




    # %%
    import re

    def lol_to_str(lol):
        listoflists_flattened = [item for sublist in lol for item in sublist]
        return ''.join([str(x) if x>=0 else '.' for x in listoflists_flattened])

    def str_to_lol(ip_str):
        ip = [int(x) if x!='.' else -1 for x in ip_str]
        l1 = re.split(r'\.+', ip_str)
        l2 = re.split(r'\d+', ip_str) 
        return [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(ip)]
    str_to_lol(lol_to_str(listoflists))
    # %%



    # %%
    # get end bit of str
    ip_list= process_input(test_txt)
    ans = 0
    for ip in ip_list:
    # ip = ip_list[0]
        listoflists =  [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(ip)]
        listoflists_flattened = [item for sublist in listoflists for item in sublist]
        liststr = ''.join([str(x) if x>=0 else '.' for x in listoflists_flattened])
        val = np.max(listoflists_flattened)
        tmpstr = liststr
        pointer = len(tmpstr.strip('.'))
        new_tmpstr = tmpstr

        for i in range(val+1)[::-1]:
            if i<0:
                break
            valstr = str(i)

            # no need to mosve values after the number of interest
            postval_str = new_tmpstr[new_tmpstr.rfind(valstr)+1:]
            # tmpstr is the whole string excl the postval_str
            tmpstr = new_tmpstr[:new_tmpstr.rfind(valstr)+1]
            # print(f"tmpstr: {tmpstr}   | {postval_str}")
            
            # split the 'pre' str into the file and the pre-str
            ind =tmpstr.find(valstr)
            pre_tmpstr = tmpstr[:ind]
            file_to_move = tmpstr[ind:]


            # split the pre str to help identify the gaps
            nums, gaps = str_split(pre_tmpstr)
            file_moved = False
            for j,g in enumerate(gaps):
                if len(g)>=len(file_to_move):
                    # if there's room... fill in the string and pad with '.'
                    gaps[j] = file_to_move + gaps[j][len(file_to_move):]
                    # nums[j] = nums[j]+''.join(['.']*len(g))
                    file_moved = True
                    break


            # recompose the str
            new_pre_tmpstr = str_join(nums, gaps)
            if file_moved:
                new_tmpstr = new_pre_tmpstr + ''.join(['.']*len(file_to_move)) +  postval_str
            else: 
                new_tmpstr = new_pre_tmpstr + file_to_move +  postval_str
            # print(f"new_tmpstr: {new_tmpstr}")
        ans += checksum(new_tmpstr)

    print(ans)

    # %%
    new1 = process_input(test_txt)[0]

    listoflists =  [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(new1)]
    listoflists_flattened = [item if len(sublist)>0 else None  for sublist in listoflists for item in sublist]

    # %%


    def flatten_list(listoflists):
        # empty 'gaps' are marked as -10
        return [item for sublist in [l if len(l)>0 else [-10] for l in  listoflists] for item in sublist]

    def unflatten_list(listoflists_flattened):
        tmp =[]
        local_tmp=[]
        for i,x in enumerate(listoflists_flattened):
            if i==0:
                local_tmp.append(x)
            else:
                if x!=listoflists_flattened[i-1]:
                    tmp.append(local_tmp)
                    local_tmp = []
                    local_tmp.append(x)
                else:
                    local_tmp.append(x)
        tmp.append(local_tmp)

        # replace the -10 with []
        return [k if k!=[-10] else [] for k in tmp]

        # %%
        tmp = listoflists[10:]

    # %%
    new1 = process_input(test_txt)[0]

    listoflists =  [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(new1)]
    maxval = np.max(flatten_list(listoflists))

    for v in range(maxval,0,-1):
        firstvals = [l[0] if len(l)>0 else -1 for i,l in enumerate(listoflists)]
        ind = firstvals.index(v)
        # if v==2:
        #     break
        # file_to_move = listoflists[i]
        for fi,f in enumerate(firstvals):
            # if gap (i.e. <0) and it's long enough
            is_gap = f==-1
            gap_is_big_enough = len(listoflists[fi])>=len(listoflists[ind])
            if is_gap and gap_is_big_enough and fi<ind: # gap has to be before file
                # print(fi)
                # fi = 1
                # f = firstvals[fi]


                # then add it to the prev. list item... and reduce the gap size ... and remove the original
                # no no no!!
                # insert the file and then insert the gap!!
                file_to_move = listoflists[ind]

                # reduce gap size 
                listoflists[fi] = listoflists[fi][len(listoflists[ind]):]

                #  clear the moved file
                listoflists[ind] = [-1]*len(file_to_move)

                # insert file .. and insert a gap before it 
                listoflists.insert(fi,file_to_move)
                listoflists.insert(fi,[-10])
                

                # print(listoflists)
                break
        print(''.join([str(x) if x>=0 else '.' for x in [x for x in flatten_list(listoflists) if x>-9]]))

    # ''.join([str(x) if x>=0 else '.' for x in [x for x in flatten_list(listoflists) if x>-9]])

    # ans: 00992111777.44.333....5555.6666.....8888..
    #     '0099211177744.333..5555.6666..8888'
    # %%



    # %%


    def part2_wrong(txt):
        ip_list= process_input(txt)
        ans = []
        for ip in tqdm(ip_list, total = len(ip_list)):
        # ip = ip_list[0]
            listoflists =  [int(x)*[int(i/2)] if i%2 ==0 else [-1]*int(x) for i,x in enumerate(ip)]
            listoflists_flattened = [item for sublist in listoflists for item in sublist]
            liststr = ''.join([str(x) if x>=0 else '.' for x in listoflists_flattened])
            val = np.max(listoflists_flattened)
            tmpstr = liststr
            pointer = len(tmpstr.strip('.'))
            new_tmpstr = tmpstr

            for i in range(val+1)[::-1]:
                if i<0:
                    break
                valstr = str(i)

                # no need to mosve values after the number of interest
                postval_str = new_tmpstr[new_tmpstr.rfind(valstr)+1:]
                # tmpstr is the whole string excl the postval_str
                tmpstr = new_tmpstr[:new_tmpstr.rfind(valstr)+1]
                # print(f"tmpstr: {tmpstr}   | {postval_str}")
                
                # split the 'pre' str into the file and the pre-str
                ind =tmpstr.find(valstr)
                pre_tmpstr = tmpstr[:ind]
                file_to_move = tmpstr[ind:]


                # split the pre str to help identify the gaps
                nums, gaps = str_split(pre_tmpstr)
                file_moved = False
                for j,g in enumerate(gaps):
                    if len(g)>=len(file_to_move):
                        # if there's room... fill in the string and pad with '.'
                        gaps[j] = file_to_move + gaps[j][len(file_to_move):]
                        # nums[j] = nums[j]+''.join(['.']*len(g))
                        file_moved = True
                        break


                # recompose the str
                new_pre_tmpstr = str_join(nums, gaps)
                if file_moved:
                    new_tmpstr = new_pre_tmpstr + ''.join(['.']*len(file_to_move)) +  postval_str
                else: 
                    new_tmpstr = new_pre_tmpstr + file_to_move +  postval_str
                # print(f"new_tmpstr: {new_tmpstr}")
            ans.append(checksum(new_tmpstr))
        print(len(ans), len(ip_list))

        return np.sum(ans)