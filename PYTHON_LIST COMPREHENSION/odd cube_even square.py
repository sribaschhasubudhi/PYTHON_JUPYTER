# Create a list of even numbers squared and odd numbers cubed from 1 to 10
numl=[1,2,3,4,5,6,7,8,9,10]
eol=[i**2 if i%2==0 else i**3 
     for i in numl]
print(eol)

# Normal method:-
eon_l=[]
for i in numl:
    if i%2==0:
        eon_l.append(i**2)
    elif i%2!=0:
        eon_l.append(i**3)
print(eon_l)
