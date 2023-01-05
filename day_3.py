# Part 1
total_score = 0
with open("day_3_root.txt") as f:
    for line in f:
        print(line)
        line = line.strip()
        comp_1 = set(line[:len(line) // 2])
        comp_2 = set(line[len(line) // 2:])
        intersection = comp_1 & comp_2
        intersection = list(intersection)[0]
        if intersection.isupper():
            total_score += ord(intersection) - 38
        else:
            total_score += ord(intersection) - 96
print(total_score)

# Part 2
total_score = 0
group = []
with open("day_3_root.txt") as f:
    for line in f:
        group.append(set(line.strip()))
        if len(group) != 3:
            continue
        intersection = group[0] & group[1] & group[2]
        intersection = list(intersection)[0]
        if intersection.isupper():
            total_score += ord(intersection) - 38
        else:
            total_score += ord(intersection) - 96
        group = []
print(total_score)
