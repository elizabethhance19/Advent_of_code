# Unique substring

# Read input
with open("day_6.txt") as f:
    line = f.read()
    print(line)

# Part 1
for index in range(0, len(line) - 3):
    sub = line[index:index+4]
    print(sub)
    if len(sub) == len(set(sub)):
        print(index+4)
        break

# Part 2
for index in range(0, len(line) - 13):
    sub = line[index:index+14]
    if len(sub) == len(set(sub)):
        print(index+14)
        break
