
# add function
def addition(a: float, b: float)-> float:
    return a + b
# subtract function
def subtraction(a: float, b: float)-> float:
    return a - b
# multiply function
def multiplication(a: float, b: float)-> float:
    return a * b
# divide function
def division(a: float, b: float)-> float:
    if b == 0:
         raise ValueError("Cannot divide by zero.")
    return a / b