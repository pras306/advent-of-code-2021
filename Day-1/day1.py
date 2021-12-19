
############################################################ PART ONE ##########################################################
# Link to Problem : https://adventofcode.com/2021/day/1
# Open input file and read each line till end of file and count whether the current line value is greater than the previous one

prev_value = None
increment_counter = 0
with open("input.txt") as inputTxtFile:
    for line in inputTxtFile:
        if prev_value is not None and (int(line) > prev_value):
            increment_counter += 1
        
        prev_value = int(line)

print("Total number of times depth increased: " + str(increment_counter))

############################################################ PART TWO ##########################################################
# Link to Problem : https://adventofcode.com/2021/day/1#part2
prev_window_sum = None
increment_counter = 0
window_length = 3
window = []
current_window_sum = 0
counter = 0

with open("input.txt") as inputTextFile:
    for line in inputTextFile:
        counter += 1
        if len(window) < window_length:
            window.append(int(line))
            current_window_sum += int(line)
        
        if len(window) == window_length:
            if prev_window_sum is not None and current_window_sum > prev_window_sum:
                increment_counter += 1
            
            prev_window_sum = current_window_sum
            current_window_sum -= window.pop(0)

            window.append(int(line))
            current_window_sum += int(line)

if current_window_sum > prev_window_sum:
    increment_counter += 1

print("Total number of times sums increased: " + str(increment_counter))
