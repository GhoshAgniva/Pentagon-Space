import random

total_chance=3
win_count=0
lose_count=0

def cash_memo():
    print(''' 
+-------------------------+
| Minimum Deposit: 100    |
| Level 1: Minimum 100    |
| Level 2: Minimum 500    |
| Level 3: Minimum 1000   |
+-------------------------+
''')
    if level_input==1:
        if cash_deposite>=100:
            if win_count>0:
                print(f"you won the match you got{cash_deposite*2}Rs. Thank you")
            else:
                print(f"your current balance is {cash_deposite-100}")
        else:
            print("invalid input")
    if level_input==2:
        if cash_deposite>=500:
            if win_count>0:
                print(f"you won the match you got{cash_deposite*3}Rs. Thank you")
            else:
                print(f"your current balance is {cash_deposite-500}")
        else:
            print("invalid input")

    if level_input==3:
        if cash_deposite>=1000:
            if win_count>0:
                print(f"you won the match you got{cash_deposite*3}Rs. Thank you")
            else:
                print(f"your current balance is {cash_deposite-00}")
        else:
            print("invalid input")



def easy_gambling():
    global win_count,lose_count #since win_count and lose_count are global varriable so we need to inilize this
    easy_number_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"choose a number from the list: {easy_number_list}")
    for i in range(total_chance):
        user_choose=int(input("enter a number you choose:  "))
        #choosing random number by computer
        random_number=random.choice(easy_number_list)
        if user_choose==random_number:
            print(f"you choose {user_choose} and computer choose {random_number} and both are equal so you won the cash")
            win_count=win_count+1
        elif user_choose!=random_number:
            print(f"you choose {user_choose} and computer choose {random_number} and both not equal so you lose the game")
            lose_count=lose_count+1
        else:
            print("Invalid input")



def Medium_gambling():
    global win_count,lose_count
    medium_number_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    print(f"choose a number from the list: {medium_number_list}")
    for i in range(total_chance):
        user_choose = int(input("enter a number you choose:  "))
        # choosing random number by computer
        random_number = random.choice(medium_number_list)
        if user_choose == random_number:
            print(
                f"you choose {user_choose} and computer choose {random_number} and both are equal so you won the cash")
            win_count=win_count+1
        elif user_choose != random_number:
            print(
                f"you choose {user_choose} and computer choose {random_number} and both not equal so you lose the game")
            lose_count=lose_count+1
        else:
            print("Invalid input")



def Hard_gambling():
    global win_count,lose_count
    hard_number_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    print(f"choose a number from the list: {hard_number_list}")
    for i in range(total_chance):
        user_choose = int(input("enter a number you choose:  "))
        # choosing random number by computer
        random_number = random.choice(hard_number_list)
        if user_choose == random_number:
            print(
                f"you choose {user_choose} and computer choose {random_number} and both are equal so you won the cash")
            win_count=win_count+1

        elif user_choose != random_number:
            print(
                f"you choose {user_choose} and computer choose {random_number} and both not equal so you lose the game")
            lose_count=lose_count+1
        else:
            print("Invalid input")

print('''Welcome to the Casino
                        There are 3 levels
            +-------------------------------------+
            | 1. Easy (press 1 for Easy)          |
            | 2. Medium (press 2 for Medium)      |
            | 3. Hard (press 3 for Hard)          |
            |                                     |
            |                                     |
            |                                     |
            +-------------------------------------+
            Select your levels
''')
level_input=int(input("Enter your Level: "))
cash_deposite=int(input("Enter the amount : "))
if level_input==1:
    easy_gambling()
    cash_memo()
elif level_input==2:
    Medium_gambling()
    cash_memo()
elif level_input==3:
    Hard_gambling()
    cash_memo()
else:
    print("Invalid Input")




