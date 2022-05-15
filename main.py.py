#Ask user to run operation -> validate
def run_calc():
    while True:
        global run_cal
        run_cal = input("Run a calculation? Enter either (yes/no) in lowercase: ")
        if run_cal not in ('yes', 'no'):
            print('Did not understand that. Please enter yes or no')
        else:
            return run_cal
            break

#Build function to accept user inputs and calculate values
def simple_cal():

    print("Choose Operation")
    print("1 .Add")
    print("2 .Subtract")
    print("3 .Mulitply")
    print("4 .Divide")

    while True:
        choice = input("Enter Operation 1, 2, 3, or 4: ")
        if choice not in ('1' ,'2', '3', '4'): #Validate user operation 
            print('Not a operation. Please select either 1, 2, 3, or 4')
        else:
            break

    while True:
        try:
            num1 = float(input("Enter first number: ")) #Validate num 1
        except ValueError:
            print('Not a number. Please try again')
        else:
            break
                        
    while True:
        try:
            num2 = float(input("Enter second number: ")) #validate num 2
        except ValueError:
            print('Not a number. Please try again')
        else:
            break

#Perfrom Calculations
    if choice == "1":
        addsum = num1 + num2
        print(num1, "+", num2, "=", addsum)

    if choice == "2":
        subtractsum = num1 - num2
        print(num1, "-", num2, "=", subtractsum)

    if choice == "3":
        multiplysum = num1 * num2
        print(num1, "*", num2, "=", multiplysum)

    if choice == "4":
        dividesum = num1 / num2
        print(num1, "/", num2, "=", dividesum)

#Run program
while True:
    run_calc()
    if run_cal == 'yes':
        simple_cal()
    else:
        print("Goodbye")
        break


