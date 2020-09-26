print("Want To Know Your Century Year")
name = input("Enter Your Name : ")
print(f"Hello {name} excited to Know your Century year\n")
b = int(input("Enter current Year : "))
a = int(input("Enter your age or birth year : "))

if len(str(a)) == 2 or len(str(a)) == 3:
    if a < 0:
        print("You don't even exist")
    elif a > 100:
        print("You are the oldest person alive")
        print(f"Century year achieved at year {b-(a-100)}")
    else:
        print(f"You will score your century after {100-a} years")
        print(f"You had achieved your century in year {100-a+b}")

elif len(str(a)) == 4:

    if b - a < 0:
        print("You don't even exist")
    elif b - a > 100:
        print("You are the oldest person alive")
        print(f"You had achieved your century in year {a+100}")
    else:
        print(f"You will score your century after {100-(b-a)} years")
        print(f"You will score your century in year {b+(100-(b-a))}")

else:
    print("Please Enter Correct data")
    exit()



