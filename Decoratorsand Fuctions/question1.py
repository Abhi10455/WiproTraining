import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
        return result
    return wrapper

def write_numbers_to_file(file):
    with open(file, "w") as file:
        for i in range(1, 11):
            file.write(str(i) + "\n")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
result = factorial(num)
print(f"Factorial of {num} is {result}")

