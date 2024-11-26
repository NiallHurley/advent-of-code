#%%
daynum = 23

import numpy as np

with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

# %%
   
# ok ... want to 'walk' each path and count the steps... 
#    but there are junctions... so let's walk the path
#    until we get to a junction
#    in fact... let's identify all the junctions... then
#    walk each path between junctions...
#    then arrange the 'junction to junction' path which maximises
#    the number of steps
   
# def get_junctions()

from collections import deque

lines = test_txt
lines = input_txt
# lines = txt.split('\n')
R, C = len(lines), len(lines[0])


dirs = [(1,0),(0,1),(-1,0),(0,-1)]


q = deque()
dist={}
junction={}
visited = {}

start_node = (0,lines[0].find('.'))
end_node = (R-1,lines[-1].find('.'))
junction[start_node] = 2
junction[end_node] = 2

# initialise to start loc
# for r, line in enumerate(lines):
#    if 'S' in line:
#        q.append((r, line.index('S')))


q.append(start_node)

def allowable_dir(curr_symbol, dr, dc):
    return True
    # if curr_symbol != '#':
    #     return True
    # elif (curr_symbol == '>' and dr==0  and dc==1) or \
    #     (curr_symbol == '<' and dr==0  and dc==-1) or \
    #     (curr_symbol == '^' and dr==-1  and dc==0) or \
    #     (curr_symbol == 'v' and dr==1  and dc==0):
    #     return True
    # else:
    #     return False

opts = 0
while q:
    # popleft coord
    r,c = q.popleft()
    if visited.get((r,c)) == None:
        visited[(r,c)] = 1
        # step in each direction
        for dr,dc in dirs:
            newr, newc  = r+dr, c+dc  
            if  0 <= newr < R and 0 <= newc < C and lines[newr][newc]!='#':       
                q.append((newr,newc))
                opts +=1
        if opts>2:
            junction[r,c] = opts
        opts = 0

print('junctions:')
for key, value in junction.items():
    # The if statement checks if the value of each item is equal to 56.
    if value >1 :
        # If the value is equal to 56, the key of that item is printed.
        print(key)


#%%
        
# visited = set() # Set to keep track of visited nodes of graph.

# def dfs(visited, graph, node):  #function for dfs 
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

j1 = (0, 1)
j2 = (5, 3)

j_dists = junction.copy()
for key in j_dists:
    j_dists[key] = 0

visited = {} # Set to keep track of visited nodes of graph.
mlen = {}


# this function aims to find the length of the path between pairs of 'junction' nodes
def dfs_pathlength_between_nodes(visited, lines, node,maxlen,dest):  #function for dfs 
    if node not in visited:
        retval = maxlen
        print (node,maxlen)
        visited[node] = maxlen+1
        r,c = node
        for dr,dc in dirs:
            newr, newc  = r+dr, c+dc 
            allowed =  allowable_dir(lines[r][c], dr,dc) and 0 <= newr < R and 0 <= newc < C and lines[newr][newc]!='#'
            is_junction = (newr,newc) in junction
            if allowed:
                if is_junction:
                    print((newr,newc))
                if (newr,newc) == dest:
                    print(f'here {(newr,newc)}, {maxlen},{node}')
                    j_dists[(newr,newc)] = maxlen+1
                    visited[(newr,newc)] = maxlen+2
                    return(maxlen)
                    

                if not is_junction:
                    # print((newr,newc))
                    retval = dfs_pathlength_between_nodes(visited, lines, (newr,newc),maxlen+1,dest)
        return(retval)
    else:
        return(None)




a = dfs_pathlength_between_nodes(visited,lines,j1,0,j2)
print(f"a = {a}")

