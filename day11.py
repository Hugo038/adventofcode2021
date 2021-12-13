import numpy as np

with open("inputs/day11.txt") as f:
    octopusses = np.array([[int(i) for i in line.strip()] for line in f])

def adj_finder(position):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, octopusses.shape[0])
            rangeY = range(0, octopusses.shape[1])
            (newX, newY) = (position[0] + dx, position[1] + dy)
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append([newX, newY])
    return adj

def flash(position):
    adj = adj_finder(position)
    for pos in adj:
        if octopusses[pos[0], pos[1]] > 0:
            octopusses[pos[0], pos[1]] += 1
    octopusses[position[0], position[1]] = -100000

def ans():
    flashes = 0
    for z in range(1,10000):
        for i in range(10):
            for j in range(10):
                octopusses[i, j] += 1
        while np.any(octopusses > 9):
            for i in range(10):
                for j in range(10):
                    if octopusses[i, j] > 9:
                        flash([i, j])
                        flashes+=1
        for i in range(10):
            for j in range(10):
                if octopusses[i, j] < 0:
                    octopusses[i,j] = 0
        if np.all(octopusses == 0):
            return z
    return flashes

print(ans())