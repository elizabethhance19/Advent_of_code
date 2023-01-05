# Rock paper scissors

# Part 1
lookup = {'A X': 4, #3+1,
          'A Y': 8, #6+2,
          'A Z': 3, #0+3,
          'B X': 1, #0+1
          'B Y': 5, #3+2
          'B Z': 9, #6+3,
          'C X': 7, #6+1,
          'C Y': 2, #0+2,
          'C Z': 6} #3+3

total_score = 0
with open("day_2.txt") as f:
    for line in f:
        plays = line.strip()
        play_score = lookup[plays]
        total_score += play_score
print(total_score)

# Part 2
lookup = {'A X': 3,
          'A Y': 4,
          'A Z': 8,
          'B X': 1,
          'B Y': 5,
          'B Z': 9,
          'C X': 2,
          'C Y': 6,
          'C Z': 7}

total_score = 0
with open("day_2.txt") as f:
    for line in f:
        plays = line.strip()
        play_score = lookup[plays]
        total_score += play_score
print(total_score)


