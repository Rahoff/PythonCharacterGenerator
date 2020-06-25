"""Create a Wizard character"""
import random

import lvladjust
import saves
import size


def create_character(abilities):
    # Sort and shorten the ability list
    abilities.sort(reverse=True)
    abilities = abilities[:7]
    return abilities


def compute_skillpoints(job, intel_bonus, race, lvl):
    racial_bonus = 0
    if race == 'Human':
        racial_bonus = 4

    start_skill = (2 + intel_bonus) * 4 + racial_bonus
    adjusted_skill = lvladjust.skillsadj(job, intel_bonus, lvl)
    return start_skill + adjusted_skill


def compute_age(race):
    age = 0
    if race == 'Human':
        age = 15 + random.randint(1, 6) + random.randint(1, 6)
    if race == 'Dwarf':
        age = 40 + (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                    + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))
    if race == 'Elf':
        age = 110 + (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                     + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                     + random.randint(1, 6) + random.randint(1, 6))
    return age


def format_sheet(race, sex, job, name, abilities, char_name, lvl):
    # Assign abilities rolls to the best ability for the class
    strength = abilities[5]
    con = abilities[3]
    dex = abilities[1]
    intel = abilities[0]
    wis = abilities[2]
    cha = abilities[4]
    com = abilities[6]
    # Make racial adjustments to abilities
    if race == 'Dwarf':
        con = con + 2
        com = com - 2
    if race == 'Elf':
        dex = dex + 2
        con = con - 2

    # figure out ability bonuses
    str_bonus = 0
    dex_bonus = 0
    con_bonus = 0
    intel_bonus = 0
    wis_bonus = 0
    cha_bonus = 0
    com_bonus = 0

    if strength > 11 or strength < 10:
        str_bonus = size.ability_bonus(strength)
    if con > 11 or con < 10:
        con_bonus = size.ability_bonus(con)
    if dex > 11 or dex < 10:
        dex_bonus = size.ability_bonus(dex)
    if intel > 11 or intel < 10:
        intel_bonus = size.ability_bonus(intel)
    if wis > 11 or wis < 10:
        wis_bonus = size.ability_bonus(wis)
    if cha > 11 or cha < 10:
        cha_bonus = size.ability_bonus(cha)
    if com > 11 or com < 10:
        com_bonus = size.ability_bonus(com)

    # fill out all vital stats
    hp = lvladjust.hitpointsadj(con_bonus, lvl, job)
    skills = compute_skillpoints(job, intel_bonus, race, lvl)
    feats = lvladjust.featadj(lvl, job, race)
    age = compute_age(race)
    height = size.compute_height(race, sex)
    weight = size.compute_weight(race, sex)
    save = saves.wizsaves(lvl)
    ability_incr = lvladjust.ability_increase(lvl)

    # print everything to the character file
    with open(char_name, 'a') as f:
        print("NAME--", name, "  RACE--", race, "  CLASS--", job, "  LEVEL--", lvl, "  AGE--", age, file=f)
        print("", file=f)
        print("SEX--", sex, "  HEIGHT--", height, "  WEIGHT--", weight, file=f)
        print("", file=f)
        print("STR: ", strength, "  Bonus- ", str_bonus, file=f)
        print("DEX: ", dex, "  Bonus- ", dex_bonus, file=f)
        print("CON: ", con, "  Bonus- ", con_bonus, file=f)
        print("INT: ", intel, "  Bonus- ", intel_bonus, file=f)
        print("WIS: ", wis, "  Bonus- ", wis_bonus, file=f)
        print("CHA: ", cha, "  Bonus- ", cha_bonus, file=f)
        print("COM: ", com, "  Bonus- ", com_bonus, file=f)
        print("", file=f)
        print("Hit Points = ", hp, file=f)
        print("", file=f)
        print("Skill points = ", skills, file=f)
        print("", file=f)
        print("Feats = ", feats, file=f)
        print("", file=f)
        print("Available ability points to spend = ", ability_incr, file=f)
        print("", file=f)
        print("                Fortitude   Reflex   Will", file=f)
        print("                -------------------------", file=f)
        print("Saving Throws =    ", save[0] + con_bonus, "        ", save[1] + dex_bonus, "    ", save[2] + wis_bonus,
              file=f)
        print("", file=f)

    x = open("wizardspells.txt", "r")
    x1 = x.readline()
    for i in range(lvl + 3):
        with open(char_name, 'a') as f:
            print(x1, file=f)
        x1 = x.readline()

