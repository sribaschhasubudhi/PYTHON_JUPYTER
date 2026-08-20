from itertools import tee

numbers = iter([1,2,3])

a, b = tee(numbers)

print(next(a))
print(next(b))
print(next(a))
print(next(b))