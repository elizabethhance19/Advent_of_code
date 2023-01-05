# Navigating directories and their sizes

# Directory class
class Directory():
    def __init__(self, name, parent=None):
        self.name = name
        self.size = 0
        self.parent = parent
        self.dir = {}
        self.file = []

# Read input and build directory tree
with open("day_7_sample.txt") as f:
    root_dir = Directory('/')
    current_dir = root_dir
    for line in f:
        line = line.strip()
        if line in ['$ cd /', '$ ls']:
            continue
        elif line == '$ cd ..':
            current_dir = current_dir.parent
        elif line.startswith('$ cd'):
            current_dir = current_dir.dir[line.split()[2]]
        elif line.startswith('dir'):
            current_dir.dir[line.split()[1]] = Directory(line.split()[1], parent=current_dir)
        else:
            current_dir.size += int(line.split()[0])

# Calculate size of each directory
    # Issue when duplicate directory names
# dir_totals = {}
# def dfs(directory, dir_totals):
#     dir_totals[directory.name] = directory.size
#     for subdir in directory.dir.values():
#         dir_totals[directory.name] += dfs(subdir, dir_totals)
#     return dir_totals[directory.name]
# dfs(root_dir, dir_totals)
# print(sum(i for i in dir_totals.values() if i <= 100000))

list_totals = []
def dfs(directory, list_totals):
    sub_t = directory.size
    for subdir in directory.dir.values():
        sub_t += dfs(subdir, list_totals)
    list_totals.append(sub_t)
    return sub_t
# def dfs(directory, list_totals):
#     print('directory.name = ', directory.name)
#     sub_t = directory.size
#     print(sub_t)
#     for subdir in directory.dir.values():
#         print('subdir.name = ', subdir.name)
#         sub_t += dfs(subdir, list_totals)
#         print('for loop sub_t', sub_t)
#     print('append ', sub_t)
#     list_totals.append(sub_t)
#     print('return')
#     return sub_t

dfs(root_dir, list_totals)

# Part 1
print(sum(i for i in list_totals if i <= 100000))


# Part 2
root_dir_size = max(list_totals)
min_space_to_free = 30000000 - (70000000 - root_dir_size)
print(min(i for i in list_totals if i >= min_space_to_free))
