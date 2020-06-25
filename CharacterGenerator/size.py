import math
import random


def compute_height(race, sex):
    height = 0
    if race == 'Human':
        size_mod = random.randint(1, 10) + random.randint(1, 10)
        if sex == 'Male':
            inches = 58 + size_mod
            feet = math.floor(inches / 12)
            height = ('%.0f' % feet) + "'" + str(inches % 12) + '"'
        else:
            inches = 53 + size_mod
            feet = math.floor(inches / 12)
            height = ('%.0f' % feet) + "'" + str(inches % 12) + '"'

    if race == 'Dwarf':
        size_mod = random.randint(1, 4) + random.randint(1, 4)
        if sex == 'Male':
            inches = 45 + size_mod
            feet = math.floor(inches / 12)
            height = ('%.0f' % feet) + "'" + str(inches % 12) + '"'
        else:
            inches = 43 + size_mod
            feet = math.floor(inches / 12)
            height = ('%.0f' % feet) + "'" + str(inches % 12) + '"'

    if race == 'Elf':  # Male and Female elves are the same height.
        size_mod = random.randint(1, 6) + random.randint(1, 6)
        inches = 53 + size_mod
        feet = math.floor(inches / 12)
        height = ('%.0f' % feet) + "'" + str(inches % 12) + '"'

    return height


def compute_weight(race, sex):
    weight = 0
    if race == 'Human':
        size_mod = random.randint(1, 10) + random.randint(1, 10)
        if sex == 'Male':
            weight = 120 + (size_mod * (random.randint(1, 4) + random.randint(1, 4)))
        else:
            weight = 85 + (size_mod * (random.randint(1, 4) + random.randint(1, 4)))

    if race == 'Dwarf':
        size_mod = random.randint(1, 4) + random.randint(1, 4)
        if sex == 'Male':
            weight = 130 + (size_mod * (random.randint(1, 6) + random.randint(1, 6)))
        else:
            weight = 100 + (size_mod * (random.randint(1, 6) + random.randint(1, 6)))

    if race == 'Elf':
        size_mod = random.randint(1, 6) + random.randint(1, 6)
        if sex == 'Male':
            weight = 85 + (size_mod * (random.randint(1, 6)))
        else:
            weight = 80 + (size_mod * (random.randint(1, 6)))

    return weight


def ability_bonus(base):
    bonus = 0
    if base == 12 or base == 13:
        bonus = 1
    if base == 14 or base == 15:
        bonus = 2
    if base == 16 or base == 17:
        bonus = 3
    if base == 18 or base == 19:
        bonus = 4
    if base == 20 or base == 21:
        bonus = 5

    if base == 8 or base == 9:
        bonus = -1
    if base == 6 or base == 7:
        bonus = -2
    if base == 4 or base == 5:
        bonus = -3
    if base == 2 or base == 3:
        bonus = -4
    if base == 1:
        bonus = -5

    return bonus
