# tuples are used to represent related values, like rows in a database
# immutable, cannot add or replace any sub values
my_tuple = (1,2,3)

print(my_tuple[0])

# will not work as you can't change the values in a typle
# my_tuple[0] = 10

# deconstruct the tuple
mikesAge, johnsAge, billAge = my_tuple

print("Mike is {0} years old".format(mikesAge))

# changing a tuple cannot be done so in order to update we must copy old values to new tuple with updated value
my_tuple2 = (10, my_tuple[-2], my_tuple[-1])

print(my_tuple2)