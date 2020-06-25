import random
import cleric
import fighter
import rogue
import wizard

while True:
    # Get name of new character and start the txt file
    name = input('What is the name of this character? ')
    print("")
    char_name = str(name + ".txt")
    with open(char_name, 'w') as f:
        print("Here are " + name + "'s ability rolls.", file=f)
        print("", file=f)

    # Validate and format class input
    print("What class would you like generate? (W)izard, (F)ighter, (C)leric, or (R)ogue...")
    job = input("Enter 'W, F, C, R': ")
    print("")
    while True:
        if job.upper() == 'W' or job.upper() == 'F' or job.upper() == 'C' or job.upper() == 'R':
            break
        else:
            job = input("Please enter a W for wizard, F for fighter, C for cleric or R for Rogue.")
    if job.upper() == 'W':
        job = 'Wizard'
    if job.upper() == 'F':
        job = 'Fighter'
    if job.upper() == 'C':
        job = 'Cleric'
    if job.upper() == 'R':
        job = 'Rogue'

    # Validate and format race input
    print("Now chose a Race. (H)uman, (E)lf, (D)warf,) ")
    race = input("Enter 'H, E, or D': ")
    print("")
    while True:
        if race.upper() == 'H' or race.upper() == 'E' or race.upper() == 'D':
            break
        else:
            race = input("Please enter an 'H' for Human, an 'E' for Elf or a 'D' for dwarf")
    if race.upper() == 'H':
        race = 'Human'
    if race.upper() == 'E':
        race = 'Elf'
    if race.upper() == 'D':
        race = 'Dwarf'

    # choose a starting level

    while True:
        try:
            lvl = int(input("What level would you like to make? Enter 1 - 20: "))
            if 0 < lvl < 21:
                break
            else:
                print("Please enter a level from 1 - 20.")

        except ValueError:
            print("Please enter a level from 1 - 20.")

    # Validate and format gender input
    sex = input("(M)ale or (F)emale? ")
    print("")
    while True:
        if sex.upper() == 'M' or sex.upper() == 'F':
            break
        else:
            sex = input("Please enter an M for male or an F for female.")
    if sex.upper() == 'M':
        sex = 'Male'
    if sex.upper() == 'F':
        sex = 'Female'

    # Array type validation
    char_type = input("Is this character (E)lite or (M)undane ")
    print("")
    while True:
        if char_type.upper() == 'M' or char_type.upper() == 'E':
            break
        else:
            char_type = input("Please enter an E for elite or an M for mundane ")
    print("Your character is now saved as ", char_name, " on your hard disk.")
    print("-----------------------------------------------------------------")
    print("")


    def mundane_array(char_name):
        """Rolling the mundane array"""
        ability_list = []
        with open(char_name, 'a') as f:
            print("Rolling 3d6 ten times....", file=f)
            print("--------------------------", file=f)
        for i in range(10):
            die_one = random.randint(1, 6)
            die_two = random.randint(1, 6)
            die_three = random.randint(1, 6)
            total = (die_one + die_two + die_three)
            with open(char_name, 'a') as f:
                print("Roll-", i + 1, ": ", die_one, die_two, die_three, "=", total, file=f)
            ability_list.append(total)
        with open(char_name, 'a') as f:
            print("--------------------------", file=f)
        return ability_list


    def elite_array(char_name):
        """Here is where we generate abilities for an elite character."""
        ability_list = []
        with open(char_name, 'a') as f:
            print("Rolling 3d6 twelve times....", file=f)
            print("----------------------------", file=f)
        for i in range(12):
            die_one = random.randint(1, 6)
            die_two = random.randint(1, 6)
            die_three = random.randint(1, 6)
            total = (die_one + die_two + die_three)
            with open(char_name, 'a') as f:
                print(i + 1, ":", die_one, die_two, die_three, "=", total, file=f)
            ability_list.append(total)
        with open(char_name, 'a') as f:
            print("-----------------------------", file=f)
        return ability_list


    # Choose what ability array to use
    if char_type.upper() == 'M':
        ability_list = mundane_array(char_name)

    if char_type.upper() == 'E':
        ability_list = elite_array(char_name)

    # Choose what class to use
    if job == 'Wizard':
        abilities = wizard.create_character(ability_list)
        wizard.format_sheet(race, sex, job, name, abilities, char_name, lvl)

    if job == 'Fighter':
        abilities = fighter.create_character(ability_list)
        fighter.format_sheet(race, sex, job, name, abilities, char_name, lvl)

    if job == 'Cleric':
        abilities = cleric.create_character(ability_list)
        cleric.format_sheet(race, sex, job, name, abilities, char_name, lvl)

    if job == 'Rogue':
        abilities = rogue.create_character(ability_list)
        rogue.format_sheet(race, sex, job, name, abilities, char_name, lvl)

    # Loop through the program until the user is finished
    rerun = input("Would you like to make another? Y/N ")
    while True:
        if rerun.upper() == 'Y' or rerun.upper() == 'N':
            break
        else:
            rerun = input("Please enter a Y or an N. ")
    if rerun.upper() == 'N':
        print("Thank You.")
        break
