# dictionaries operations
my_dict = {'first': "John", 'last': "Smith"}

print(my_dict['first'])

# add a new value to the dictionary
my_dict['age'] = 23

print(my_dict)

# get has an optional default value, so if we attempt to access a key that does not exist we will get the default
print(my_dict.get('gender', "male"))

# keys that do not exist return None for the value
print(my_dict.get('gender'))

# removes the value with the specified key from the dictionary
print(my_dict.pop('age'))

# pop also has a default parameter
print(my_dict.pop('age', 100))

# setdefault works like get when the key exists
print(my_dict.setdefault('first', "Something Other than John"))

# adds a new value if the key does not exist
print(my_dict.setdefault('age', 54))
print(my_dict)

# tuples can be keys but lists cannot
my_dict[(54, "Adam", "Smith")] = "Superior person"
print(my_dict)

# keys can only exist once so this operation would overwrite the existing key
my_dict[(54, "Adam", "Smith")] = "Troubled person"
print(my_dict)
