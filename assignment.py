str_input=input("enter the string: ")
words=str_input.split()
final_result=""
for i in words:
    final_result = i+" "+final_result
print(final_result)
new_result=final_result.split()
str2=new_result[0].upper()
for i in range(1,len(new_result)):
    str2 = str2+" "+new_result[i]
print(str2)
