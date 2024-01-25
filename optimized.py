#!/usr/bin/env python3

import csv
import sys

def bubble_sort(a):
	update=True
	n=len(a)
	while(update==True and n>1):
		update = False
		for i in range(len(a)-1):
			if a[i]>a[i+1]:
				a[i],a[i+1]=a[i+1],a[i]
				update = True
		n-=1
	return a


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} inputfile".format(sys.argv[0]))
        sys.exit(1)

    input_filename = sys.argv[1]

    with open(input_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        input_list = [row for row in csvreader]

    bubble_sort(input_list)

    for row in input_list:
        print(','.join(row))
