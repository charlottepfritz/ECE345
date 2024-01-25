
#!/usr/bin/env python3

import csv
import sys

def partition(array, low, high):

    pivot = array[high]
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} inputfile".format(sys.argv[0]))
        sys.exit(1)

    input_filename = sys.argv[1]

    with open(input_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        input_list = [row for row in csvreader]

    quickSort(input_list,0,len(input_list)-1)

    for row in input_list:
        print(','.join(row))


