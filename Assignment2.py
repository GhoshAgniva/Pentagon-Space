range_number = int(input("ENter the number: "))

for i in range(1, range_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("pentagon Space")
    elif i % 5 == 0 and i % 3 != 0:
        print("space")
    elif i % 3 == 0 and i % 5 != 0:
        print("pentagone")
    else:
        print(i)
