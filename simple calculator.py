# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Dictionary to map operator symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Get a series of numbers and operators from the user
user_input = input("Enter a series of numbers and operators (e.g., 5 + 3 - 2 * 4): ")
tokens = user_input.split()  # Split input into tokens (e.g., ["5", "+", "3", "-", "2", "*", "4"])

# Create an iterator for the tokens
token_iter = iter(tokens)

# Start with the first number
result = float(next(token_iter))  # Convert the first number to float

# Iterate through the rest of the tokens
for token in token_iter:
    operator = token  # Get the operator (e.g., "+")
    next_number = float(next(token_iter))  # Get the next number
    
    # Use the operator to perform the corresponding calculation
    if operator in operations:
        result = operations[operator](result, next_number)
    else:
        print(f"Invalid operator: {operator}")
        break

# Print the final result
print("Result:", result)
