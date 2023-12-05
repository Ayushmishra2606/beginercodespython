#Find the Number of Vowels, Consonants, Digits and White space in a String


st=input('enter the string')
vowel=0
consonant=0
dig=0
space=0

for i in st:
    if i in 'aeiouAEIOU':
         vowel+=1
    elif i.isalpha():
        consonant+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        dig+=1


print('no. of vowels',vowel)
print('no. of consonants',consonant)
print('no. of digits',dig)
print('no. of white space',space)
