.PHONY: all clean

all: sort1 sort2 sort3 experiment

sort1: bubble_sort.py
	echo '#!/usr/bin/env python3' > sort1
	type bubble_sort.py >> sort1

sort2: quick_sort.py
	echo '#!/usr/bin/env python3' > sort2
	type quick_sort.py >> sort2

sort3: merge_sort.py
	echo '#!/usr/bin/env python3' > sort3
	type merge_sort.py >> sort3

experiment: experiment.py
	echo '#!/usr/bin/env python3' > experiment
	type experiment.py >> experiment

clean:
	del sort1 sort2 sort3 experiment