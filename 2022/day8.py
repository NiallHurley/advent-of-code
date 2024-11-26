#%%
daynum = 8


with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]


import numpy as np

# %%

def visible_trees(txt):
   m = np.array([[int(c) for c in line.strip()] for line in txt])
   v = np.zeros(m.shape).astype(int)

   eps = np.ones(m.shape)*.001
   eps_cs = np.flipud(np.cumsum(eps,axis=0))

   for r in range(0,4):
      m_rot = np.rot90(m,-r)+ eps_cs
      m_cummax_rot = np.maximum.accumulate(m_rot)
      this_v = (m_rot == m_cummax_rot).astype(int)
      this_v_unrot =np.rot90(this_v,r)
      print(m_rot, m_cummax_rot)
      v+=this_v_unrot

   return sum(v.flatten()>0)




# %%
def part1(txt):
   
   return visible_trees(txt)

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1 : {part1(input_txt)}")



# x='|/|a'
# x2 = []
# print(f"Before: {folders[x]}")
# if type(folders[x])==list:
#     for l in folders[x]:
#         print(l)
#         if type(l)==str:
#             print('got here')
#             if type(folders[l])==int:
#                 x2.append(folders[l])
#             # try:
#             #     print(f"l = {folders[l]}")
#             #     x2.append(sum(folders[l]))
#             #     print(x2)
#             # except:
#             else:
#                 x2.append(l)
#         else:
#             x2.append(l)
#     folders[x]  = x2
# print(f"After: {folders[x]}")
# print("")
# folders
# %%
def count_vis_trees(treeline, h):
   for i,t in enumerate(treeline):
      if t>=h:
         return(i+1)
   return(len(treeline))


def part2(txt):
   m = np.array([[int(c) for c in line.strip()] for line in txt])
   v = np.zeros(m.shape).astype(int)
   a = 0

   R,C = m.shape
   for r in range(R):
      for c in range(C):
         c_tree = m[r,c]
         # get row and column
         row_l = np.flip(m[r,:c]) # flip so that we can check from left to right
         row_r = m[r,(c+1):]
         
         col_u = np.flip(m[:r,c]) # flip so that we can check from left to right
         col_d = m[(r+1):,c]

         # print([row_l,row_r, col_u,col_d]) # print to check

         # now just count trees until we see one the same height as c_tree
         a =  np.max([a,np.prod([count_vis_trees(col_u,c_tree),
               count_vis_trees(col_d,c_tree),
               count_vis_trees(row_l,c_tree),
               count_vis_trees(row_r,c_tree)])])
         
         # print([count_vis_trees(col_u,c_tree),
         #       count_vis_trees(col_d,c_tree),
         #       count_vis_trees(row_l,c_tree),
         #       count_vis_trees(row_r,c_tree)]) 
   return a

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2 (test): {part2(input_txt)}")
# %%


# [[3 0 3 7 3]
#  [2 5 5 1 2]
#  [6 5 3 3 2]
#  [3 3 5 4 9]
#  [3 5 3 9 0]]


# %%

   