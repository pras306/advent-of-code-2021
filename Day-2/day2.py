############################################################ PART ONE ##########################################################
# Problem Link: https://adventofcode.com/2021/day/2

horizontal_pos = 0
depth = 0

with open("input.txt") as inputTextFile:
    for line in inputTextFile:
        command, unit = line.split()

        if command == "forward":
            horizontal_pos += int(unit)
        elif command == "down":
            depth += int(unit)
        else:
            depth -= int(unit)

print("Final value is " + str(horizontal_pos * depth))

############################################################ PART TWO ##########################################################
# Link to Problem : https://adventofcode.com/2021/day/2#part2

horizontal_pos = 0
depth = 0
aim = 0

with open("input.txt") as inputTextFile:
    for line in inputTextFile:
        command, unit = line.split()

        if command == "forward":
            horizontal_pos += int(unit)
            depth += aim * int(unit)
        elif command == "down":
            aim += int(unit)
        else:
            aim -= int(unit)

print("Final value is " + str(horizontal_pos * depth))