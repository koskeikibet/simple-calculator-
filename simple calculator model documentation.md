
# Project Title

A brief description of what this project does and who it's for

Here's a professional documentation for the calculator code you provided. This documentation includes explanations for each function and a usage guide, and is structured to be user-friendly and comprehensive.

---

# Calculator Program Documentation

## Overview

This calculator program performs basic arithmetic operations (+, -, *, /) on a sequence of numbers and operators entered by the user. It processes the user’s input and calculates the result in a sequential (left-to-right) manner, regardless of traditional operator precedence.

## Prerequisites

- **Python 3.6+** is required.

## Code Walkthrough

### 1. **Define Calculator Functions**

Each arithmetic operation is implemented as a separate function, making it easy to reference and extend.

```python
def add(x, y):
    return x + y
```

- **`add(x, y)`**: Returns the sum of `x` and `y`.
  
```python
def subtract(x, y):
    return x - y
```

- **`subtract(x, y)`**: Returns the difference between `x` and `y`.

```python
def multiply(x, y):
    return x * y
```

- **`multiply(x, y)`**: Returns the product of `x` and `y`.

```python
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
```

- **`divide(x, y)`**: Returns the quotient of `x` divided by `y`. Checks for division by zero to avoid errors.

### 2. **Dictionary Mapping**

The `operations` dictionary maps each operator symbol to its corresponding function. This allows the program to dynamically select the correct function based on the operator.

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

### 3. **Processing User Input**

The program accepts a series of numbers and operators from the user in a single line, then splits this input into tokens.

```python
user_input = input("Enter a series of numbers and operators (e.g., 5 + 3 - 2 * 4): ")
tokens = user_input.split()  # Split input into tokens
```

Each token is processed sequentially to calculate the result.

### 4. **Main Calculation Logic**

The program starts with the first number as the initial result, then iterates through the remaining tokens, applying each operator to the current result and the next number.

```python
result = float(next(token_iter))  # Start with the first number
for token in token_iter:
    operator = token  # Get the operator
    next_number = float(next(token_iter))  # Get the next number
    if operator in operations:
        result = operations[operator](result, next_number)
    else:
        print(f"Invalid operator: {operator}")
        break
```

### 5. **Output**

The final result is printed once all operations have been processed.

```python
print("Result:", result)
```

## Usage Instructions

1. **Run the Script**:
   - Run the script in a Python environment.
   
2. **Provide Input**:
   - Enter a series of numbers and operators in the format:
     ```
     5 + 3 - 2 * 4
     ```
   - The program will calculate the result based on the sequence of inputs.

3. **Handling Errors**:
   - Division by zero will trigger an error message: `Error: Cannot divide by zero`.
   - An invalid operator (not +, -, *, or /) will terminate the program with a message.

## Future Enhancements

- **Operator Precedence**: Implement traditional operator precedence (e.g., multiplication and division before addition and subtraction).
- **Parentheses Support**: Add support for parentheses to group expressions.

## License

This code is provided under the MIT License. You are free to modify and distribute it as long as attribution is provided to the original author.

--- 

Let me know if you'd like any additional details or examples!