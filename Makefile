.PHONY: all clean

all: sort1 sort2 experiment

sort1: bubble_sort.py
	echo '#!/usr/bin/env python3' > sort1
	cat bubble_sort.py >> sort1
	chmod +x sort1

sort2: optimized.py
	echo '#!/usr/bin/env python3' > sort2
	cat optimized.py >> sort2
	chmod +x sort2

experiment: experiment.py
	echo '#!/usr/bin/env python3' > experiment
	cat experiment.py >> experiment
	chmod +x experiment


clean:
	rm -f sort1 sort2 experiment