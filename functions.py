def showSomeText(text):
    print("Here is the text I would like to display when this function is called {0}!".format(text))

def add(num1, num2):
    return num1 + num2

showSomeText("Johnathan")

print(add(3,6))

# functions can contain default values
def circle(center_x, center_y, radius = 10.0):
    pass

# builds a tuple from the values, means any number cna be added
def second_circle(center_x, center_y, radius, *extra_radii):
    pass

# builds a dictionary ** is for this
def another_circle(center_x, center_y, radius, *extra_radii, **attributes):
    pass

# annotate parameters
def last_circle(center_x: float, center_y: float, radius = 10.0, *extra_radii, **attributes):
    pass

def foo():
    return "Foo"