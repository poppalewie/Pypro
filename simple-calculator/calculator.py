def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2

def subtract(num1, num2):
    return num1 - num2

def main():
    while True:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter Second Number: "))
            operator = input("Choose operation (+, -, /, *) or 'q' to quit: ")

            if operator.lower() == 'q':
                print("Goodbye!")
                break

            if operator == "+":
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif operator == "*":
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif operator == "-":
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif operator == "/":
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Invalid operator.")
        
        except ValueError as e:
            if str(e) == "Cannot divide by zero":
                print("Error: Division by zero is not allowed")
            else:
                print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()