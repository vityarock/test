#!/usr/bin/env python3
# query_count = int(input())
# print(query_count)
# query_list = []
# for item in range(query_count):
# 	query_list.append(input())
# print(query_list)
space_dict = dict()

def create_space(master, slave):
	print("create_space", slave, "in", master)
	if master not in space_dict:
		space_dict[master] = {slave: None}
		print(space_dict)
		

def	add_var(namespace, variable):
	print ("add_var", variable, "in", namespace)
def get_query():
	pass

query_list = ['add global a', 'create foo global', 'create bar foo']
query = query_list.pop(0).split()
arg1 = query[1]
arg2 = query[2]
if query[0] == "create":
	master, slave = arg1, arg2
	create_space(master, slave)
elif query[0] == "add":
	namespace, variable = arg1, arg2
	add_var(namespace, variable)


# print(query)
# print(query_list)
parent = []
#query_input = map(str, input().split())

