import csv
import random
times = 100
num = 1000000
language = 'Python'
sortName = 'HeapSort'
my_list = []
path = r'C:\Users\21604419\Documents\IT8x20\A1\Code\Data\random' + str(times) + '_' + str(num) + '.csv'
resultpath = r'C:\Users\21604419\Documents\IT8x20\A1\Code\Data\Result.csv'

with open(path, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=','))
    f.close()


def swap(i, j):
    sqc[i], sqc[j] = sqc[j], sqc[i]


def heapify(end, i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    max = i
    if l < end and sqc[i] < sqc[l]:
        max = l
    if r < end and sqc[max] < sqc[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)


def heapsort():
    end = len(sqc)
    start = end // 2 - 1  # use // instead of /
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)
sqc = data


def repeat_fun(times, f):
    for i in range(times): f()


def do():
    from datetime import datetime
    tstart = datetime.now()
    heapsort()
    tend = datetime.now()
    delta = tend - tstart
    my_list.append(delta.microseconds / 1000)


repeat_fun(times, do)

from statistics import mean,pstdev,pvariance

print('Heap Sort:\nMean: ' + str(mean(my_list)) + '\nVariance: ' + str(pvariance(my_list)) + '\nStandard Deviation: ' + str(pstdev(my_list)))


with open(resultpath, 'a',newline='') as rp:
    a = csv.writer(rp, delimiter=',', lineterminator='\n')
    result = [[num, times, language, sortName, str(mean(my_list)), str(pvariance(my_list)), str(pstdev(my_list))]]
    a.writerows(result)
    rp.close()
