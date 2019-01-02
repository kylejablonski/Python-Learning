print ("Hello, World!")

# simple calculations
billAmount = 35
tipPercentage = [.20, .18, .15, .10, .05]

tipAmount = (tipPercentage[0] * billAmount)
finalBill = billAmount + tipAmount

# Template practice
outputFormat = "Most people tip {0} that would be {1} for {2} which totals {3}"
print (outputFormat.format(tipPercentage[0], tipAmount, billAmount, finalBill))

# split a string
outputList = outputFormat.split()
print(outputList)
outputList = outputFormat.split("{")
print(outputList)

# length of a string
print(len(outputFormat))


