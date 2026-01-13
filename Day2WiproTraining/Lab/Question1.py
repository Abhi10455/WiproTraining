from functools import reduce

for i in range(1,21):
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumbers = list(filter(lambda x: x % 2 == 0, numbers))
print(evennumbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumbers = list(filter(lambda x: x % 2 == 0 , numbers))
sqevenumbers = list(map(lambda x: x ** 2, numbers))
print(sqevenumbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumbers = list(filter(lambda x: x % 2 == 0 , numbers))
sqevenumbers = list(map(lambda x: x ** 2, numbers))
sum = reduce(lambda x,y:x+y, numbers)
print(sum)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_evens = list(map(lambda x: x**2, even_numbers))
for index, value in enumerate(squared_evens):
    print(index, value)
