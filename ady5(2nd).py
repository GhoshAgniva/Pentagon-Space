#finding substring from a string
str="If you think you can or you cannot you are right"
print(str.count("you"))
print(str)
str1="you"
print(str1 in str)
print(str.find("you"))
print(str.index("you"))
print(str.rfind("you"))
print(str.rindex("you"))
print(str.find("kohili"))


#checking the string contain the character or the number
str2=input()
if str2.isalpha():
    print("the string contain only alphabet")
if str2.isdigit():
    print("the string contain omly number")
if str2.isalnum():
    print("this string contain both")
