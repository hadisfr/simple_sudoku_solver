#! /usr/bin/env python3

from pr2 import *

def A_Star(table, l ,emptyRoomsNumbers) :

	if emptyRoomsNumbers == 0 :

		return True;

	index = 0;
	huresticValue = l * l + 1; # infinite

	for j in range(len(table)) :

		if table[j] == 0 : 

			temp = calcHurestic(table ,l ,j);
			if(temp < huresticValue):

				index = j;
				huresticValue = temp;

	emptyRoomsNumbers -= 1;

	for j in range(l * l) : 

		table[index] = j+1;

		if not validate(table ,l ,index) :

			continue;

		if A_Star(table ,l ,emptyRoomsNumbers) :

			return True;

	table[index] = 0;
	return False;

if __name__ == '__main__':
	(table, l) = get_input()

	print_table(table, l, " ", "_")
	print("")
	if A_Star(table, l, countEmptyRooms(table, l)):
		print_table(table, l, " ", "_")
	else:
		print("Could not been filled.")

