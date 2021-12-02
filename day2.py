with open("inputs/day2.txt") as f:
    directions = [(line.strip()).split(' ') for line in f]


def part1():
    x, y = 0, 0
    for i in directions:
        match i[0]:
            case 'forward':
                x += int(i[1])
        match i[0]:
            case 'down':
                y += int(i[1])
        match i[0]:
            case 'up':
                y -= int(i[1])
    return x * y


def part2():
    x, y, aim = 0, 0, 0
    for i in directions:
        match i[0]:
            case 'forward':
                x += int(i[1])
                y += aim * int(i[1])
        match i[0]:
            case 'down':
                aim += int(i[1])
        match i[0]:
            case 'up':
                aim -= int(i[1])
    return x * y


print(part1())
print(part2())