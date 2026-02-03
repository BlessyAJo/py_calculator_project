from app.operations import addition, subtraction, multiplication, division

def calculator():
    
    # print a message to welcome the user to the calculator.
    print("Welcome to the calculator application! Type 'exit' to quit")
    
    while True:
        user_input = input("Enter an operation (+, -, *, /) and two numbers, or 'exit' to quit: ")

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break 

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue  

        if operation == "+":
            result = addition(num1, num2)  
        elif operation == "-":
            result = subtraction(num1, num2)  
        elif operation == "*":
            result = multiplication(num1, num2)  
        elif operation == "/":
            try:
                result = division(num1, num2) 
            except ValueError as e:
                # handles the case where someone tries to divide by zero, which we can't do.
                print(e)  
                continue 
        else:
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue 
        print(f"Result: {result}")
