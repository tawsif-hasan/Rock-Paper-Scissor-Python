import random

user = input("Choose: R for rock, P for paper and S for scissors")
computer = random.choice(("R", "P", "S"))

if (user == "R" and computer == "S") or (user == "S" and computer == "P") or (user == "P" and computer == "R"):
    print(computer)
    print("You Win")

elif (user == "R" and computer == "R") or (user == "S" and computer == "S") or (user == "P" and computer == "P"):
    print(computer)
    print("Tied")

else:
    print(f"Computer played: {computer}")
    print("You Lose")