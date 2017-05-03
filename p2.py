from pr2 import *

pathCost = 0;
emptyRoomsNumbers = CountEmptyRooms(table ,l ,i = 0);

def A_Star(table, l ,emptyRoomsNumbers ,pathCost = 0) :

	if emptyRoomsNumbers == 0 :

		return True;

	index = 0;

	for j in range(len(table)) :

		if table[j] == 0 : 

			#use calcHurestic function to calculate hurestic amount and save the index of this room in index variable

	emptyRoomsNumbers--;
	pathCost++;

	for j in range(len(table)) : 

		table[index] = j+1;

		if not validate(table ,l ,index) :

			-continue;

		if A_Star(table ,l ,emptyRoomsNumbers ,pathCost) :

			return True;

	table[index] = 0;
	return False;