# def longest_path(coord_,len_so_far,max_len):
#     # if type(coord_) != tuple:
#     #     return max_len
#     local_max = len_so_far

    
#      # step in each direction
#     for dr,dc in dirs:
#         newr, newc  = r+dr, c+dc 
#         allowed =  allowable_dir(lines[r][c], dr,dc) and 0 <= newr < R and 0 <= newc < C and lines[newr][newc]!='#'
#         if allowed:
#             local_max = max(local_max,longest_path((newr,newc),len_so_far+1,max_len))
#             if (newr,newc) in junction:
#                 j_dists[(newr,newc)] = local_max
#     max_len = max(max_len,local_max)        
                

# longest_path(j1,0,0)



# %%












j_dists = junction.copy()
for key in j_dists:
    j_dists[key] = 0

visited = {} # Set to keep track of visited nodes of graph.


# this function aims to find the length of the path between pairs of 'junction' nodes
def dfs_pathlength_between_nodes(visited, lines, node,maxlen,dest):  #function for dfs 
    if node not in visited:
        retval = maxlen
        # print (node,maxlen)
        visited[node] = maxlen+1
        r,c = node
        for dr,dc in dirs:
            newr, newc  = r+dr, c+dc 
            allowed =  allowable_dir(lines[r][c], dr,dc) and 0 <= newr < R and 0 <= newc < C and lines[newr][newc]!='#'
            is_junction = (newr,newc) in junction
            if allowed:
                if is_junction:
                    # print((newr,newc))
                    # if (newr,newc) == dest:
                        # print(f'here {(newr,newc)}, {maxlen},{node}')
                    j_dists[(newr,newc)] = maxlen+1
                    visited[(newr,newc)] = maxlen+2
                    return(maxlen)
                    
                else:
                    # print((newr,newc))
                    retval = dfs_pathlength_between_nodes(visited, lines, (newr,newc),maxlen+1,dest)
        return(retval)
    else:
        # print('here')
        return(None)



j_out = {}
outmat = np.zeros([len(j_dists),len(j_dists)])

for  i,j1 in enumerate( j_dists):
    for  i2,j2 in enumerate( j_dists):
            if i!=i2:
        # if i2>i:
                # print([i,i2], [j1,j2])
                visited = {} # Set to keep track of visited nodes of graph.

                a = dfs_pathlength_between_nodes(visited,lines,j1,0,j2)
                if j2 in visited:
                    outmat[i,i2] = visited[j2]

                    tmp = ((j2[0],j2[1]),visited[j2])
                    print('tmp',tmp)
                    if j1 not in j_out: # or j_out[j1] is None:
                        j_out[j1] = [tmp]
                    else:
                        j_out[j1] = j_out[j1].append(tmp)

j_out,outmat
# %%
[r,c]=np.where(outmat)
js  = list( j_dists.keys())
edges = []
for i in zip(r,c):
    edges.append([js[i[0]],js[i[1]],outmat[i]])

# %%
def find_longest_path(edges, start, end):
    from collections import defaultdict

    # Create a graph representation from the edge list
    graph = defaultdict(list)
    for edge in edges:
        from_junction, to_junction, distance = edge
        graph[tuple(from_junction)].append((tuple(to_junction), distance-1))
        graph[tuple(to_junction)].append((tuple(from_junction), distance-1))

    # Helper function to perform DFS
    def dfs(current, end, visited, current_length):
        if current == end:
            return current_length
        visited.add(current)
        max_length = 0
        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                max_length = max(max_length, dfs(neighbor, end, visited, current_length + distance))
        visited.remove(current)
        return max_length

    return dfs(tuple(start), tuple(end), set(), 0)

# 

start = start_node
end = end_node
longest_path_length = find_longest_path(edges, start, end)
print("Longest path length:", longest_path_length)

# %%


# # %%
# def part1(txt):
#    return None

# print(f"Part 1 (test): {part1(test_txt)}")
# print(f"Part 1: {part1(input_txt)}")

# # %%
# def part2(txt):
#    return None

# print(f"Part 2 (test): {part2(test_txt)}")
# print(f"Part 2: {part2(input_txt)}")
# %%
