import csv
import random
times = 50
num = 10000
language = 'Python'
sortName = 'MergeSort'
my_list = []
path = r'C:\Users\21604419\Documents\IT8x20\A1\Code\Data\random' + str(times) + '_' + str(num) + '.csv'
resultpath = r'C:\Users\21604419\Documents\IT8x20\A1\Code\Data\Result.csv'

with open(path, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=','))
    f.close()


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def repeat_fun(times, f):
    for i in range(times): f()


def do():
    from datetime import datetime
    tstart = datetime.now()
    mergeSort(data)
    tend = datetime.now()
    delta = tend - tstart
    my_list.append(delta.microseconds / 1000)


repeat_fun(times, do)

from statistics import mean,pstdev,pvariance

print ('Merge Sort:\nMean: ' + str(mean(my_list)) + '\nVariance: ' + str(pvariance(my_list)) + '\nStandard Deviation: ' + str(pstdev(my_list)))

with open(resultpath, 'a',newline='') as rp:
    a = csv.writer(rp, delimiter=',', lineterminator='\n')
    result = [[num, times, language, sortName, str(mean(my_list)), str(pvariance(my_list)), str(pstdev(my_list))]]
    print(result)
    a.writerows(result)
    rp.close()
