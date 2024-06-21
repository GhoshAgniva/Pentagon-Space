#Removing the space between the character
str1=input()
new_str=""
i=0
while(i<=len(str1)-1):
    data=str1[i]
    if data==" ":
        i=i+1
    else:
        new_str=new_str+data
        i=i+1
print(new_str)




