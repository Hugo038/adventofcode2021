with open("inputs/day1.txt") as f:
    data = [int(line.strip()) for line in f]

def part1():
    pairs = zip(data[:-1], data[1:])
    return len([i for i,j in pairs if j > i])

def part2():
    trips = zip(data[:-2], data[1:-1], data[2:])
    sums = [(i+j+k) for i, j, k in trips]
    sumszip = zip(sums[:-1], sums[1:])
    return len([i for i, j in sumszip if j > i])

print(part1())
print(part2())








