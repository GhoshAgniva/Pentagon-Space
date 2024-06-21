first_arm=int(input("Eneter the first arm: "))
second_arm=int(input("Eneter the second  arm: "))
third_arm=int(input("Eneter the thrid arm: "))
if first_arm>0 and second_arm>0 and third_arm>0:
    if first_arm==second_arm==third_arm:
        print("It is a Equal triangle")
    elif first_arm+second_arm>third_arm and second_arm+third_arm>first_arm and first_arm+third_arm>second_arm:
        print("triangle formed")
    else:
        print("not possible to form a triangle")
else:
    print("not possible to form a triangle")
