# Reorganizing stacks

#stacks = [list('ZN'), list('MCD'), list('P')]
#         [G]         [D]     [Q]
# [P]     [T]         [L] [M] [Z]
# [Z] [Z] [C]         [Z] [G] [W]
# [M] [B] [F]         [P] [C] [H] [N]
# [T] [S] [R]     [H] [W] [R] [L] [W]
# [R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
# [C] [N] [H] [R] [N] [H] [D] [J] [Q]
# [N] [D] [M] [G] [Z] [F] [W] [S] [S]
#  1   2   3   4   5   6   7   8   9

stacks = [list('NCRTMZP'), list('DNTSBZ'), list('MHQRFCTG'),
          list('GRZ'), list('ZNRH'), list('FHSWPZLD'),
          list('WDZRCGM'), list('SJFLHWZQ'), list('SQPWN')]

# Part 1
# with open("day_5.txt") as f:
#     for line in f:
#         input = [int(s) for s in line.split() if s.isdigit()]
#         num_to_move = input[0]
#         from_stack = input[1]-1
#         to_stack = input[2]-1
#
#         for i in range(1, num_to_move+1):
#             stacks[to_stack].append(stacks[from_stack].pop())
#
# top_item = [item[-1] for item in stacks]
# print(''.join(top_item))

# Part 2
with open("day_5.txt") as f:
    for line in f:
        input = [int(s) for s in line.split() if s.isdigit()]
        num_to_move = input[0]
        from_stack = input[1]-1
        to_stack = input[2]-1

        # Add to new stack
        stacks[to_stack].extend(stacks[from_stack][-num_to_move:])
        # Remove from old stack
        del stacks[from_stack][-num_to_move:]

        print(stacks)

top_item = [item[-1] for item in stacks]
print(''.join(top_item))