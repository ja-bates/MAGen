import random

import CalculatorTwo

# Loop a random amount of times between 10 and 50
loopMax = random.randint(10, 50)

# Print the amount of sequences requested
print("Request for " + str(loopMax) + " sequences received. Beginning Math...")

# Creating an operations list

operations = ["+"]

operations.append('-')
operations.append('*')
operations.append('/')

# Print the amount of operations being used

print("operation count " + str(len(operations)))

# Look at the different operations beings used

print("Calculations will consist of the following operations" + str(operations))

# Print three new lines

print('\n\n')

# This loop will loop LoopMax number of times
# Example: if LoopMax is 10 then Index would get these values sequentially: 0,1,2,3,4,5,6,7,8,9

for index in range(loopMax):
    # get random numbers to operate with
    num1 = random.randint(-99, 99)
    num2 = random.randint(-99, 99)

    print('calculation corresponding with ' + str(num1) + ' and ' + str(num2))

# Showing which operation is used in each calculation
    
    for operation in operations:
        print("operation used is " + operation)
        CalculatorTwo.runoperation(operation, num1, num2)
        print()  # new line

    print('\n')



