text = input("Enter a text: ")
norm_text = ""

for c in text:
    if c.isalpha():
        norm_text += c.lower()


is_palindrome = norm_text == norm_text[::-1]

if is_palindrome:
    print("Is a palindrome.")
else:
    print("Is not a palindrome.")

