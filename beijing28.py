# pip install more-itertools
from itertools import combinations, permutations
import datetime

def main(start, end, step):
    starttime = datetime.datetime.now()
    result = {}
    arr = []
    for i in combinations([i for i in range(start, end)], step):
        arr.append(sum(i) % 10)

    for i in combinations(arr, 3):
        total = sum(i) 
        result[total] = result[total] + 1 if result.get(total) else 1
    
    Sum = sum(result.values())
    print("和值   概率\n--------------------\n")
    for i in range(0, 28):
        print("%2s    %s" % (i, round(result[i] / Sum, 3)))

    endtime = datetime.datetime.now()

    print("\n--------------------\n执行完毕，共耗时：%ss" % (endtime - starttime).seconds)

if __name__ == '__main__':
    main(1, 10, 6)

