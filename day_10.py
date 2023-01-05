# Noop/Addx, sprite position
# Part 1
cycle_values = [1]
update_for_next_cycle = cycle_values[0]
with open("day_10.txt") as f:
    for line in f:
        line = line.split()
        instruction = line[0]

        print(line)

        if instruction == 'noop':
            cycle_values.append(update_for_next_cycle)
        elif instruction == 'addx':
            value = int(line[1])
            cycle_values.append(update_for_next_cycle)
            cycle_values.append(update_for_next_cycle)
            update_for_next_cycle += value
# print(sum([cycle_values[20]*20, cycle_values[60]*60, cycle_values[100]*100, cycle_values[140]*140, cycle_values[180]*180, cycle_values[220]*220]))

# Part 2
grid = [["." for x in range(40)] for y in range(6)]

grid_row = 0
for cycle_number in range(1, len(cycle_values)):
    sprite_center = cycle_values[cycle_number]
    grid_pos = (cycle_number - 1) % 40
    #print('cycle_number ', cycle_number)
    #print('sprite_center ', sprite_center)
    #print('grid_pos to change ', grid_pos)

    # if center or +- 1 = cycle_number -> write in grid[row, cycle_number-1]
    if grid_pos in [sprite_center, sprite_center-1, sprite_center+1]:
        grid[grid_row][grid_pos] = '#'
        #print('change')

    if cycle_number % 40 == 0:
        grid_row += 1

for line in grid:
    print(''.join(line))

# 1,2,3 -> 0,1,2
# 41, 42, 43 -> 0,1,2
# 81, 82, 83



"""
grid_row = 0
for cycle_number in range(1, len(cycle_values)):
    sprite_center = cycle_values[cycle_number]

    # if center or +- 1 = cycle_number -> write in grid[row, cycle_number-1]
    if cycle_number in [sprite_center, sprite_center-1, sprite_center+1]:
        grid[grid_row][cycle_number-1] = '#'

    if cycle_number % 40 == 0:
        grid_row += 1
"""