with open("inputs/day8.txt") as f:
    input = [(line.strip()).split(' ') for line in f]
    input = [(l[:10], l[11:]) for l in input]

def part1():
    ans = 0
    for i in input:
        ans += len([x for x in i[1] if len(x) in {2,3,4,7}])
    return ans

def decypher(line):
    input, output = line[0], line[1]
    sum_input_freqs = []
    input_long_str = ''.join([str(x) for x in input])
    char_count_dict = {i: str(input_long_str.count(i)) for i in 'abcdefg'}
    for i in input:
        b = ''.join([char_count_dict[j] for j in i])
        sum_input_freqs.append(sum(int(digit) for digit in str(b)))
    freq_to_number = {42: 0, 17: 1, 34: 2, 39: 3, 30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9}
    sum_output_freqs = []
    for i in output:
        b = ''.join([char_count_dict[j] for j in i])
        sum_output_freqs.append(sum(int(digit) for digit in str(b)))
    return int(''.join([str(freq_to_number[i]) for i in sum_output_freqs]))

def part2():
    return sum([decypher(i) for i in input])

print(part1())
print(part2())
