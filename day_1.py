# Sum groupings

# Read input
with open("day_1.txt") as f:
    all_lines = f.read()
print(all_lines)

# Part 1
groupings = all_lines.split("\n\n")
print(groupings)

number_groupings = [s.split("\n") for s in groupings]
number_groupings = [[int(j) for j in i] for i in number_groupings]
print(number_groupings)

group_sums = [sum(l) for l in number_groupings]
print(group_sums)
print(max(group_sums))

# Part 2
top_3 = sorted(group_sums, reverse=True)[:3]
print(top_3)
print(sum(top_3))
