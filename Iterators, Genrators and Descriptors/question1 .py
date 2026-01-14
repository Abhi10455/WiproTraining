class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input("Enter N: "))
print("\nUsing Custom Iterator:")
for num in NumberIterator(n):
    print(num)
print("\nUsing Fibonacci Generator:")
for num in fibonacci(n):
    print(num)

