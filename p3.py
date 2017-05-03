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

def solve(table, domains, primary_list, l, i = 0):
	if i >= len(table):
		return (True, set())

	if table[i] != 0:
		return solve(table, domains, primary_list, l, i + 1)

	conflict_list = set()
	for j in domains[i]:
		table[i] = j
		(had_conflict, local_conflict_list) = complete_validate(table, l, i)
		if not had_conflict:
			(child_is_ok, child_conflict_list) = solve(table, domains, primary_list, l, i + 1)
			if child_is_ok:
				return (True, set())
			else:
				# print(i, table[i], conflict_list, "Child CF: ", child_conflict_list, child_conflict_list.intersection(primary_list), " :")
				if len(child_conflict_list) > 0 and len(child_conflict_list.intersection(primary_list)) == 0 and i not in child_conflict_list:
					# print(i, table[i], conflict_list, "Child CF: ", child_conflict_list, child_conflict_list.intersection(primary_list))
					# print_table(table, l, " ", "_")
					table[i] = 0
					return (False, child_conflict_list)
		else:
			conflict_list = conflict_list.union(local_conflict_list)
	# print(i, table[i], "(%r)" % domains[i], conflict_list)
	# print_table(table, l, " ", "_")
	table[i] = 0
	return (False, conflict_list)

def make_domains(table, l):
	domains = []
	primary_list = set()
	for i in range(len(table)):
		if table[i] == 0:
			primary_list.add(i)
		domains.append(set())
		for j in range(l * l):
			domains[i].add(j + 1)
	for i in range(len(table)):
		if table[i] != 0:
			coord  = (i % (l * l), i // (l * l))
			for j in range(l * l):
				if get_index((j, coord[1]), l) != i and table[i] in domains[get_index((j, coord[1]), l)]:
					domains[get_index((j, coord[1]), l)].remove(table[i])
				if get_index((coord[0], j), l) != i and table[i] in domains[get_index((coord[0], j), l)]:
					domains[get_index((coord[0], j), l)].remove(table[i])
			square = ((coord[0] // l) * l, (coord[1] // l) * l)
			for j in range(l):
				for k in range(l):
					if get_index((square[0] + j, square[1] + k), l) != i and \
					table[i] in domains[get_index((square[0] + j, square[1] + k), l)]:
						domains[get_index((square[0] + j, square[1] + k), l)].remove(table[i])

	order_list = []
	for i in range(len(table)):
		order_list.append((i, len(domains[i])))

	order_list.sort(key=lambda x: x[1])

	return (domains, [x[0] for x in order_list], primary_list)

if __name__ == '__main__':
	(table, l) = get_input()

	print_table(table, l, " ", "_")
	print("")
	(domains, order_list, primary_list) = make_domains(table, l)
	if solve(table, domains, primary_list, l)[0]:
		print_table(table, l, " ", "_")
	else:
		print("Could not been filled.")
