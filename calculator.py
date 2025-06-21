def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        else:
            return num1 / num2
    else:
        return "Invalid operator!"

# Main program starts here
print("Simple Calculator")
print("------------------")

try:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")
