# decimal_number=int(input("enter the number "))
# binary_number=""
# while decimal_number>0:
#     reminder=decimal_number%2
#     binary_number=str(reminder)+binary_number
#     decimal_number=decimal_number//2
# print(binary_number)

#binary to decimal

binary_number=input("enter the binary number: ")
decimal_number=0
for i in binary_number:
    decimal_number=decimal_number*2+int(i)
print(decimal_number)



