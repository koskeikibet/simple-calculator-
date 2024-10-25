# Function for Addition
def add(x, y):
    return x + y

# Function for Subtraction
def subtract(x, y):
    return x - y

# Function for Multiplication
def multiply(x, y):
    return x * y

# Function for Division
def divide(x, y):
    return x / y

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take the operation choice from the user
choice = input("Enter choice (1/2/3/4): ")

# Take input from the user for the two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the calculation based on the user's choice
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    if num2 != 0:
        print("Result:", divide(num1, num2))
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid choice!")
