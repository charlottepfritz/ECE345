.PHONY: all clean

all: sort1 sort2 sort3 optimized experiment

sort1: bubble_sort.py
	echo '#!/usr/bin/env python3' > sort1
	cat bubble_sort.py >> sort1
	chmod +x sort1

sort2: quick_sort.py
	echo '#!/usr/bin/env python3' > sort2
	cat sort2.py >> sort2
	chmod +x sort2

sort3: merge_sort.py
	echo '#!/usr/bin/env python3' > sort3
	cat sort3.py >> sort2
	chmod +x sort3

optimized: optimized.py
	echo '#!/usr/bin/env python3' > optimized
	cat optimized.py >> sort2
	chmod +x optimized

experiment: experiment.py
	echo '#!/usr/bin/env python3' > experiment
	cat experiment.py >> experiment
	chmod +x experiment

clean:
	rm -f sort1 sort2 experiment