from collections import Counter

with open("inputs/day3.txt") as f:
    binary = [(line.strip()) for line in f]
    binary_string_list = [list(line) for line in binary]

def most_common(lst):
    if lst.count('1') < lst.count('0'):
        return '0'
    else:
        return '1'

def least_common(lst):
    if lst.count('1') < lst.count('0'):
        return '1'
    else:
        return '0'

def part1():
    zipped_list = (zip(*binary_string_list))
    gamma = []
    for i in zipped_list:
        x = most_common(list(i))
        gamma.append(x)
    gamma_bin = ''.join(gamma)
    epsilon_bin = ''.join(['1' if i == '0' else '0' for i in gamma])
    return int(gamma_bin, 2) * int(epsilon_bin, 2)

def part2(binary_oxy):
    binary_scrubber = binary_oxy[::]
    for i in range(50):
        zip_oxy = list(zip(*[line for line in binary_oxy]))
        binary_oxy = [x for x in binary_oxy if x[i] == most_common(zip_oxy[i])]
        if len(binary_oxy) == 1:
            break
    for i in range(50):
        zip_scrubber = list(zip(*[line for line in binary_scrubber]))
        binary_scrubber = [x for x in binary_scrubber if x[i] == least_common(zip_scrubber[i])]
        if len(binary_scrubber) == 1:
            break
    scrubber = ''.join(binary_scrubber[0])
    oxy = ''.join(binary_oxy[0])
    return int(oxy, 2) * int(scrubber, 2)

print(part1())
print(part2(binary))

