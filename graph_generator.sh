#!/bin/bash

for iterator in $(seq 1 $1); do
	echo -e "$iterator\c"

	for _ in $(seq 1 $(($1-1))); do
		echo -e " $(($RANDOM%$1+1))\c"
	done

	echo ""
done

# Example output to pipe to input.txt
# 1 5 3 3 8 6 6 0 4 7 
# 2 1 9 8 3 2 1 1 2 4 
# 3 4 9 7 6 6 4 8 8 0 
# 4 9 0 7 7 4 1 3 4 0 
# 5 9 6 1 9 6 5 8 2 7 
# 6 4 4 0 4 5 5 1 0 4 
# 7 0 1 9 4 1 7 1 6 5 
# 8 3 8 4 7 9 8 9 0 0 
# 9 5 7 9 0 0 4 9 7 2 
# 10 2 6 0 7 5 0 9 1 7 
