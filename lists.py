# list practice
namesList = []

# add names to the list
namesList.append("Matthew")
namesList.append("Mark")
namesList.append("Luke")
namesList.append("John")

print("the list of names has lenght = {0}, with values: {1}".format(len(namesList), namesList))

print("Removing the name 'Mathew' from namesList:")
firstName = namesList.pop(0)
print("Removed: {0} from namesList!".format(firstName))
print(namesList)

# we can access elements with negative index by starting from the end of the list
print(namesList[-1])

# we can also combine two lists
namesList2 = ["William", "Benjamin", "Arthur", "Julias", "Bartholemew"]
namesList.extend(namesList2)
print(namesList)

for index in range(25):
    print("Item {0}".format(index))