line_1 = "qwertyuiop"
line_2 = "asdfghjkl"
line_3 = "zxcvbnm"


action = input("Encrypt or decrypt (e/d): ")
if action not in ["e", "d"]:
    print("Action is not valid...")
    exit(1)

text = input("Please enter text: ")
text = text.lower()

if action == "e":
    increment = 1
else:
    increment = -1

output_text = ""
for c in text:
    if c == " ":
        output_text += c
        continue

    found = False
    for line in [line_1, line_2, line_3]:
        if c in line:
            found = True
            index = line.index(c)
            new_index = (index + increment) % len(line)
            output_text += line[new_index]
            break

    if not found:
        output_text += c

print(output_text)
