import numpy as np
from tqdm.autonotebook import tqdm
import matplotlib.pyplot as plt
from scipy.spatial.distance import cityblock

#ax.imshow(data, extent=[0, 1, 0, 1]) # imagesc


txt = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
tmp = []
for l in txt.split('\n'):
  tmp.append([x for x in l])

map_ = np.array(tmp)
print(map_)

a,b = np.where(map_=='S')
start_loc = (a[0],b[0])



def take_next_step(curr_loc, curr_steps,step_count_max = 64):
  new_locs=[]
  # north
  new_locs.append((curr_loc[0]-1,curr_loc[1]+0))
  # south
  new_locs.append((curr_loc[0]+1,curr_loc[1]+0))
  # east
  new_locs.append((curr_loc[0]+0,curr_loc[1]+1))
  # west
  new_locs.append((curr_loc[0]+0,curr_loc[1]-1))

  new_steps = curr_steps+1
  # print(new_locs)
  for new_loc in new_locs:
    # print(new_loc)
    # check boundary
    stepped_outside =  (new_loc[0]>=mat.shape[0] or
                      new_loc[1]>=mat.shape[1] or
                      new_loc[0]<0 or
                      new_loc[1]<0 )

    if not stepped_outside:
       # check for rocks
      is_rock =  map_[new_loc] == '#'
      if not is_rock:
        # if step_count_max reached...
        if new_steps<step_count_max:
          # take another step
          # print(f'calling {[new_loc, new_steps]},{new_steps,step_count_max}')
          take_next_step(new_loc, new_steps,step_count_max)
        else:
          assert new_steps==step_count_max
          # note the location
          mat[new_loc] =1



n_steps = 64
global mat
a,b = np.where(map_=='S')
new_start_loc = [(a[i],b[i]) for i in range(len(a))]
for _ in tqdm(range(n_steps), desc=" outer", position=0):
  # use 'set' to remove duplicates
  new_start_loc = set(new_start_loc)
  # print(f"\t{i} : {len(new_start_loc)} ")
  mat = np.zeros(map_.shape)
  for start_loc in  tqdm(new_start_loc, desc=" inner", position=1,leave=False):
    take_next_step(start_loc, 0, 1)
    a,b = np.where(mat==1)
    new_start_loc = [(a[i],b[i]) for i in range(len(a))]


print(np.sum(np.sum(mat)))
print(mat)

