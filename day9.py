import numpy as np

with open("inputs/day9.txt") as f:
    input = np.array([[int(i) for i in line.strip()] for line in f])

def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def get_basin(i, j, m, n, checked, input_X):
    neighbours = (get_adjacent_indices(i,j,m,n))
    adjacent_indices_no_nines = [x for x in neighbours if input_X[x] == '0']
    for x in adjacent_indices_no_nines:
        if x not in checked:
            checked.append(x)
            get_basin(x[0], x[1], m, n, checked, input_X)
    return len(checked)



def part1():
    lengthx = len(input[0])
    lengthy = len(input)
    ans = 0
    for i in range(lengthx):
        for j in range(lengthy):
            neighbours = get_adjacent_indices(i, j, lengthx, lengthy)
            if all(input[i,j] < input[x] for x in neighbours):
                ans +=input[i,j]+1
    return ans

def part2():
    lengthx = len(input[0])
    lengthy = len(input)
    basins = []
    input_X = np.where(input==9, 'X', input)
    input_X = np.where(input<9, 0, input_X)
    for i in range(lengthx):
        for j in range(lengthy):
            if input_X[j,i] == '0':
                basins.append(get_basin(j,i,lengthy,lengthx,checked=[], input_X=input_X))
    return np.prod(sorted(list(set(basins)), reverse=True)[:3])

print(part1())
print(part2())