from pr2 import *


emptyRoomsNumbers = CountEmptyRooms(table ,l);

def A_Star(table, l ,emptyRoomsNumbers) :

	if emptyRoomsNumbers == 0 :

		return True;

	index = 0;
	#huresticValue = infinite;

	for j in range(len(table)) :

		if table[j] == 0 : 

			temp = calcHurestic(table ,l ,j);
			if(temp < huresticValue):

				index = j;
				huresticValue = temp;

	emptyRoomsNumbers--;

	for j in range(l * l) : 

		table[index] = j+1;

		if not validate(table ,l ,index) :

			-continue;

		if A_Star(table ,l ,emptyRoomsNumbers) :

			return True;

	table[index] = 0;
	return False;