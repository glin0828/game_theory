# Game theory: prisoners' dilemma
from random import randint

rounds = randint(1, 10)  # Randomly choose number of rounds between 1 and 10
# A simple game where a user plays against a computer in a modified version of the Prisoner's Dilemma.
print("Welcome to the modified Prisoner's Dilemma game!")
comp_count = 0
user_count = 0

for i in range(rounds):

    comp_num = int(randint(0, 1)) # Computer chooses 0 or 1 randomly (avoid bug: computer only chooseing 0...)
    user_num = int(input("Enter 0 or 1: "))

    if user_num > comp_num:
        user_count += 10
        comp_count -= 0
    elif user_num < comp_num:
        user_count -= 0
        comp_count += 10
    elif user_num == comp_num == 0:
        user_count += 8
        comp_count += 8
    elif user_num == comp_num == 1:
        user_count += -5
        comp_count += -5

    print(f"Round {i + 1}: You: {user_num}, Computer: {comp_num}")
    print(f"Scores - You: {user_count}, Computer: {comp_count}")

if user_count > comp_count:
    print("You won!")
elif user_count < comp_count:
    print("You lost...")
else:
    print("It's a tie!")