#! /usr/bin/env python3

from pr2 import *

def complete_validate(table, l, i):
	coord  = (i % (l * l), i // (l * l))
	conflict_list = set()
	for j in range(l * l):
		if (table[i] == table[get_index((j, coord[1]), l)] and i != get_index((j, coord[1]), l)):
			conflict_list.add(get_index((j, coord[1]), l))
		if (table[i] == table[get_index((coord[0], j), l)] and i != get_index((coord[0], j), l)):
			conflict_list.add(get_index((coord[0], j), l))
	square = ((coord[0] // l) * l, (coord[1] // l) * l)
	for j in range(l):
		for k in range(l):
			if(table[get_index((square[0] + j, square[1] + k), l)] == table[i] and i != get_index((square[0] + j, square[1] + k), l)):
				conflict_list.add(get_index((square[0] + j, square[1] + k), l))
	return ((len(conflict_list) > 0), conflict_list)

def solve(table, l, i = 0):
	if i >= l * l * l * l:
		return (True, set())

	if table[i] != 0:
		return solve(table, l, i + 1)

	conflict_list = set()
	for j in range(l * l):
		table[i] = j + 1
		(had_conflict, local_conflict_list) = complete_validate(table, l, i)
		if not had_conflict:
			(child_is_ok, child_conflict_list) = solve(table, l, i + 1)
			if child_is_ok:
				return (True, set())
			else:
				if i not in child_conflict_list:
					print(i, table[i], conflict_list, "Child CF: ", child_conflict_list)
					print_table(table, l, " ", "_")
					table[i] = 0
					return (False, child_conflict_list)
		else:
			conflict_list = conflict_list.union(local_conflict_list)
	print(i, table[i], conflict_list)
	print_table(table, l, " ", "_")
	table[i] = 0
	return (False, conflict_list)

if __name__ == '__main__':
	(table, l) = get_input()

	print_table(table, l, " ", "_")
	print("")
	if solve(table, l)[0]:
		print_table(table, l, " ", "_")
	else:
		print("Could not been filled.")


