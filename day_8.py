 # Trees and scenic view
import numpy as np
trees = []
with open("day_8.txt") as f:
    for line in f:
        line = line.strip()
        line = list(map(int, line))
        trees.append(line)

trees = np.array(trees)
nrow = trees.shape[0]
ncol = trees.shape[1]

# Part 1
num_vis = 0
for i in range(0, nrow):
    for j in range(0, ncol):
        # On boundary
        if i == 0 or i == nrow - 1 or j == 0 or j == ncol - 1:
            num_vis += 1
            continue
        max_left = max(trees[i, 0:j])
        max_right = max(trees[i, j+1:ncol])
        max_up = max(trees[0:i, j])
        max_down = max(trees[i+1:nrow, j])
        # Check if tree less than any of maxes
        if trees[i, j] > min([max_left, max_right, max_up, max_down]):
            num_vis += 1
print(num_vis)

# Part 2
def check_visibility(tree, dir_array):
    # If all trees visible
    if np.all(dir_array < tree):
        num_vis = dir_array.size
    else:
        num_vis = np.where((dir_array < tree) == False)[0][0] + 1
    return(num_vis)

max_scenic_score = 0
for i in range(0, nrow):
    for j in range(0, ncol):
        # On boundary
        if i == 0 or i == nrow - 1 or j == 0 or j == ncol - 1:
            continue
        tree = trees[i,j]
        left = trees[i, 0:j]
        right = trees[i, j+1:ncol]
        up = trees[0:i, j]
        down = trees[i+1:nrow, j]

        tree_scenic_score = check_visibility(tree, np.flip(left)) * check_visibility(tree, np.flip(up)) * check_visibility(tree, right) * check_visibility(tree, down)

        max_scenic_score = max(max_scenic_score, tree_scenic_score)

print(max_scenic_score)

