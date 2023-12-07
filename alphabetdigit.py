character = input("Enter a character: ")

if character.isalpha():
    print("The character is an alphabet.")
elif character.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")
