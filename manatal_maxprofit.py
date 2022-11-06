#Find the start and end indices that give you the max profit
#for example:
#given [-1 9 0 8 -5 6 -24]
#result will be [1,5]
#constrains: 6 seconds, 512mb of memory
import os, psutil
import random
import time

from hurry.filesize import size


def maxprofit(d):
    size = len(d)
    start = end = 0
    max1 = sum(d)
    i = 0
    while i < size-1:
        sub_data1 = d[i::]
        if sum(sub_data1) > max1:
            max1 = sum(sub_data1)
            start = i
        i += 1
    max_profit = sum(d[i::])
    j = size
    while j > start+1:
        sub_data2 = d[start:j:]
        if sum(sub_data2) > max_profit:
            end = j-1
            max_profit = sum(sub_data2)
        j -= 1
    return [start, end]

def main():
    # pylint: disable = C, W
    # n = int(input())
    # ts = [int(i) for i in input().split()]
    # data = [-1, 9, 0, 8, -5, 6, -24]
    # data = [-722, 713, 83, -285, -39, 860, -505, -775, -389, 584]
    data = []
    for i in range(10000):
        data.append(random.randint(-100, 100))
    # with redirect_stdout(sys.stderr):
    print(data)
    st = time.time()
    process = psutil.Process(os.getpid())
    solution = maxprofit(data)
    et = time.time()
    print(solution)
    print(size(process.memory_info().rss))
    print(et - st)


if __name__ == "__main__":
    main()
