import time


print("Welcome to the smart console")
while True:
    # Smart console
    print("1. Calculator")
    print("2. Current time and date")
    print("3. Help")
    print("4. Quit")
    user_input = input("What would you like to do?:")

    # Calculator
    if user_input == "1":
        print("Welcome to the calculator")
        print("To quit write 'quit'")
        while True:
            equation = input("Enter your calculation:")
            # check what the user inputs and calculate accordingly
            if equation == "quit":
                break
            try:
                result = eval(equation)
                # Apply clip function to the result
                print(result)
            except:
                print("Invalid input")

    # Current time and date
    elif user_input == "2":
        print("\n Current time and date:")
        print(time.strftime("\n %H:%M:%S %d/%m/%Y \n"))
    elif user_input == "4":
        print("Quit")
        break

    # Help
    elif user_input == "3":
        print("\n 1. Calculator: Enter an equation and get the answer")
        print("\n 2. Current time and date: Get the current time and date")
        print("\n 3. Help: Get help")
        print("\n 4. Quit: Quit the program")
    else:
        print("Command not recognised")
