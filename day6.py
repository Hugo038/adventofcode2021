with open("inputs/day6.txt") as f:
    data = [int(x) for x in list(f)[0].split(',')]

def initialise_dict(lst):
    fishes_list = []
    for i in range(0,10):
        fishes_list.append(lst.count(i))
    return fishes_list

def rotate(l, n):
    return l[n:] + l[:n]

def answer(n):
    fishes = initialise_dict(data)
    for i in range(1,n+1):
        fishes = rotate(fishes, 1)
        if fishes[9]>0:
            fishes[6] += fishes[9]
            fishes[8] += fishes[9]
            fishes[9] = 0
    return sum([x for x in fishes[:9]])

print(answer(256))


