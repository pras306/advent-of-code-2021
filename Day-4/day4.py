############################################################ PART ONE ##########################################################
# Problem Link: https://adventofcode.com/2021/day/4

bingo_called_numbers = []
bingo_boards = []

with open("input.txt") as inputTextFile:
    new_board = []
    for line in inputTextFile:
        line = line.strip()

        if(line.find(",") > 0):
            bingo_called_numbers = line.split(",")
            continue

        if(len(line) == 0):
            if(len(new_board) == 0):
                continue
            bingo_boards.append(new_board)
            new_board = []
            continue

        line_array = line.split(" ")
        board_row = []
        for num in line_array:
            if(len(num) == 0):
                continue
            board_row.append(int(num))
        
        new_board.append(board_row)
    
    bingo_boards.append(new_board)

def game_round(called_number, board):
    number_of_rows = len(bingo_boards[board])
    number_of_columns = len(bingo_boards[board][0])

    for row in range(0, number_of_rows):
        for col in range(0, number_of_columns):
            if(int(called_number) == bingo_boards[board][row][col]):
                # print('3:', called_number, bingo_boards[board][row][col])
                bingo_boards[board][row][col] = 'B'
    
    for row in range(0, number_of_columns):
        bingo_count = bingo_boards[board][row].count('B')
        if(bingo_count == number_of_columns):
            # print("bingo row check")
            return True
    
    for col in range(0, number_of_columns):
        bingo_count = 0
        for row in range(0, number_of_rows):
            if(bingo_boards[board][row][col] == 'B'):
                bingo_count += 1
        
        if(bingo_count == number_of_rows):
            # print("bingo col check")
            return True

    # bingo_diagonal = 0
    # bingo_reverse_diagonal = 0
    # for num in range(0, number_of_rows):
    #     if(bingo_boards[board][num][num] == 'B'):
    #         bingo_diagonal += 1
        
    #     if(bingo_boards[board][number_of_rows - 1 - num][num] == 'B'):
    #         bingo_reverse_diagonal += 1
    
    # if(bingo_diagonal == number_of_rows):
    #     print("bingo diagonal check")
    #     return True
    
    # if(bingo_reverse_diagonal == number_of_rows):
    #     print("bingo reverse diagonal check")
    #     return True
    
    return False



number_index = 0
bingo = False
all_boards_checked = False
winner_board = []
winning_number = None
winnin_board_num = 0

while (not bingo and not all_boards_checked):
    for board_num in range(0, len(bingo_boards)):
        bingo = game_round(bingo_called_numbers[number_index], board_num)        
        if(bingo):
            winner_board = bingo_boards[board_num]
            winning_number = bingo_called_numbers[number_index]
            winnin_board_num = board_num
            break

    number_index += 1

    if(number_index == len(bingo_called_numbers) - 1):
        all_boards_checked = True

sum_unmarked_numbers = 0

for row in range(0, len(winner_board)):
    for col in range(0, len(winner_board[0])):
        if(winner_board[row][col] != 'B'):
            sum_unmarked_numbers += winner_board[row][col]

final_score = sum_unmarked_numbers * int(winning_number)

# # print(bingo_boards)
# print(winnin_board_num)
# print(winner_board)
# print(winning_number)
print(final_score)

############################################################ PART TWO ##########################################################
# Link to Problem : https://adventofcode.com/2021/day/4#part2


number_index = 0
bingo = False
all_boards_checked = False
loser_board = []
boards_won = []
losing_number = None
losing_board_num = 0

while (not bingo and not all_boards_checked):
    for board_num in range(0, len(bingo_boards)):
        if(board_num in boards_won):
            continue
        bingo = game_round(bingo_called_numbers[number_index], board_num)        
        if(bingo):
            losing_number = bingo_called_numbers[number_index]
            losing_board_num = board_num            
            boards_won.append(board_num)
            if (len(bingo_boards) != len(boards_won)):
                bingo = False

    number_index += 1

    if(number_index == len(bingo_called_numbers) - 1):
        all_boards_checked = True

sum_unmarked_numbers = 0
loser_board = bingo_boards[boards_won[len(boards_won) - 1]]

for row in range(0, len(loser_board)):
    for col in range(0, len(loser_board[0])):
        if(loser_board[row][col] != 'B'):
            sum_unmarked_numbers += loser_board[row][col]

final_score = sum_unmarked_numbers * int(losing_number)

# print(bingo_boards)
# print(losing_board_num)
# print(loser_board)
# print(losing_number)
print(final_score)