def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def chain_operations(x, y, operations):
    result = x
    for operation in operations:
        result = operation(result, y)
    return result