# This is a standard calculator with no repeat calculation option
# It is also importable
# features clean code


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Cannot Divide by Zero")


def runoperation(operation, num1, num2):
    """ Determines Operation and prints result"""
    if operation == 1 or operation == "+":
        print(add(num1, num2))
    elif operation == 2 or operation == "-":
        print(sub(num1, num2))
    elif operation == 3 or operation == "*":
        print(mult(num1, num2))
    elif operation == 4 or operation == "/":
        print(div(num1, num2))
    else:
        print("Invalid Input. The Program will exit.")
        return


def main():

        validinput = False
        while not validinput:
            try:
                num1 = int(input("What is the first number?"))
                num2 = int(input("What is the second number?"))
                operation = int(input('Which Operation? 1)Add, 2)Subtract, 3)Multiply or 4)Divide?'))
                validinput = True
            except ValueError:
                print("Invalid Entry. Try Again.")
            except:
                print("Unknown Error")
            runoperation(operation, num1, num2)

# Allows us to import this file


if __name__ == "__main__":
    main()
