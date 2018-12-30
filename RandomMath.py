import random

# Easy as this to call code from the same directory
# Note that in CalculatorTwo the main function was altered to be called conditionally
import CalculatorTwo

# Loop a random amount of times between 10 and 50
loopMax = random.randint(10, 50)

# Print the amount of sequences requested
print("Request for " + str(loopMax) + " sequences received. Beginning Math...")

# Creating Lists IMPORTANT
# give me a list named operations that has 1 element in it that is the string plus sign
# empty list would be operatoins = [] also commas to add more elements

operations = ["+"]

# dot operation calls a function to something else
# something 'in this case minus' is being added by the append function to the list 'operations'

operations.append('-')
operations.append('*')
operations.append('/')

# len function returns the amount of things in our list AS AN INTEGER

print("operation count " + str(len(operations)))

# Look at the different operations beings used

print("Calculations will consist of the following operations" + str(operations))

# \n is the string representation of a new line
# the print function also creates its own new line upon use
# This code prints (3) new lines

print('\n\n')

# This loop will loop LoopMax number of times
# Example: if LoopMax is 10 then Index would get these values sequentially: 0,1,2,3,4,5,6,7,8,9

for index in range(loopMax):
    # get random numbers to operate with
    num1 = random.randint(-99, 99)
    num2 = random.randint(-99, 99)

    print('calculation corresponding with ' + str(num1) + ' and ' + str(num2))

    for operation in operations:
        print("operation used is " + operation)
        CalculatorTwo.runoperation(operation, num1, num2)
        print() # new line

    print('\n')



