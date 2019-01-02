# set is like a dictionary that only contains keys, size does not limit the speed of set operations
# there is no duplicates
# membership testing 
# set operations: 

my_set = {57, 'Mike', 200.0, (1,2,3)}

print(my_set)

# you can construct a set from a list, which will eliminate duplicate values
my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,11,12]
print(my_list)
new_set = set(my_list)

print(new_set)

# checking a value in the set returns a boolean value
print(1 in new_set)

# you can create a union of two sets with the | 
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
print("union of the sets {0}".format(set_1 | set_2))

# intersection of a set using &
print("intersection of a set {0}".format(set_1 & set_2))

# set difference with the -
print("set difference: {0}".format(set_1 - set_2))

# either of the sets but not in both
print("either of the sets but not in both {0}".format(set_1 ^ set_2))

# add 
print("Adding 10 to the set")
set_1.add(10)
print(set_1)

# discard
print("Removing 4 from the set")
set_1.discard(4)
print(set_1)

# pop - arbitrarily removes an item but not randomly
print("Popping an item from the set...")
removed_val = set_1.pop()
print("Removed {0} from the set_1".format(removed_val))
print(set_1)

# update a set from another set
print("Updating the set with a new value")
set_1.update(set_2)
print(set_1)

# difference_update
print("Difference update on the set")
set_1.difference_update(set_2)
print(set_1)

#forezenset - immutable set of a previous one
print("Freezing the set")
frozenSet = frozenset(set_1)
print(frozenSet)