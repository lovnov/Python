import csv
import random
times = 50
num = 10000
language = 'Python'
sortName = 'QuickSort'
my_list = []
path = r'C:\Users\21604419\Documents\IT8x20\A1\Code\Data\random' + str(times) + '_' + str(num) + '.csv'
resultpath = r'C:\Users\21604419\Documents\IT8x20\A1\Code\Data\Result.csv'

with open(path, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=','))
    f.close()


def quicksort(alist):
    quicksortHelper(alist, 0, len(alist) - 1)


def quicksortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quicksortHelper(alist, first, splitpoint - 1)
        quicksortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark



def _quicksort(aList, first, last):
    if first < last:
        pivot = partition(aList, first, last)
        _quicksort(aList, first, pivot - 1)
        _quicksort(aList, pivot + 1, last)


def partition(aList, first, last):
    pivot = first + random.randrange(last - first + 1)
    swap(aList, pivot, last)
    for i in range(first, last):
        if aList[i] <= aList[last]:
            swap(aList, i, first)
            first += 1
    swap(aList, first, last)
    return first


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]


def repeatfunc(times, f):  ##Define repeat function method
    for i in range(times): f()


def func():
    from datetime import datetime
    tstart = datetime.now()
    quicksort(data)
    tend = datetime.now()
    delta = tend - tstart
    my_list.append(delta.microseconds / 1000)  ##Change Microseconds to Milliseconds by /1000


repeatfunc(times, func)  ##Call repeatFunc to loop the sorting function to a number of times

from statistics import mean,pstdev,pvariance
##Work out the mean, variance and standard Deviation
print('Quick Sort:\nMean: ' + str(mean(my_list)) + '\nVariance: ' + str(pvariance(my_list)) + '\nStandard Deviation: ' + str(pstdev(my_list)))


with open(resultpath, 'a') as rp:
    a = csv.writer(rp, delimiter=',', lineterminator='\n')
    result = [[num, times, language, sortName, str(mean(my_list)), str(pvariance(my_list)), str(pstdev(my_list))]]
    a.writerows(result)
    rp.close()