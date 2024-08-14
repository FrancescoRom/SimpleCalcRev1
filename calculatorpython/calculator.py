
# simple calculator

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


print("SELECT OPERATION")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")

while True:

    while True:

        choice = input("What calculation do you want to do? (1/2/3/4): ") # asking the user for operation

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input")
                break

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}") # add
            
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}") # subtract
            
        elif choice == "3":
            print(f"{num1} / {num2} = {divide(num1, num2)}") # divide
            
        elif choice == "4":
            print(f"{num1} * {num2} = {multiply(num1, num2)}") # multiply

        elif choice != ("1", "2", "3", "4"):
            print("Please enter a number between 1 and 4.") # if user enters anything else than a number between 1 and 4

        while True: # loop until user enters y or n
            next_calculation = input("Want to continue? (y/n): ")
            if next_calculation == "y":
                break
            elif next_calculation == "n":
                print("Okay, till next time!")
                exit()
            else:
                print("Invalid input, please enter 'y' or 'n'.")
            

    
            

