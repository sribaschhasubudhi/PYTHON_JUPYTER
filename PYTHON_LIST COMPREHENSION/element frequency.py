#  List of elements with their frequency in a dictionary

# Method-1:-
numbers=[1,1,1,2,3,5,5,5,5,7,9,5,3]
freq=[(i,numbers.count(i)) for i in set(numbers)]
freq=dict(freq)
print(freq)

# Method-2:-
numbers=[1,1,1,2,3,5,5,5,5,7,9,5,3]
freq2=[(i,numbers.count(i)) for i in dict.fromkeys(numbers)]
freq2=dict(freq2)
print(freq2)