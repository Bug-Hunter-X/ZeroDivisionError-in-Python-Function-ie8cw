def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # or raise a more informative error, like ValueError("Cannot divide by zero")

result = my_function(10, 0)
print(result) # Output: 0 