# Generate a list of pairs of numbers where the sum of each pair is prime
# Normal Method:-
prime_list=[]
for i in range(0,11):
    for j in range(2,11):
        is_prime=True
        for k in range(2,i+j):
            total=i+j
            if total%k==0:
                is_prime=False
                break

        if is_prime:
            prime_list.append((i,j))
print(prime_list)

# List Comprehension Method:-
primetl=[(i,j)
         for i in range(0,11)
                  for j in range(2,11)
         if all((i+j)%k!=0 for k in range(2,i+j))
         ]
print(primetl)