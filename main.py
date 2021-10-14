import random
user_points = 0
pc_points = 0
user_value = 0
pc_value = random.randint(0, 2)
no_of_turns = 0
# 0--> Rock
# 1 --> paper
# 2 -->scissors


while no_of_turns <= 2:
    user_input = input("Type in 'Rock'/'paper'/'scissors' to play or q to quit: ").lower()
    if user_input == "q":
        print('Thanks for playing')
        quit()
    elif user_input not in ("rock", "paper", "scissors"):
        print("Type a valid command")
        continue
    elif user_input == "rock":
        user_value = 0
        no_of_turns += 1
    elif user_input == "paper":
        user_value = 1
        no_of_turns += 1
    elif user_input == "scissors":
        user_value = 2
        no_of_turns += 1
# 0>rock 1>paper 2>scissors
if user_value == 0 and pc_value == 1:
    pc_points += 1
    print("Pc won")
elif user_value == 0 and pc_value == 2:
    user_points += 1
elif user_value == 1 and pc_value == 0:
    user_points += 1
elif user_value == 1 and pc_value == 2:
    pc_points += 1
elif user_value == 2 and pc_value == 0:
    pc_points += 1
elif user_value == 2 and pc_value == 1:
    user_points += 1

if user_points > pc_points:
    print("Hurray you won")
elif user_points == pc_points:
    print("Draw")
else: print("Sorry you lost")





