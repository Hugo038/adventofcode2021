def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open("inputs/day4.txt") as f:
    data = [line.strip().split(',') for line in f]
    data = [line for line in data if line != ['']]
    bingo_numbers = [int(x) for x in data[0]]
    boards = data[1:]
    boards_flattened = [x for i in boards for x in i]
    boards_flattened = [x.replace('  ', ' ').replace(' ', ',') for x in boards_flattened]
    boards_list = [int(x) for x in ','.join(boards_flattened).split(',')]
    boards = [i for i in divide_chunks(boards_list, 25)]

def check_bingo(board):
    combinations = [[0, 5, 10, 15, 20],
                    [1, 6, 11, 16, 21],
                    [2, 7, 12, 17, 22],
                    [3, 8, 13, 18, 23],
                    [4, 9, 14, 19, 24],
                    [0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9],
                    [10, 11, 12, 13, 14],
                    [15, 16, 17, 18, 19],
                    [20, 21, 22, 23, 24]]
    for i in combinations:
        sum_row = [board[j] for j in i]
        if sum([board[j] for j in i]) == 500:
            return 'Bingo'

def part1():
    for number in bingo_numbers:
        for b in range(len(boards)):
            boards[b] = [100 if x == number else x for x in boards[b]]
            if check_bingo(boards[b]) == 'Bingo':
                bingoboard = boards[b]
                final_number = number
                break
            else:
                continue
            break
        else:
            continue
        break
    bingo_board_clean = [x for x in bingoboard if x!=100]
    return sum(bingo_board_clean) * final_number

def part2(boards):
    bingo_boards = []
    for number in bingo_numbers:
        for b in range(len(boards)):
            boards[b] = [100 if x == number else x for x in boards[b]]
            if check_bingo(boards[b]) == 'Bingo':
                bingo_boards.append(boards[b])
        boards = [x for x in boards if x not in bingo_boards]
        if len(boards) == 1:
            last_board = boards[0]
            break
        else:
            continue
    for number in bingo_numbers:
        last_board = [100 if x == number else x for x in last_board]
        if check_bingo(last_board) == 'Bingo':
            last_number = number
            break
        else:
            continue
    bingo_board_clean = [x for x in last_board if x!=100]
    return sum(bingo_board_clean) * last_number


print(part2(boards))




