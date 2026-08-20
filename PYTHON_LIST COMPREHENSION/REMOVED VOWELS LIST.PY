# Generate a list of strings with vowels removed
time=["hour","minutes","seconds","clock"]
nvl=[
    ''.join(ch for ch in word       # 2nd line
            if ch not in "aeiou")   # 3rd line
    for word in time                # 1st line
]
print(nvl)

# Normal Method:-
no_vowel_lst=[]
for word in time:
    no_vowel_word=""
    for i in word:
        if i not in "aeiou":
            no_vowel_word+=i
        else:
            pass
    no_vowel_lst.append(no_vowel_word)
print(no_vowel_lst)