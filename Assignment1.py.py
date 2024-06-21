# IF CAPITAL THEN TURN INTO SMALL AND VICE VERSA WITHOUT USING INBUILT IN FUNCTION

data = input("Enter a character: ")
new_string = ""

for char in data:
    if 97 <= ord(char) <= 122:

        lowercase_char = chr(ord(char) - 32)
        new_string += lowercase_char

    elif 65 <= ord(char) <= 90:
        upper_case = chr(ord(char) + 32)
        new_string += upper_case  # Append the character itself

print(new_string)