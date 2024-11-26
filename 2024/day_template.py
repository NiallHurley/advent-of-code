import os

# Define the folder structure and day template
folder_name = "2024"
day_template = """#%%
daynum = {day}
import numpy as np

with open(f"day{{daynum}}_test_input.txt", "r") as f:
    test_txt = [line.strip() for line in f.readlines()]

with open(f"day{{daynum}}_input.txt", "r") as f:
    input_txt = [line.strip() for line in f.readlines()]

# %%
def part1(txt):
    return None

print(f"Part 1 (test): {{part1(test_txt)}}")
print(f"Part 1: {{part1(input_txt)}}")

# %%
def part2(txt):
    return None

print(f"Part 2 (test): {{part2(test_txt)}}")
print(f"Part 2: {{part2(input_txt)}}")
# %%
"""

# Create 2024 folder if not exists
os.makedirs(folder_name, exist_ok=True)

# Generate files for the first day as an example
day_num = 1
day_folder = os.path.join(folder_name, f"day_{day_num:02}")
os.makedirs(day_folder, exist_ok=True)

# Create the solution file
with open(os.path.join(day_folder, f"day_{day_num:02}.py"), "w") as f:
    f.write(day_template.format(day=day_num))

# Create input and test input files
for input_type in ["input", "test_input"]:
    with open(os.path.join(day_folder, f"day_{day_num:02}_{input_type}.txt"), "w") as f:
        f.write("")  # Empty files to start with

# Verify structure and files created
os.listdir(folder_name)
