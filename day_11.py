# Monkey game
import math
# Sample input
# monkeys = [{'items': [79, 98], 'op': '*19', 'divis': 23, 'true': 2, 'false': 3, 'num_inspection': 0},
#            {'items': [54, 65, 75, 74], 'op': '+6', 'divis': 19, 'true': 2, 'false': 0, 'num_inspection': 0},
#            {'items': [79, 60, 97], 'op': '**2', 'divis': 13, 'true': 1, 'false': 3, 'num_inspection': 0},
#            {'items': [74], 'op': '+3', 'divis': 17, 'true': 0, 'false': 1, 'num_inspection': 0}]

# My input
monkeys = [{'items': [57, 58], 'op': '*19', 'divis': 7, 'true': 2, 'false': 3, 'num_inspection': 0},
           {'items': [66, 52, 59, 79, 94, 73], 'op': '+1', 'divis': 19, 'true': 4, 'false': 6, 'num_inspection': 0},
           {'items': [80], 'op': '+6', 'divis': 5, 'true': 7, 'false': 5, 'num_inspection': 0},
           {'items': [82, 81, 68, 66, 71, 83, 75, 97], 'op': '+5', 'divis': 11, 'true': 5, 'false': 2, 'num_inspection': 0},
           {'items': [55, 52, 67, 70, 69, 94, 90], 'op': '**2', 'divis': 17, 'true': 0, 'false': 3, 'num_inspection': 0},
           {'items': [69, 85, 89, 91], 'op': '+7', 'divis': 13, 'true': 1, 'false': 7, 'num_inspection': 0},
           {'items': [75, 53, 73, 52, 75], 'op': '*7', 'divis': 2, 'true': 0, 'false': 4, 'num_inspection': 0},
           {'items': [94, 60, 79], 'op': '+2', 'divis': 3, 'true': 1, 'false': 6, 'num_inspection': 0}]


# Part 1
for _ in range(20):
    for i, m in enumerate(monkeys):
        print(m)

        for item in m['items']:
            print(item)
            operation = m['op']
            worry_level = eval(str(item) + operation)
            worry_level = worry_level//3

            # Test divis
            if worry_level % m['divis'] == 0:
                monkeys[m['true']]['items'].append(worry_level)
            else:
                monkeys[m['false']]['items'].append(worry_level)
            m['num_inspection'] += 1
        monkeys[i]['items'] = []

print("After round 20")
for i, monkey in enumerate(monkeys):
    print(f"Monkey {i}: {monkey['items']}")
for i, monkey in enumerate(monkeys):
    print(f"Monkey {i}: {monkey['num_inspection']}")

x = sorted([m['num_inspection'] for m in monkeys])
print(x[-1] * x[-2])


# Part 2
# Extend for 10000 rounds, remove divide by 3