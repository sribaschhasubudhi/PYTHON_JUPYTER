build=["Cement","Rod","Plank","Brick","Shovel"]

# Create a list of words with their characters sorted
revl=[''.join(sorted(i)) for i in build]
print(revl)

# Create a list of words with their characters sorted (both uppercase and lowercase letters treated equally)
revl2=[''.join(sorted(i,key=lambda x:x.lower())) for i in build]
print(revl2)

# Normal Method:-
sort_lst=[]
for materials in build:
    new="".join(sorted(materials))
    sort_lst.append(new)
print(sort_lst)