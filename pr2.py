#! /usr/bin/env python3

import math

#print entire table
def print_table(table, l, e = "\t", line = "_______"):
	for i1 in range(l):
		if i1 > 0:
			for i2 in range((l + 1) * l - 1):
				print(line, end = e)
			print("")
		for i2 in range(l):
			for j in range(l):
				if j > 0:
					print("|", end = e) 
				for k in range(l):
					print([table[i1 * l * l * l + i2 * l * l + j * l + k], "."][table[i1 * l * l * l + i2 * l * l + j * l + k] == 0], end = e)
					# print(i1 * l * l * l + i2 * l * l + j * l + k, end = "\t")
			print("")

#return the index of the room in table
def get_index(coord, l):
	return coord[1] * l * l + coord[0]

#check if room assignment is valid or not
def validate(table, l, i):
	coord  = (i % (l * l), i // (l * l))
	for j in range(l * l):
		if (table[i] == table[get_index((j, coord[1]), l)] and i != get_index((j, coord[1]), l)) or\
		(table[i] == table[get_index((coord[0], j), l)] and i != get_index((coord[0], j), l)):
			return False
	square = ((coord[0] // l) * l, (coord[1] // l) * l)
	for j in range(l):
		for k in range(l):
			if(table[get_index((square[0] + j, square[1] + k), l)] == table[i] and i != get_index((square[0] + j, square[1] + k), l)):
				return False
	return True


#reading input from file
def get_input():
	rin = input().split(" ")
	rin[1] = rin[1][1:-1]
	l = int(math.sqrt(int(rin[0])))
	table = rin[1].split(",")
	for i in range(len(table)):
		table[i] = int(table[i])
	return (table, l)


#count empty rooms
def countEmptyRooms(table ,l) :

	emptyRoomsNumbers = 0;

	for i in range(len(table)) : 

		if table[i] == 0 :

			emptyRoomsNumbers += 1;

	return emptyRoomsNumbers;
