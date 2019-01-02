# loop over a list
print("Lists")
digits = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in digits:
    print("Item {0}".format(i))

# loop over a dictionary
print("Dictionaries")
titles = {'president': "Bill", 'vice_president': "Mike", 'secrectary':"Jason", 'engineer_1':"Kyle"}

for title in titles:
    print(title) # prints only the keys

for title in titles:
    print(titles.get(title)) # use the keys to get the values


# for a set lets print it
print("Sets")
random_set = (1,4,2,5,3,2,7,9,86,6,5)

for rando in random_set:
    print(rando)


# use range function to loop to a number
print("Up to using range and lists")
for item in range(20):
    print(item)


# for loop to print all options for a tip :number means add padding of `number` spaces
billAmount = 100
tipPercentage = [.20, .18, .15, .10, .05]
tipTemplate = "{0:4}% -> ${1:4}"
for i in tipPercentage:
    print (tipTemplate.format(i * 100, i * billAmount))

# loop with if else
oneThroughTen = [1,2,3,4,5,6,7,8,9,10]
for b in oneThroughTen:
    if(b % 2 == 0): 
        print("even {0}".format(b))
    else:
        print("odd {0}".format(b))

# while loops

hasHitLimit = False
counter = 0
while not hasHitLimit:
    print("Not after 5!")
    counter += 1
    if(counter > 5):
        hasHitLimit = True

print("Ended while")

# continue
for i in range(10):
    if i % 2:
        continue
    print("For {0}".format(i))

# break
for i in range (100):
    if i * i > 500:
        break
    print("For {0}".format(i * i))

# pass (does nothing or takes up space that was otherwise blank)
for i in range (10):
    pass

if 10 < 12:
    pass

while False:
    pass

