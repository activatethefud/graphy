#!/bin/bash

1=1

for iterator in $(seq $1 $2); do
	echo -e "$iterator \c"

	for _ in $(seq $1 $(($2-1))); do
		echo -e "$(($RANDOM%$2)) \c"
	done

	echo ""
done
