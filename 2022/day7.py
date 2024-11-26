#%%
daynum = 8


with open(f"day{daynum}_test_input.txt", "r") as f:
   test_txt = [line.strip() for line in f.readlines()]

with open(f"day{daynum}_input.txt", "r") as f:
   input_txt = [line.strip() for line in f.readlines()]

# %%
   
def create_dict_of_folder_sizes(txt):
   folders = {}
   prefix = ''
   sep = '|'
   for line in txt:
      if line == "$ cd ..":
         # sep.join("|/|a|d|g".split(sep)[:-1])
         prefix = sep.join(prefix.split(sep)[:-1])
      elif line[0:4] == "$ cd":
         prefix = prefix + sep +line[5:]
      elif line[0:4] == "$ ls":
         folders[prefix] = []
      elif line[0:3] == "dir":
         folders[prefix].append(prefix+sep+line[4:])
      else:
         folders[prefix].append(int(line.split(' ')[0]))

   def sum_up_summable_folders(folders):
      for x in folders.keys():
         try:
            folders[x] = sum(folders[x])
         except:
            pass
      return folders

   def replace_folder_name_with_sizes(folders):
      printing__ = 0
      for x in folders.keys():
         x2 = []
         if printing__ :
            print(f"Before: {folders[x]}")
         if type(folders[x])==list:
            for l in folders[x]:
               # print(l)
               if type(l)==str:
                     if printing__ :
                        print('got here')
                     if type(folders[l])==int:
                        x2.append(folders[l])
                     # try:
                     #     print(f"l = {folders[l]}")
                     #     x2.append(sum(folders[l]))
                     #     print(x2)
                     # except:
                     else:
                        x2.append(l)
               else:
                     x2.append(l)
            folders[x]  = x2
         if printing__ :
            print(f"After: {folders[x]}")
            print("")
      return folders

   counter = 0
   while 1:
      if not any([type(folders[x])==list for x in folders]):
         break
      folders = sum_up_summable_folders(folders)
      folders = replace_folder_name_with_sizes(folders)
      counter+=1
      if int(counter/100) == counter/100:
         print(f"iterations: {counter}")

   return folders



# %%
def part1(txt):
   return None

print(f"Part 1 (test): {part1(test_txt)}")
print(f"Part 1 (test): {part1(input_txt)}")

# %%
def part2(txt):
   return None

print(f"Part 2 (test): {part2(test_txt)}")
print(f"Part 2 (test): {part2(input_txt)}")
# %%
