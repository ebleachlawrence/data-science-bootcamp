# Programme that asks users for two numbers and an operator and performs a caculation. 
# This calculation can then either be saved or viewed. The programme aims to handle various user errors.

# File path variable can be changed depending on the users' set up. This current file path works locally for me
file_path = './output.txt'

# Opening instructions for the user
print("This programme allows to you to complete a calculation, save the calculation and view completed calculations.")

# While loop to take initial user input and present error if input is not one of the two options
while True: 
    initial_input = input("Would you like to view create a new calculation or view previous files? Please enter either 'calculation' or 'file'\n")
    if initial_input.lower() == 'calculation':
        
        # Loop to request an integer and print error message if another data type is entered
        first_number = input("Please enter a number\n")
        while ValueError:
            try:
                float(first_number)
            except ValueError:
                print("Oops that wasn't a whole number!")
                first_number = input("Please try again and enter a whole number\n")
            else: 
                break
            

        # Same loop as above but for the second number
        second_number = input("Please enter a second number\n")
        while ValueError:
            try: 
                float(second_number)
            except ValueError:
                print("Oops that wasn't a whole number!")
                second_number = input("Please try again and enter a whole number\n")
            else: 
                break


        print("Your numbers are: ", first_number, " and ", second_number)


        # Final loop for user to input an operator with an error if they input something else
        while True:
            operation = str(input("What operation would you like to perform?  Please enter +, -, * or /\n"))
            if operation in ("+", "-", "*", "/"):
                break
            else:
                print("Oops that wasn't an operator! Please enter either +, -, / or *\n")
                

        # If statement statement that completes the relevant calculation and defines the output variable
        if operation == '+':
            calculation = float(first_number) + float(second_number)
        elif operation == '-':
            calculation = float(first_number) - float(second_number)
        elif operation == '/':
            
            # Including more error handling for a ZeroDivisonError
            try: 
                calculation = float(first_number) / float(second_number)
            except ZeroDivisionError:
                print("Oops! You can't divide a number by zero! Please choose a different number\n")
                second_number = input("Please enter a second number\n")
                while ValueError:
                    try: 
                        float(second_number)
                    except ValueError:
                        print("Oops that wasn't a whole number!")
                        second_number = input("Please try again and enter a whole number\n")
                    else: 
                        break
                calculation = float(first_number) / float(second_number)
        elif operation == '*':
            calculation = float(first_number) * float(second_number)
        else: 
            print("Error: Please restart the programme")


        output = f"The calculation was {first_number} {operation} {second_number} = {calculation}"
        print(output)
        print("Your result will now be saved to 'output.txt'")

        # Either creates or amends existing output.txt and appends the new calculation to the file
        file = open(file_path, "a")
        file.write(output + "\n")
        file.close()

        # Loop that asks the user if they would like to open the file and ends the programme if not
        while True:
            open_file = input("Would you like to open the file?\n")
            if open_file.lower() == "yes":
                with open(file_path, "r") as file:
                    # Print to terminal for ease of checking but can be changed to just read
                    print(file.read())
                break
            elif open_file.lower() == "no":
                break
            else:
                print("Please enter either 'yes' or 'no' ")
        break

    # Second loop for if the user wants to open a file, with error handling
    elif initial_input.lower() == 'file':
        while OSError: 
            file_name = input("What is the name of the file you would like to open?\n")
            try:
                with open(file_name, "r") as file:
                    print(file.read())
                break
        
        # This was the error I was recieving instead of FileNotFound, not sure if it needs to be changed but might just be my set up
            except OSError as error:
                print("Sorry ", file_name, " could not be found. Please try again")
        break
    else:
        print("Oops! Please enter either 'calculation' or 'file'\n")
print("Thank you. End of programme.")