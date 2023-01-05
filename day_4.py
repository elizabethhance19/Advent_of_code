# Overlapping intervals

# Part 1
total_score = 0
with open("day_4.txt") as f:
    for line in f:
        line = line.strip().split(',')
        line = [s.split("-") for s in line]
        a = int(line[0][0])
        b = int(line[0][1])
        c = int(line[1][0])
        d = int(line[1][1])
        if c >= a and d <= b:
            total_score += 1
        elif a >= c and b <= d:
            total_score += 1

print(total_score)

# Part 2
total_score = 0
with open("day_4.txt") as f:
    for line in f:
        line = line.strip().split(',')
        line = [s.split("-") for s in line]
        a = int(line[0][0])
        b = int(line[0][1])
        c = int(line[1][0])
        d = int(line[1][1])
        if a <= c <= b:
            total_score += 1
        elif c <= a <= d:
            total_score += 1

print(total_score)

