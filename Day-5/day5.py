############################################################ PART ONE AND PART TWO ##########################################################
# Problem Link: https://adventofcode.com/2021/day/5
# Problem Link: https://adventofcode.com/2021/day/5/#part2

matching_coordinates = []
diagonal_coordinates = []
max_coord = 0

with open("input.txt") as inputTxtFile:
    for line in inputTxtFile:
        line = line.strip()
        line_array = line.split(",")
        x1_coord = int(line_array[0])
        y2_coord = int(line_array[2])
        line_array = line_array[1].split('->')
        y1_coord = int(line_array[0])
        x2_coord = int(line_array[1])
        
        if(x1_coord == x2_coord or y1_coord == y2_coord):
            if(x1_coord > max_coord):
                max_coord = x1_coord
            if(y1_coord > max_coord):
                max_coord = y1_coord
            if(x2_coord > max_coord):
                max_coord = x2_coord
            if(y2_coord > max_coord):
                max_coord = y2_coord
            matching_coordinates.append({ 'start': [x1_coord, y1_coord], 'end': [x2_coord, y2_coord] })
        
        if(abs(x1_coord - x2_coord) == abs(y1_coord - y2_coord)):
            diagonal_coordinates.append({ 'start': [x1_coord, y1_coord], 'end': [x2_coord, y2_coord] })


line_diagram = [[0] * (max_coord + 1) for _ in range(max_coord + 1)]

for coord in matching_coordinates:
    x1, y1 = coord['start']
    x2, y2 = coord['end']

    range_start, range_end = 0, 0
    common_coord = 0

    if x1 == x2:
        common_coord = x1
        if y1 < y2:
            range_start = y1
            range_end = y2
        else:
            range_start = y2
            range_end = y1
        
        for num in range(range_start, range_end + 1):
            line_diagram[num][common_coord] += 1
    else:
        common_coord = y1
        if x1 < x2:
            range_start = x1
            range_end = x2
        else:
            range_start = x2
            range_end = x1
        
        for num in range(range_start, range_end + 1):
            line_diagram[common_coord][num] += 1

for coord in diagonal_coordinates:
    x1, y1 = coord['start']
    x2, y2 = coord['end']

    x_step = 1 if x2 > x1 else -1
    y_step = 1 if y2 > y1 else -1

    x_coords = []
    y_coords = []

    for x in range(x1, x2 + x_step, x_step):
        x_coords.append(x)

    for y in range(y1, y2 + y_step, y_step):
        y_coords.append(y)

    for coords in range(0, len(x_coords)):
        line_diagram[y_coords[coords]][x_coords[coords]] += 1


overlap_counter = 0

for row in range(0, max_coord + 1):
    for col in range(0, max_coord + 1):
        if(line_diagram[row][col] >= 2):
            overlap_counter += 1

print(overlap_counter)