############################################################ PART ONE ##########################################################
# Problem Link: https://adventofcode.com/2021/day/3

gamma_rate = 0
epsilon_rate = 0

zero_counter = []
one_counter = []

def binary_to_decimal(binary):
    temp = binary
    decimal, i, n = 0,0,0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary = binary // 10
        i += 1
    return decimal

with open("input.txt") as inputFileTxt:
    for line in inputFileTxt:
        digit = 1
        line = line.strip()
        for char in line:
            if int(char) == 1:
                if len(one_counter) >= digit:
                   one_counter[digit - 1] += 1
                else:
                    one_counter.append(1)
                    zero_counter.append(0)
            else:
                if len(zero_counter) >= digit:
                   zero_counter[digit - 1] += 1
                else:
                    zero_counter.append(1)
                    one_counter.append(0)
            digit += 1

gamma_binary = ''
epsilon_binary = ''
for index in range(0,len(zero_counter)):
    if(zero_counter[index] > one_counter[index]):
        gamma_binary += str(0)
        epsilon_binary += str(1)
    else:
        gamma_binary += str(1)
        epsilon_binary += str(0)

gamma_rate = binary_to_decimal(int(gamma_binary))
epsilon_rate = binary_to_decimal(int(epsilon_binary))

print("Power Consumpsion of the submarine is: " + str(gamma_rate * epsilon_rate))

############################################################ PART TWO ##########################################################
# Link to Problem : https://adventofcode.com/2021/day/3#part2

oxygen_generator_data = []
co2_scrubber_data = []

def get_from_bit_criteria(input_array, bit, is_most_common):
    zeros_data = []
    ones_data = []
    zero_counter = 0
    one_counter = 0
    for data in input_array:
        if(data[bit] == '1'):
            ones_data.append(data)
            one_counter += 1
        else:
            zeros_data.append(data)
            zero_counter += 1
    
    if is_most_common:
        if zero_counter > one_counter:
            input_array = zeros_data
        else:
            input_array = ones_data
    else:
        if zero_counter <= one_counter:
            input_array = zeros_data
        else:
            input_array = ones_data
    
    return input_array
    


with open("input.txt") as inputTextFile:
    for line in inputTextFile:
        oxygen_generator_data.append(line.strip())
        co2_scrubber_data.append(line.strip())

current_bit = 1
while(len(oxygen_generator_data) > 1):
    oxygen_generator_data = get_from_bit_criteria(oxygen_generator_data, current_bit - 1, True)
    current_bit += 1

current_bit = 1
while(len(co2_scrubber_data) > 1):
    co2_scrubber_data = get_from_bit_criteria(co2_scrubber_data, current_bit - 1, False)
    current_bit += 1


print("Life support Rating of the submarine is: " + str(binary_to_decimal(int(oxygen_generator_data[0])) * binary_to_decimal(int(co2_scrubber_data[0]))))