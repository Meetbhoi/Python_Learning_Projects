import math  # Importing math module to use mathematical functions

# Basic Arithmetic Function
def algebra(x, y):
    Simple_Operatios = input("Enter the operation you want to perform (+, -, *, /): ")
    
    # Addition
    if Simple_Operatios == "+":
        print(f"The addition of {x} and {y} is: {x + y}")
    # Subtraction
    elif Simple_Operatios == "-":
        print(f"The subtraction of {x} and {y} is: {x - y}")
    # Multiplication
    elif Simple_Operatios == "*":
        print(f"The multiplication of {x} and {y} is: {x * y}")
    # Division with zero check
    elif Simple_Operatios == "/":
        if y == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"The division of {x} by {y} is: {x / y}")
    else:
        print("Invalid operation selected.")

# Advanced Mathematical Functions
def Math_Function():
    print("Select the type of function you want to perform:")
    print("Press 1 for Trigonometric operations\nPress 2 for Exponential and Logarithmic operations\nPress 3 for other functions like square, square root, etc.")

    n = int(input("Enter your choice (1/2/3): "))

    # Trigonometric Functions
    if n == 1:
        print("Choose a trigonometric operation:")
        print("1. sin\n2. cos\n3. tan\n4. cosec\n5. sec\n6. cot")
        n2 = int(input("Enter the operation number: "))
        a = float(input("Enter the angle in degrees: "))

        # Convert angle from degrees to radians
        angle_rad = math.radians(a)

        if n2 == 1:
            print(f"sin({a}) = {math.sin(angle_rad)}")
        elif n2 == 2:
            print(f"cos({a}) = {math.cos(angle_rad)}")
        elif n2 == 3:
            print(f"tan({a}) = {math.tan(angle_rad)}")
        elif n2 == 4:
            print(f"cosec({a}) = {1 / math.sin(angle_rad)}")
        elif n2 == 5:
            print(f"sec({a}) = {1 / math.cos(angle_rad)}")
        elif n2 == 6:
            print(f"cot({a}) = {1 / math.tan(angle_rad)}")
        else:
            print("Invalid operation number.")

    # Exponential and Logarithmic Functions
    elif n == 2:
        print("Choose an operation:")
        print("1. Exponential (e^x)\n2. Natural Logarithm (ln x)\n3. Logarithm base 10 (log₁₀ x)")
        choice = int(input("Enter your choice: "))
        num = float(input("Enter the number: "))

        if choice == 1:
            print(f"e^{num} = {math.exp(num)}")
        elif choice == 2:
            print(f"ln({num}) = {math.log(num)}")
        elif choice == 3:
            print(f"log₁₀({num}) = {math.log10(num)}")
        else:
            print("Invalid choice.")

    # Other Math Operations
    elif n == 3:
        print("Choose a function:")
        print("1. Square (x²)\n2. Square Root (√x)\n3. Cube (x³)\n4. Cube Root (∛x)")
        ch = int(input("Enter your choice: "))
        val = float(input("Enter the number: "))

        if ch == 1:
            print(f"{val}² = {val ** 2}")
        elif ch == 2:
            print(f"√{val} = {math.sqrt(val)}")
        elif ch == 3:
            print(f"{val}³ = {val ** 3}")
        elif ch == 4:
            print(f"∛{val} = {val ** (1/3)}")
        else:
            print("Invalid choice.")
    else:
        print("Invalid category selected.")

# 🌟 Main Program Execution Starts Here
print("Choose the type of calculation:")
print("Press 1 for basic arithmetic operations (+, -, ×, ÷)")
print("Press 2 for advanced functions (sin, cos, exp, etc.)")
i = int(input("Enter your choice (1/2): "))

# Handle choice between basic and advanced
if i == 1:
    X = float(input("Enter the value of X: "))
    Y = float(input("Enter the value of Y: "))
    algebra(X, Y)
elif i == 2:
    Math_Function()
else:
    print("Invalid selection. Please choose 1 or 2.")
