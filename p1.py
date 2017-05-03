#! /usr/bin/env python3

from pr2 import *

def dfs(table, l, i = 0):
	if i >= len(table):
		# print_table(table, l, " ", "_")
		return True
	if table[i] != 0:
		return dfs(table, l, i + 1)
	for j in range(l * l):
		table[i] = j + 1
		if not validate(table, l, i):
			continue
		if dfs(table, l, i + 1):
			return True
	table[i] = 0
	return False


if __name__ == '__main__':
	(table, l) = get_input()

	print_table(table, l, " ", "_")
	print("")
	if dfs(table, l):
		print_table(table, l, " ", "_")
	else:
		print("Could not been filled.")
