import math

with open("inputs/day7.txt") as f:
    crabs = [int(x) for x in list(f)[0].split(',')]

def determine_fuel(lst):
    lowest_fuel = math.inf
    for i in range(0, max(lst)//2):
        fuel = sum([abs(x-i) for x in lst])
        if fuel<lowest_fuel:
            lowest_fuel = fuel
    return lowest_fuel

def determine_fuel_2(lst):
    lowest_fuel = math.inf
    for i in range(0, max(lst)//2):
        fuel = sum([(abs(x-i)*(abs(x-i)+1)//2) for x in lst])
        if fuel<lowest_fuel:
            lowest_fuel = fuel
    return lowest_fuel


def part1():
    return determine_fuel(crabs)

def part2():
    return determine_fuel_2(crabs)

print(part1())
print(part2())
