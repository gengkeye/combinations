# pip install more-itertools
from itertools import combinations, permutations

def main(start, end, step):
    result = {}
    arr = []
    for i in combinations([i for i in range(start, end)], step):
        arr.append(sum(i) % 10)

    for i in combinations(arr, 3):
        total = sum(i) 
        result[total] = result[total] + 1 if result.get(total) else 1
    
    Sum = sum(result.values())
    for i in range(0, 28):
        print("%s %s" % (i, round(result[i] / Sum, 3)))

if __name__ == '__main__':
    main(1, 13, 6)

