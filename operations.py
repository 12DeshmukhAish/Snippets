def arithmetic_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Example usage
num1 = 10
num2 = 5

print("Addition:", arithmetic_operation(num1, num2, 'add'))        # Output: 15
print("Subtraction:", arithmetic_operation(num1, num2, 'subtract')) # Output: 5
print("Multiplication:", arithmetic_operation(num1, num2, 'multiply')) # Output: 50
print("Division:", arithmetic_operation(num1, num2, 'divide'))       # Output: 2.0
print("Invalid operation:", arithmetic_operation(num1, num2, 'modulus')) # Output: Error: Invalid operation.
