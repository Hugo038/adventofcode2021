import numpy as np

with open("inputs/day5.txt") as f:
    input = [(line.strip()) for line in f]
    input = [x.replace(' -> ', ',').split(',') for x in input]
    input_part_b = [[int(j) for j in i] for i in input]
    input_part_a = [x for x in input if x[0] == x[2] or x[1] == x[3]]

def determine_lines(lst):
    returnlist = []
    if lst[0] == lst[1] and lst[2] == lst[3]:
        if lst[3] < lst[1]:
            lst[0], lst[1], lst[2], lst[3] = lst[2], lst[3], lst[0], lst[1]
        for i in range(lst[1], (lst[3]+1)):
            returnlist.append((i, i))
    elif lst[0] == lst[2]:
        if lst[3]<lst[1]:
            lst[1], lst[3] = lst[3], lst[1]
        for i in range(lst[1], (lst[3]+1)):
            returnlist.append((lst[0], i))
    elif lst[1] == lst[3]:
        if lst[2]<lst[0]:
            lst[0], lst[2] = lst[2], lst[0]
        for i in range(lst[0], (lst[2]+1)):
            returnlist.append((i, lst[3]))
    else:
        if lst[0] > lst[2]:
            if lst[1] < lst[3]:
                for i in range(0, (lst[3]-lst[1])+1):
                    returnlist.append((lst[0]-i, lst[1]+i))
            if lst[1] > lst[3]:
                for i in range(0, (lst[1]-lst[3])+1):
                    returnlist.append((lst[0]-i, lst[1]-i))
        if lst[0] < lst[2]:
            if lst[1] < lst[3]:
                for i in range(0, (lst[3]-lst[1])+1):
                    returnlist.append((lst[0]+i, lst[1]+i))
            if lst[1] > lst[3]:
                for i in range(0, (lst[1]-lst[3])+1):
                    returnlist.append((lst[0]+i, lst[1]-i))



    return returnlist

def part1():
    gridsize = max([x for i in input_part_b for x in i])+1
    grid = np.zeros((gridsize,gridsize), dtype=int)
    for i in input_part_b:
        coordinates = determine_lines(i)
        print(i)
        print(coordinates)
        for x,y in coordinates:
            grid[x,y] += 1

    return np.count_nonzero(grid>1)


print(part1())

