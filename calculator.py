def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def modulo(x, y):
    """Modulo Function"""
    if y == 0:
        return "Error! Division by zero for modulo."
    else:
        return x % y


# Main function to run the calculator with the added modulo operation
def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulo")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)

        elif choice == '5':
            result = modulo(num1, num2)
            print(num1, "%", num2, "=", result)
    else:
        print("Invalid Input")


# The call to calculator() function is commented out to prevent automatic execution in this environment
calculator()
