# Head and tail
import numpy as np

"""
# Part 1
h = np.array([0, 0])
t = np.array([0, 0])
t_visit = [t]

# T movement:
    # if T beside H -> don't move
    # else: T goes to previous H spot

def is_touching(h, t):
    # Distance > 1
    if any(abs(h-t) > 1):
        return False
    return True


def make_move(direction, h, t):
    previous_h = np.copy(h)

    if direction == 'R':
        h[0] += 1
    elif direction == 'L':
        h[0] -= 1
    elif direction == 'U':
        h[1] += 1
    elif direction == 'D':
        h[1] -= 1

    # Move t if not touching
    if not is_touching(h,t):
        t = previous_h

    return h, t

with open("day_9_sample.txt") as f:
    for line in f:
        line = line.split()
        direction = line[0]
        moves = int(line[1])

        for move in range(moves):
            h, t = make_move(direction, h, t)
            t_visit.append(t)

        print(h)
        print(t)

# Get count unique coordinates from t_visit
print(len([list(x) for x in set(tuple(x) for x in t_visit)]))
"""

# Part 2
knots = np.array([[0, 0]] * 10)  # where knots[0] -> head
tail_visit = {(knots[-1][0], knots[-1][1])}


def move_b(a, b):
    b = b + np.sign(a - b)
    return b


def is_touching(a, b):
    if any(abs(a - b) > 1):
        return False
    return True


def make_move(direction, knots):
    # First move head
    if direction == 'R':
        knots[0][0] += 1
    elif direction == 'L':
        knots[0][0] -= 1
    elif direction == 'U':
        knots[0][1] += 1
    elif direction == 'D':
        knots[0][1] -= 1

    # Go through tail 1-9, check if touching, if not touching then move
    for i in range(1, len(knots)):
        if not is_touching(knots[i - 1], knots[i]):
            knots[i] = move_b(knots[i - 1], knots[i])

    return knots


with open("day_9.txt") as f:
    for line in f:
        line = line.split()
        direction = line[0]
        moves = int(line[1])

        for move in range(moves):
            knots = make_move(direction, knots)
            print(knots[-1])
            tail_visit.add((knots[-1][0], knots[-1][1]))


# Get count unique coordinates from tail_visit
print(len(tail_visit))
