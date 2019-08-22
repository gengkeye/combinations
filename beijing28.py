# pip install more-itertools
from itertools import combinations, permutations

def main(start, end, step):
    result = {}
    arr = []
    for i in combinations([i for i in range(start, end)], step):
        arr.append(list(i))

    for i in combinations(arr, 3):
        total = 0
        for j in i:
            total += sum(j) % 10

        if result.get(total):
            result[total] += 1
        else:
            result[total] = 1
    
    Sum = sum(result.values())
    for i in range(0, 28):
        print("%s %s" % (i, round(result[i] / Sum, 3)))

if __name__ == '__main__':
    main(1, 13, 6)

