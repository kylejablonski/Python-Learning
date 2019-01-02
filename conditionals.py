print("Hello, World! This is a conditionals program test.")

# prompts for a value and checks if its more or less than 100
maxValue = int(input("Please enter a value: "))

if maxValue > 100:
    print("The max value of {0} is greater than 100!".format(maxValue))
elif maxValue < 100:
    print("The max value of {0} is less than 100!".format(maxValue))
else:
    print("Looks like the value you entered is not a max value!")

# grabs user input and using an expression to determine what to print
firstName = input("Now enter your first name: ")
firstName = firstName if firstName == 'Bill' else 'That was not a name'
print("Wow coolname, {0}".format(firstName))

if not len(firstName) > 10:
    print("that is a medium size name")
else:
    print("Whoa shorty, that name is not long.")
