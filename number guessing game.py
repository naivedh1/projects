import random as rd

play = True
a = rd.randint(1000, 9999)
print(f"(For testing) The number to guess is: {a}")  # 👈 Reveals the number at the beginning
turn = 6

print("WELCOME!!")
print("You have 6 chances to GUESS the NUMBER between 1000 & 9999")

while play and turn > 0:
    try:
        inp = int(input(f"\nTake a guess (Attempts left: {turn}): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if inp == a:
        print("Hurraayyyy!! You were spot on 🎉🎉")
        play = False

    elif inp < a:
        print("OOPS!! Wrong answer, You guessed TOO LOW")
        turn -= 1

    elif inp > a:
        print("OOPS!! Wrong answer, You guessed TOO HIGH")
        turn -= 1

    if inp != a and turn > 0:
        x = input("\nPress 1 if you want to continue, or 2 to exit: ")
        if x == '2':
            print("Thank you for playing. Goodbye!")
            break

if turn == 0 and inp != a:
    print(f"\nYou Lose! The correct number was {a}")
